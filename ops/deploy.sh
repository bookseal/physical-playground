#!/usr/bin/env bash
# The real deploy logic, run ON the bit-habit server by the SSH forced command.
#
# The server's ~/workspace/physical-spark-deploy.sh is a 4-line bootstrap that
# pulls this repo and then `exec`s this file, passing the commit we were on
# BEFORE the pull. That indirection is what makes this script itself deployable:
# change it, push, and the next deploy already runs the new version.
#
#   usage: ops/deploy.sh <previous-HEAD-sha | "none">
set -euo pipefail

before="${1:-none}"
cd /home/ubuntu/workspace/physical-spark

echo "physical-spark updated to $(git rev-parse --short HEAD) at $(date -u +%FT%TZ)"

# Did anything under <path> change in this deploy? A first-ever deploy ("none")
# counts as "everything changed" so every component gets applied once.
changed() {
  [ "$before" = none ] && return 0
  git diff --name-only "$before" HEAD | grep -q "^$1"
}

# --- site + docs playbook ----------------------------------------------------
# viewer/server.py serves both, reading this checkout through a hostPath mount,
# so new pages and new docs are live the moment the bootstrap's git reset lands.
# Its CODE, though, is loaded into memory at startup — so a change to the server
# itself only takes effect after a restart. Content: free. Code: one restart.
if changed viewer/; then
  echo "viewer/ changed -> restart the site pod to reload server.py"
  sudo -n k3s kubectl rollout restart deploy/physical-spark
fi

# --- auth service ------------------------------------------------------------
# A real container image, so it needs a build + a rollout to pick up new code.
if changed auth/; then
  echo "auth/ changed -> rebuild image + restart"
  docker build -q -t localhost:5000/pr-auth:latest auth/ >/dev/null
  docker push -q localhost:5000/pr-auth:latest >/dev/null 2>&1 \
    || docker push localhost:5000/pr-auth:latest
  sudo -n k3s kubectl rollout restart deploy/pr-auth
fi

# --- k8s manifests -----------------------------------------------------------
# The gap we're closing: until now, editing k8s/site.yaml or auth/k8s/*.yaml
# shipped the file to the server but never told the cluster about it.
#
# Applied unconditionally, not just when they change. `apply` is idempotent —
# an unchanged manifest costs one "unchanged" line — and applying every time
# makes the deploy self-healing: whatever anyone poked by hand on the box gets
# reset to what's in git. The manifests, not the cluster, are the source of truth.
echo "applying k8s manifests"
sudo -n k3s kubectl apply -f k8s/site.yaml -f auth/k8s/
