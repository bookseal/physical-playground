"""Physical Spark — passwordless auth (email magic-link). MVP.

Flow:
  POST /api/auth/start   {email}          -> emails a one-time magic link
  GET  /api/auth/verify  ?token=...       -> validates, find-or-creates user, sets session cookie
  GET  /api/auth/me                       -> {email, nickname} or 401
  POST /api/auth/logout                   -> clears session

Security posture (MVP — review before real users): single-use tokens hashed at
rest, 15-min TTL; httpOnly+Secure+SameSite cookies; no passwords; no account
enumeration on /start. Email creds come from env (a k8s secret) — never hardcoded.
"""

import hashlib
import os
import smtplib
import sqlite3
import ssl
import time
from email.message import EmailMessage

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr

from nicknames import generate_nickname

DB_PATH = os.environ.get("PS_AUTH_DB", "/data/auth.db")
SITE = os.environ.get("PS_SITE", "https://physical-spark.bit-habit.com")
COOKIE_DOMAIN = os.environ.get("PS_COOKIE_DOMAIN", ".bit-habit.com")
TOKEN_TTL = 15 * 60          # magic link valid 15 min
SESSION_TTL = 30 * 24 * 3600  # session valid 30 days
RESEND_COOLDOWN = 30          # min seconds between links per email

app = FastAPI(title="pr-auth")


def db():
    con = sqlite3.connect(DB_PATH)
    con.execute("PRAGMA journal_mode=WAL")
    return con


