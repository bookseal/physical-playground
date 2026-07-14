#!/usr/bin/env python3
"""Guard: every relative link between our docs must actually resolve.

The playbook is published — a dead link is a 404 in a visitor's face, and the docs
lean hard on cross-references. External http(s) links are NOT checked: they break for
reasons we do not control, and a CI job that fails because someone else's site is down
is a job people learn to ignore.

Run it yourself, exactly as CI does:   python3 ops/ci/check-links.py
"""
import os
import re
import subprocess
import sys
from urllib.parse import unquote, urlparse

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                      capture_output=True, text=True, check=True).stdout.strip()
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")          # [text](target)


def tracked_markdown():
    out = subprocess.run(["git", "ls-files", "*.md"], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout
    return [p for p in out.splitlines() if p]


def is_external(target):
    return bool(urlparse(target).scheme) or target.startswith(("#", "mailto:", "//"))


def main():
    broken = []
    checked = 0
    for rel in tracked_markdown():
        path = os.path.join(ROOT, rel)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        for m in LINK.finditer(text):
            target = m.group(1).strip().split(" ")[0]        # drop an optional "title"
            if not target or is_external(target):
                continue
            if target.startswith("[["):                       # wiki-style link, not a path
                continue
            target = unquote(target.split("#", 1)[0])         # drop the anchor
            if not target:
                continue
            checked += 1
            resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
            if not os.path.exists(resolved):
                line = text[: m.start()].count("\n") + 1
                broken.append(f"      {rel}:{line}  ->  {target}")

    print(f"▸ links: {checked} relative links across {len(tracked_markdown())} tracked .md files")
    if broken:
        print("  ✗ these point at nothing:")
        print("\n".join(broken))
        print("\n✗ link check FAILED")
        return 1
    print("  ✓ every relative link resolves\n\n✓ link check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
