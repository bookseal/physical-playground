# pr-auth — passwordless email magic-link auth (MVP)

Small FastAPI service that gives Physical Revolt accounts with **no passwords**: you enter your email,
get a one-time link, click it, and you're in (a random English nickname is minted on first sign-in).
Runs on the k3s cluster next to the static site, same-origin under `/api/auth/*`.

- `app.py` — the service (start / verify / me / logout).
- `nicknames.py` — random nickname generator (`brave-otter-42`).
- `k8s/` — Deployment, Service, and the `physical-revolt` Ingress with the `/api/auth` path added.

## Endpoints
| method | path | purpose |
|---|---|---|
| POST | `/api/auth/start` `{email}` | email a 15-min magic link |
| GET | `/api/auth/verify?token=` | validate, find-or-create user, set `pr_session` cookie |
| GET | `/api/auth/me` | `{email, nickname}` or 401 |
| POST | `/api/auth/logout` | clear session |

## Deploy (on the `bithabit` server)
```bash
cd ~/workspace/physical-revolt          # the cloned repo
# 1) build + push to the cluster's local registry
docker build -t localhost:5000/pr-auth:latest auth/
docker push localhost:5000/pr-auth:latest
# 2) apply manifests (Deployment + Service + updated Ingress)
sudo k3s kubectl apply -f auth/k8s/
sudo k3s kubectl rollout status deploy/pr-auth
```
If k3s can't pull `127.0.0.1:5000` yet, add `/etc/rancher/k3s/registries.yaml` (mirror for `127.0.0.1:5000`,
`insecure_skip_verify` for the local registry) and restart k3s — one-time.

## Email (reuse bithabit's setup) — founder-applied, Claude never sees the value
The service reads SMTP config from a secret named `pr-auth-email` (marked `optional` — until it exists the
service runs in **dev mode** and just prints the magic link to the pod log, so the flow is fully testable):
```bash
sudo k3s kubectl create secret generic pr-auth-email \
  --from-literal=SMTP_HOST=... --from-literal=SMTP_PORT=587 \
  --from-literal=SMTP_USER=... --from-literal=SMTP_PASS=... \
  --from-literal=SMTP_FROM='Physical Revolt <no-reply@bit-habit.com>'
sudo k3s kubectl rollout restart deploy/pr-auth
```
(Point these at whatever the existing habit-formation service already uses.)

## Security posture (MVP — review before real users)
Single-use tokens hashed at rest, 15-min TTL; httpOnly + Secure + SameSite=Lax cookie; per-email resend
cooldown; no account enumeration; no passwords stored. **Not yet:** CSRF tokens on logout, stronger rate
limiting/IP throttling, email deliverability hardening, Apple passkey, server-side course-progress sync.
