#!/usr/bin/env python3
"""Physical Spark — 랜딩 페이지 + 문서 뷰어를 한 프로세스가 서빙한다.

  /        랜딩 페이지 (site/index.html)
  /docs    문서 뷰어 — 레포의 .md/.txt를 브라우저에서 읽는다
  /api/*   뷰어가 쓰는 파일 트리·내용 API
  그 외    site/ 정적 파일 (courses/, assets/, auth.js …)

로컬:  python3 viewer/server.py            → http://localhost:8766  (편집 가능)
배포:  k8s가 python:3.12-alpine 안에서 이 파일을 실행하고, READ_ONLY=1을 준다.
       레포는 hostPath로 마운트되므로 git pull 하면 문서가 곧바로 반영된다.

공개 서버에서 편집을 열어두면 아무나 문서를 덮어쓸 수 있다 — READ_ONLY가 그걸 막는다.
의존성 없음 (Python 표준 라이브러리만 사용).
"""
import json
import mimetypes
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST = os.environ.get("HOST", "127.0.0.1")  # 컨테이너에선 0.0.0.0
PORT = int(os.environ.get("PORT", "8766"))
READ_ONLY = os.environ.get("READ_ONLY") == "1"
EXCLUDE_DIRS = {".git", "node_modules", "__pycache__", ".DS_Store", "viewer"}
EXCLUDE_PREFIXES = ("backup_",)
EXTENSIONS = (".md", ".txt", ".html")


def scan_files():
    files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [
            d for d in dirnames
            if d not in EXCLUDE_DIRS and not d.startswith(EXCLUDE_PREFIXES) and not d.startswith(".")
        ]
        for name in filenames:
            if not name.lower().endswith(EXTENSIONS) or name.startswith("."):
                continue
            if "local-command-caveat" in name.lower():  # 대화 export 덤프는 숨김
                continue
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, ROOT)
            try:
                mtime = os.path.getmtime(full)
            except OSError:
                continue
            files.append({"path": rel, "name": name, "mtime": mtime})
    return files


def safe_path(rel):
    full = os.path.realpath(os.path.join(ROOT, rel))
    if not full.startswith(os.path.realpath(ROOT) + os.sep):
        return None
    return full if os.path.isfile(full) else None


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def send_json(self, obj, status=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_html(self, full):
        with open(full, "rb") as f:
            body = f.read()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        url = urlparse(self.path)
        if url.path in ("/docs", "/docs/"):
            self.send_html(os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html"))
        elif url.path == "/api/config":
            # 뷰어가 켜질 때 물어본다 — 읽기 전용이면 Save 버튼을 감춘다.
            self.send_json({"read_only": READ_ONLY})
        elif url.path.startswith("/assets/"):  # 랜딩 페이지의 상대 이미지 서빙 (site/assets/)
            full = safe_path("site" + url.path)
            if not full:
                self.send_json({"error": "not found"}, 404)
                return
            ctype = mimetypes.guess_type(full)[0] or "application/octet-stream"
            with open(full, "rb") as f:
                body = f.read()
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif url.path == "/raw":
            rel = parse_qs(url.query).get("path", [""])[0]
            full = safe_path(rel)
            if not full:
                self.send_json({"error": "not found"}, 404)
                return
            ctype = mimetypes.guess_type(full)[0] or "application/octet-stream"
            if ctype.startswith("text/"):
                ctype += "; charset=utf-8"
            with open(full, "rb") as f:
                body = f.read()
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif url.path == "/api/tree":
            self.send_json(scan_files())
        elif url.path == "/api/file":
            rel = parse_qs(url.query).get("path", [""])[0]
            full = safe_path(rel)
            if not full:
                self.send_json({"error": "not found"}, 404)
                return
            with open(full, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
            self.send_json({"path": rel, "content": content, "mtime": os.path.getmtime(full)})
        else:
            # site/ 정적 파일 서빙 (courses 등) — GitHub Pages와 동일 동작
            rel = url.path.lstrip("/")
            cands = [os.path.join("site", rel)]
            if rel.endswith("/") or "." not in rel.split("/")[-1]:
                cands.append(os.path.join("site", rel, "index.html"))
            full = next((p for p in (safe_path(c) for c in cands) if p), None)
            if not full:
                self.send_json({"error": "not found"}, 404)
                return
            ctype = mimetypes.guess_type(full)[0] or "application/octet-stream"
            if ctype.startswith("text/"):
                ctype += "; charset=utf-8"
            with open(full, "rb") as f:
                body = f.read()
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    def do_POST(self):
        url = urlparse(self.path)
        if url.path == "/api/save":
            # 진짜 방어선. 클라이언트에서 Save 버튼을 감추는 것만으론 부족하다 —
            # curl 한 줄이면 우회되므로, 배포 환경에선 서버가 직접 거절해야 한다.
            if READ_ONLY:
                self.send_json({"error": "read-only server — editing is local only"}, 403)
                return
            length = int(self.headers.get("Content-Length", 0))
            try:
                payload = json.loads(self.rfile.read(length) or b"{}")
            except ValueError:
                self.send_json({"error": "bad json"}, 400)
                return
            rel = payload.get("path", "")
            content = payload.get("content", "")
            full = safe_path(rel)  # 기존 경로 검증 재사용 — ROOT 밖 저장 차단 + 파일 존재 확인
            if not full or not rel.lower().endswith(EXTENSIONS):
                self.send_json({"error": "not found"}, 404)
                return
            with open(full, "w", encoding="utf-8") as f:
                f.write(content)
            self.send_json({"path": rel, "content": content, "mtime": os.path.getmtime(full)})
        else:
            self.send_json({"error": "not found"}, 404)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"문서 뷰어: http://localhost:{PORT}  (루트: {ROOT})")
    server.serve_forever()
