#!/usr/bin/env python3
"""physical-ai-edu 문서 뷰어 — 워크스페이스의 .md/.txt를 브라우저에서 본다.

실행:  python3 viewer/server.py   →  http://localhost:8766
(다른 워크스페이스 뷰어와 겹치지 않게 :8766 사용 — 동시 실행 가능)
의존성 없음 (Python 표준 라이브러리만 사용).
"""
import json
import mimetypes
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 8766
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

    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/":
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html"), "rb") as f:
                body = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif url.path == "/landing":
            landing = os.path.join(ROOT, "site", "index.html")
            if not os.path.isfile(landing):
                self.send_json({"error": "landing not found"}, 404)
                return
            with open(landing, "rb") as f:
                body = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
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
            self.send_json({"error": "not found"}, 404)

    def do_POST(self):
        url = urlparse(self.path)
        if url.path == "/api/save":
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
