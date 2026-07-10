# Deployment & CD

How `physical-spark.bit-habit.com` ships, following the same pattern as the
other services on the bit-habit k3s box (`static-web`, `llm-app-lab`, …).

## TL;DR

Push to `main` → GitHub Actions SSHes into the server → the server pulls this
repo and (only if `auth/` changed) rebuilds the auth image. No manual step.

```
git push origin main      # that's the whole deploy
```

You can also trigger it by hand from the repo's **Actions** tab
(`workflow_dispatch`), or run it directly on the box:

```
ssh bithabit ~/workspace/physical-spark-deploy.sh
```

## The CD pattern (shared across the cluster)

The box has **no in-cluster CD tool** (no Flux/Argo/Keel) and **no cron**.
Every service deploys the same way: a per-repo **GitHub Actions** workflow SSHes
into the server on push and triggers a `git pull`. There are two service shapes:

| Shape | Example | How a deploy applies |
| --- | --- | --- |
| **Static site** — nginx serves a git checkout via a `hostPath` mount | `static-web`, `llm-app-lab`, **physical-spark site** | `git pull` = live instantly; no image build, no pod restart |
| **Built service** — a container image in the local registry `localhost:5000` | `bithabit-api`, `pr-auth` | `docker build` → `docker push` → `kubectl rollout restart` |

`physical-spark` is a **hybrid**: a static site (`site/`, served by the
`physical-spark` Deployment) **plus** a built auth service (`auth/`, the
`pr-auth` Deployment). One script handles both.

## The pieces

### 1. `physical-spark-deploy.sh` (on the server, `~/workspace/`)

```bash
cd ~/workspace/physical-spark
git fetch origin -q && git reset --hard origin/main -q      # static site is now live
# only when auth/ changed since the last deploy:
docker build -t localhost:5000/pr-auth:latest auth/
docker push localhost:5000/pr-auth:latest
sudo -n k3s kubectl rollout restart deploy/pr-auth
```

`reset --hard` (not a merge) makes the checkout an exact mirror of `origin/main`
— a deploy target should never carry local drift.

### 2. `.github/workflows/deploy.yml` (this repo)

Runs on push to `main`. Loads the deploy key and SSHes to the box. The command
it sends is ignored — see the forced command below.

### 3. The forced-command deploy key

A dedicated `ed25519` keypair scoped to deploys only:

- **Private key** → GitHub repo secret `DEPLOY_KEY` (used by the workflow).
- **Public key** → the server's `~/.ssh/authorized_keys`, pinned so the key can
  *only* run the deploy script:

  ```
  restrict,command="/home/ubuntu/workspace/physical-spark-deploy.sh" ssh-ed25519 AAAA… physical-spark-ci-deploy
  ```

  `restrict` disables port/agent/X11 forwarding and PTY allocation. Even if the
  private key leaked, it can do nothing on the box except run this one deploy.

## Infra facts

- **Host:** `158.180.71.122` (SSH alias `bithabit`), single-node **k3s**,
  Traefik ingress.
- **DNS:** `*.bit-habit.com` is a wildcard → new subdomains resolve with no DNS
  change. **TLS:** wildcard `*.bit-habit.com` cert (`tls-secret`) covers them too.
- **k8s objects** (namespace `default`):
  - `deploy/physical-spark` + `svc/physical-spark-svc` — static site (nginx,
    hostPath `~/workspace/physical-spark/site`). Manifest: [`k8s/site.yaml`](../../k8s/site.yaml).
  - `deploy/pr-auth` + `svc/pr-auth-svc` — auth service. Manifests:
    [`auth/k8s/`](../../auth/k8s/). Auth data (SQLite) persists on hostPath
    `~/workspace/pr-auth-data`.
  - `ingress/physical-spark` — routes `/api/auth` + `/api/scores` → `pr-auth-svc`,
    everything else → `physical-spark-svc`. Same-origin so the auth cookie is
    first-party. Manifest: [`auth/k8s/ingress.yaml`](../../auth/k8s/ingress.yaml).

## Watching a deploy

`gh run watch` streams the run's step status live and refreshes until it finishes
(≈7s for a static-only change; longer when `auth/` rebuilds the image):

```console
$ gh run watch -R bookseal/physical-spark
✓ main Deploy to physical-spark.bit-habit.com · 29113072093
Triggered via workflow_dispatch less than a minute ago

JOBS
✓ deploy in 7s (ID 86429790717)
  ✓ Set up job
  ✓ Load deploy key
  ✓ Trigger server deploy
  ✓ Post Load deploy key
  ✓ Complete job
```

The step statuses (`✓`/`*`/`X`) update in place; add `--exit-status` to make the
command exit non-zero if the run fails (handy in scripts). If you didn't catch
it live, pass an explicit run id — grab the newest with
`gh run list --workflow deploy.yml --limit 1`.

To see **what the server actually did** — the deploy script's output — read the
log of the `Trigger server deploy` step (the forced command streams its stdout
back into the job):

```console
$ gh run view 29113072093 -R bookseal/physical-spark --log | grep "physical-spark updated"
… Trigger server deploy … physical-spark updated to 3a974eb at 2026-07-10T17:51:53Z
```

> Note: runs currently log a harmless warning that `webfactory/ssh-agent@v0.9.0`
> targets Node 20 (auto-run on Node 24). It doesn't affect the deploy; bump the
> action version when convenient.

## Runbook

**Rotate / revoke the deploy key**

```bash
# revoke: drop the pinned line from the server
ssh bithabit "sed -i '/physical-spark-ci-deploy/d' ~/.ssh/authorized_keys"
# rotate: regenerate, then re-add the public key + reset the GitHub secret
ssh-keygen -t ed25519 -f deploy_key -N '' -C physical-spark-ci-deploy
gh secret set DEPLOY_KEY -R bookseal/physical-spark < deploy_key
```

**Auth didn't update?** It only rebuilds when `auth/` changed; force it with
`ssh bithabit "cd ~/workspace/physical-spark && docker build -t localhost:5000/pr-auth:latest auth/ && docker push localhost:5000/pr-auth:latest && sudo -n k3s kubectl rollout restart deploy/pr-auth"`.
