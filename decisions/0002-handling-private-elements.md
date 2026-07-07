# ADR 0002 — Handling private elements (public/private boundary)

> **Status:** proposed (2026-07-07) — *decision pending; pick an option below.* · **Type:** decision record
> Supersedes the ad-hoc split done in-session (two sibling repos). Related: [ADR 0001](0001-referencing-courses-and-contribution-model.md).

---

## Context
The project mixes **public** material (product concept, market, positioning, labs, design, the viewer/landing code)
and **private** material (personal context, mentor research — anonymized as "Gemini", raw drafts, funding strategy).

Current state (set up mid-session): private content was moved out of the working directory into a **separate
sibling git repo** `../physical-playground-private/` (local-only, never pushed). Plus defense-in-depth:
`.gitignore` structure, a gitleaks pre-commit hook, and the mentor identity fully anonymized.

This is **maximally secure but operationally confusing**:
- Two working directories for one project.
- Claude/tools can *reach* the private repo by absolute path (it did — the anonymization happened there) but it
  is **not auto-loaded** into context and won't show up in working-dir searches. So private knowledge is only
  used when explicitly opened.

**The real question:** what's the right long-term structure? Industry practice depends on *what* is private —
and here it's mostly **documents/PII**, not code/secrets.

## Options

| # | Option | How | Confusion | Fit |
|---|---|---|---|---|
| 1 | **Docs out of git** | Private *documents* live in Notion/Drive (already connected); secrets in a manager; repo stays code + public docs | low | ★★★ industry norm for PII/docs |
| 2 | **Private source → public export** | Work in ONE private repo (full context); a script/CI publishes only public folders to the public repo | low | ★★★ one place to work, security kept |
| 3 | **Git submodule** | Public repo embeds the private repo at `private/` (only a pointer is public) | high | ★ physically reunited but submodules are fiddly |
| 4 | **Two sibling repos (current)** | Keep as-is | medium | secure, but the confusion above |

## Decision
**TBD** — choose one. (This ADR stays `proposed` until then, then flips to `accepted` and names the choice.)

## Recommendation
Because the private material is mostly **documents**, not code:
- If the founder prefers working in files/git with Claude → **Option 2** (private is the source of truth; public
  is a filtered export). Fixes the "Claude can't auto-see private" friction *and* keeps security.
- If the founder wants private notes out of git entirely → **Option 1** (mentor/strategy → Notion/Drive).
- Lowest-effort fallback → **Option 4** kept, plus a working convention: Claude explicitly opens
  `../physical-playground-private/` whenever mentor/strategy is relevant.

## Consequences (by option)
- **1:** cleanest repo; context now spans git + Notion. Need a Notion home + a pointer from `CLAUDE.md`.
- **2:** one full working dir (best for Claude); adds a publish step; public repo becomes a derived mirror.
- **3:** one working tree; submodule ceremony (`git submodule update`, pointer commits); private repo URL is exposed.
- **4:** no change; ongoing two-dir friction; rely on discipline.

## Revisit when
- A cofounder/teammate joins (→ they need a clear, low-friction boundary — favors 1 or 2).
- The private set grows to include real secrets/keys (→ add a secrets manager regardless).
