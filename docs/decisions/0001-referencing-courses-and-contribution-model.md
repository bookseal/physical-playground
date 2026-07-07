# ADR 0001 — Referencing open courses & the contribution model

> **Status:** accepted (2026-07-07) · **Type:** decision record (ADR)
> Short notes so these two calls don't get re-litigated later. Revisit triggers noted at the end.

---

## Context
We build tutorials/projects by referencing **NVIDIA Physical AI Learning** and **Hugging Face LeRobot**
courses. Two open questions came up: (1) how far can we legally lean on their material? (2) should we build a
GitHub-style "contributor edits + PR" feature — and is a build-but-don't-use feature ever worth it?

---

## Decision 1 — Referencing courses: **link + reframe + attribute** (split code vs content)

- **Code** (e.g. LeRobot = Apache-2.0): free to use, modify, redistribute, even commercially — **as long as we
  keep the license notice + attribution.** Model weights (e.g. NVIDIA GR00T / Isaac assets) carry their **own**
  licenses — **verify commercial-use terms before shipping them in a paid product.**
- **Content** (their tutorial prose, screenshots, videos): copyrighted by default. **Do not copy-paste.**
- **Operating rule:** link to the source, explain in our **own** words/examples, attribute. Never republish
  their text/media. (This is already how `lab/references/` works.)
- **How much to worry now:** at the learning-in-public / hobby stage, low risk if we follow the rule.
  Formalize at monetization: add a `CREDITS.md` (attribution list) and re-check model licenses for paid use.

## Decision 2 — Contribution model: **use GitHub's real PR flow; don't build our own**

- Community-edited curriculum fits the moat (accumulating community records). But we **do not build** a custom
  PR/edit system — we **use GitHub**: curriculum/tutorials live in the public repo → contributors fork → PR →
  we review/merge. Zero build, real workflow, and **contributor count becomes a pitchable traction metric.**
- **Build custom only for what GitHub can't give:** the **solution peer-review** (video runs + likes gallery).
  That's the differentiator; reserve engineering there.
- **Build-but-don't-use features are a trap** (maintenance + hollow). The one exception is a **pitch demo** —
  a clickable mock of the vision — but it must be **labeled** ("coming soon" / "illustrative"), never faked as
  live. (See the landing page roadmap + illustrative leaderboard.)

---

## Consequences
- Curriculum/tutorials are authored as original, attributed, link-heavy docs — safe to make public.
- Engineering effort concentrates on the solution-gallery/peer-review product, not infra GitHub already provides.
- Public demos stay honest via explicit labels.

## Revisit when
- We start **charging** (→ do the `CREDITS.md` + model-license audit; confirm GR00T-in-paid-product terms).
- GitHub's PR flow becomes a real friction for non-technical contributors (→ reconsider a lightweight custom editor).
