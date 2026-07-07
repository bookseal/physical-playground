#!/bin/zsh
cd "$(dirname "$0")"
echo "Physical AI 교육 문서 뷰어 → http://localhost:8766"
open "http://localhost:8766"
python3 server.py