def init_db():
    con = db()
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            nickname TEXT UNIQUE NOT NULL,
            created_at INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS login_tokens(
            token_hash TEXT PRIMARY KEY,
            email TEXT NOT NULL,
            expires_at INTEGER NOT NULL,
            used INTEGER NOT NULL DEFAULT 0,
            created_at INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS sessions(
            id TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            expires_at INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS scores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL,
            level INTEGER NOT NULL,
            created_at INTEGER NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_scores_top ON scores(score DESC);
        """
    )
    con.commit()
    con.close()


init_db()


def now():
    return int(time.time())


def _token():
    import secrets
    return secrets.token_urlsafe(32)


def send_email(to_addr: str, subject: str, body: str):
    """Send via SMTP from env; if unconfigured, log the link (dev mode)."""
    host = os.environ.get("SMTP_HOST")
    if not host:
        print(f"[DEV EMAIL] to={to_addr} :: {body}", flush=True)
        return
    msg = EmailMessage()
    msg["From"] = os.environ.get("SMTP_FROM", "no-reply@bit-habit.com")
    msg["To"] = to_addr
    msg["Subject"] = subject
    msg.set_content(body)
    port = int(os.environ.get("SMTP_PORT", "587"))
    with smtplib.SMTP(host, port, timeout=15) as s:
        s.starttls(context=ssl.create_default_context())
        user = os.environ.get("SMTP_USER")
        if user:
            s.login(user, os.environ.get("SMTP_PASS", ""))
        s.send_message(msg)


class StartReq(BaseModel):
    email: EmailStr


@app.post("/api/auth/start")
def start(req: StartReq):
    email = req.email.lower().strip()
    con = db()
    # rate limit: one link per RESEND_COOLDOWN seconds per email
    recent = con.execute(
        "SELECT created_at FROM login_tokens WHERE email=? ORDER BY created_at DESC LIMIT 1",
        (email,),
    ).fetchone()
    if recent and now() - recent[0] < RESEND_COOLDOWN:
        con.close()
        return {"ok": True, "message": "Check your email for a sign-in link."}
    token = _token()
    th = hashlib.sha256(token.encode()).hexdigest()
    con.execute(
        "INSERT INTO login_tokens(token_hash,email,expires_at,used,created_at) VALUES(?,?,?,0,?)",
        (th, email, now() + TOKEN_TTL, now()),
    )
    con.commit()
    con.close()
    link = f"{SITE}/api/auth/verify?token={token}"
    send_email(
        email,
        "Sign in to Physical Spark",
        f"Click to sign in (valid 15 minutes):\n\n{link}\n\n"
        f"If you didn't request this, you can ignore this email.",
    )
    # Always the same response — no account enumeration.
    return {"ok": True, "message": "Check your email for a sign-in link."}


@app.get("/api/auth/verify")
def verify(token: str):
    th = hashlib.sha256(token.encode()).hexdigest()
    con = db()
    row = con.execute(
        "SELECT email, expires_at, used FROM login_tokens WHERE token_hash=?", (th,)
    ).fetchone()
    if not row or row[2] or row[1] < now():
        con.close()
        raise HTTPException(400, "This sign-in link is invalid or has expired.")
    email = row[0]
    con.execute("UPDATE login_tokens SET used=1 WHERE token_hash=?", (th,))
    u = con.execute("SELECT id FROM users WHERE email=?", (email,)).fetchone()
    if u:
        uid = u[0]
    else:
        nick = generate_nickname(
            lambda n: con.execute("SELECT 1 FROM users WHERE nickname=?", (n,)).fetchone()
            is not None
        )
        uid = con.execute(
            "INSERT INTO users(email,nickname,created_at) VALUES(?,?,?)",
            (email, nick, now()),
        ).lastrowid
    sid = _token()
    con.execute(
        "INSERT INTO sessions(id,user_id,expires_at) VALUES(?,?,?)",
        (sid, uid, now() + SESSION_TTL),
    )
    con.commit()
    con.close()
    resp = RedirectResponse(SITE + "/?welcome=1", status_code=302)
    resp.set_cookie(
        "pr_session", sid, max_age=SESSION_TTL, httponly=True, secure=True,
        samesite="lax", domain=COOKIE_DOMAIN, path="/",
    )
    return resp


def current_user(request: Request):
    sid = request.cookies.get("pr_session")
    if not sid:
        return None
    con = db()
    row = con.execute(
        "SELECT u.email, u.nickname, s.expires_at FROM sessions s "
        "JOIN users u ON u.id = s.user_id WHERE s.id=?",
        (sid,),
    ).fetchone()
    con.close()
    if not row or row[2] < now():
        return None
    return {"email": row[0], "nickname": row[1]}


@app.get("/api/auth/me")
def me(request: Request):
    u = current_user(request)
    if not u:
        raise HTTPException(401, "not signed in")
    return u


@app.post("/api/auth/logout")
def logout(request: Request):
    sid = request.cookies.get("pr_session")
    if sid:
        con = db()
        con.execute("DELETE FROM sessions WHERE id=?", (sid,))
        con.commit()
        con.close()
    resp = JSONResponse({"ok": True})
    resp.delete_cookie("pr_session", domain=COOKIE_DOMAIN, path="/")
    return resp


@app.get("/api/auth/health")
def health():
    return {"ok": True}


# ---- arcade scoreboard (Physical Spark mini-game) ------------------------

def _clean_name(raw: str) -> str:
    # keep it arcade-simple: printable, trimmed, max 16 chars; fall back to AAA
    name = "".join(c for c in (raw or "") if c.isprintable()).strip()[:16]
    return name or "AAA"


def _top(con, limit: int):
    rows = con.execute(
        "SELECT name, score, level, created_at FROM scores "
        "ORDER BY score DESC, created_at ASC LIMIT ?",
        (limit,),
    ).fetchall()
    return [
        {"name": r[0], "score": r[1], "level": r[2], "created_at": r[3]}
        for r in rows
    ]


class ScoreReq(BaseModel):
    name: str
    score: int
    level: int = 0


@app.post("/api/scores")
def post_score(req: ScoreReq, request: Request):
    # signed-in players post under their nickname; guests under the typed name
    u = current_user(request)
    name = u["nickname"] if u else _clean_name(req.name)
    score = max(0, min(int(req.score), 10_000_000))
    level = max(0, min(int(req.level), 999))
    con = db()
    con.execute(
        "INSERT INTO scores(name,score,level,created_at) VALUES(?,?,?,?)",
        (name, score, level, now()),
    )
    con.commit()
    top = _top(con, 10)
    con.close()
    return {"ok": True, "top": top}


@app.get("/api/scores")
def get_scores(limit: int = 10):
    con = db()
    top = _top(con, max(1, min(limit, 100)))
    con.close()
    return {"top": top}
