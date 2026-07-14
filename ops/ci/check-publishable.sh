#!/usr/bin/env bash
# Guard: nothing lands in git that we are not allowed — or do not want — to publish.
#
# This repo IS the deploy artifact: the server does `git reset --hard origin/main`
# and serves that checkout. So "tracked" and "published on the public internet" are
# the same thing. A file slipping into git is not a style problem, it is a release.
#
# Run it yourself, exactly as CI does:   ops/ci/check-publishable.sh
set -uo pipefail
fail=0
note() { printf '  %s\n' "$*"; }
bad()  { printf '  ✗ %s\n' "$*"; fail=1; }

echo "▸ copyright: no third-party material may be tracked"
# Re-Volt (1999, Acclaim) screenshots are design reference only — see CREDITS.md.
if leaked=$(git ls-files 'design/_refs/rv-*'); then
  if [ -n "$leaked" ]; then
    bad "Re-Volt screenshots are tracked — these must stay local:"
    printf '      %s\n' $leaked
  else
    note "✓ no rv-* tracked"
  fi
fi

echo "▸ weight: heavy originals stay local, only the webp ships"
if leaked=$(git ls-files 'design/_refs/gen-*.png'); then
  if [ -n "$leaked" ]; then
    bad "PNG originals are tracked — commit the .webp instead:"
    printf '      %s\n' $leaked
  else
    note "✓ no gen-*.png tracked"
  fi
fi

echo "▸ weight: no single tracked file over 8MB"
# A git repo never gets smaller. Catching a fat file before it lands is the only
# cheap moment; after it is committed, removing it means rewriting history.
big=$(git ls-files -z | xargs -0 -I{} sh -c 'test -f "{}" && printf "%s %s\n" "$(wc -c <"{}")" "{}"' \
      | awk '$1 > 8388608 {printf "      %.1fMB  %s\n", $1/1048576, $2}')
if [ -n "$big" ]; then
  bad "files over 8MB are tracked:"
  printf '%s\n' "$big"
else
  note "✓ nothing over 8MB"
fi

echo "▸ privacy: local-only context must never be tracked"
# CLAUDE.md and conversation dumps hold personal context. They are gitignored, and
# because the server only ever gets what git has, that ignore IS the publish boundary.
for f in CLAUDE.md .gitleaks.toml; do
  if git ls-files --error-unmatch "$f" >/dev/null 2>&1; then
    bad "$f is tracked — it is meant to stay local"
  fi
done
[ "$fail" -eq 0 ] && note "✓ no private files tracked"

echo
if [ "$fail" -ne 0 ]; then
  echo "✗ publishable check FAILED — see above"
  exit 1
fi
echo "✓ publishable check passed"
