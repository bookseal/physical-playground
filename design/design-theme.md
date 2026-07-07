# Design Theme — the Re-Volt Playground

> Design **thinking** for the landing page + the real service pages. This file holds the *decisions and the
> system* (the "why"); the living *pixels* live in [`site/index.html`](../site/index.html). Mood is shown
> with original inline SVG below; Re-Volt screenshots are linked (not embedded) for copyright reasons.

---

## 0. North Star — "a small maker in a big world"

The feeling we're borrowing from **[Re-Volt (1999)](https://en.wikipedia.org/wiki/Re-Volt)**: a tiny,
**plasticky RC toy** zipping through an *oversized real world* — a toy shop, a supermarket, a museum, a
suburban street ([Re-Volt Wiki: Toy World](https://revolt.fandom.com/wiki/Toy_World_1)). Bright, lightweight,
"realism + cartoonish chaos," and deeply nostalgic — a cult favorite 27 years on
([Top Gear](https://www.topgear.com/car-news/gaming/absolutely-nailed-it-1999-videogame-perfected-rc-racing-formula)).

**The translation:** our learner is that RC toy, and **Physical AI is the giant playground.** A robot arm is
a toy you drive through a world that's bigger than you — and the site should feel like the *start screen and
level-select of a beloved toy-racing game*, not an enterprise dashboard.

> One-line brief: **Nostalgic toy-arcade energy, modern web legibility. Plastic and bright — never cheap.**

---

## 1. Principles (the guardrails)

1. **Toy-scale wonder, not childishness.** The *scale trick* (you're small, the world is big) creates wonder;
   cartoon-primary-color overload creates a toy for 5-year-olds. We want the former. Our customer is a developer.
2. **Everything is a "level."** Missions, tutorials, pricing tiers — framed as tracks/levels you unlock.
3. **Playful chrome, serious core.** Retro flourishes live in *navigation, empty states, buttons, transitions*.
   The actual content (code, docs, video) stays clean and high-contrast.
4. **Motion = a lightweight toy.** Small, springy, low-latency micro-animations (hover pops, a car easing).
   Never heavy or slow — the toy is *zippy*.
5. **Legibility wins every tie.** Nostalgia never costs contrast or readability. Retro *flavor*, modern *UX*.

---

## 2. Palette — "RC plastic on asphalt"

Track/asphalt as the base; bright molded-plastic toy colors as accents. (Reconciles with the current landing.)

<svg width="100%" viewBox="0 0 720 96" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Palette">
  <g font-family="monospace" font-size="11" fill="#fff" text-anchor="middle">
    <rect x="0"   y="0" width="120" height="66" fill="#0c0e14"/><text x="60"  y="86" fill="#888">#0c0e14 track</text>
    <rect x="120" y="0" width="120" height="66" fill="#39e0c8"/><text x="180" y="86" fill="#888">#39e0c8 teal</text>
    <rect x="240" y="0" width="120" height="66" fill="#ff5d8f"/><text x="300" y="86" fill="#888">#ff5d8f pink</text>
    <rect x="360" y="0" width="120" height="66" fill="#ffcf4d"/><text x="420" y="86" fill="#888">#ffcf4d gold</text>
    <rect x="480" y="0" width="120" height="66" fill="#2ec4ff"/><text x="540" y="86" fill="#888">#2ec4ff blue</text>
    <rect x="600" y="0" width="120" height="66" fill="#35e08a"/><text x="660" y="86" fill="#888">#35e08a green</text>
  </g>
</svg>

- **Track `#0c0e14`** — the dark asphalt base (dominant surface). Light mode = `#f6f7fb` (pale garage floor).
- **Teal `#39e0c8`** — primary action / "GO". **Pink `#ff5d8f`** — secondary / accent / "hot" state.
- **Gold `#ffcf4d`** — rewards, stars, best-lap, likes. **Blue/Green** — category tags (mission types).
- **Rule:** one accent leads per screen; the rest support. Toy colors are *seasoning*, asphalt is the *meal*.

---

## 3. Type & texture

- **Display / wordmark:** heavy, condensed, uppercase — an *arcade cabinet* feel. System stack:
  `ui-monospace` for HUD/labels + a bold sans (system) for headlines. (No pixel webfont — keep it self-hosted/system for speed; imply retro via weight, spacing, ALL-CAPS, not a novelty font.)
- **Body:** clean modern sans, generous line-height. This is where legibility wins.
- **Texture (sparingly):** subtle perspective grid (the "track"), soft plastic gloss on primary buttons
  (highlight + hard drop shadow = molded-plastic depth), rounded-but-chunky corners.

<svg width="100%" viewBox="0 0 720 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Perspective track grid">
  <defs><linearGradient id="fade" x1="0" y1="1" x2="0" y2="0">
    <stop offset="0" stop-color="#39e0c8" stop-opacity=".5"/><stop offset="1" stop-color="#39e0c8" stop-opacity="0"/></linearGradient></defs>
  <g stroke="url(#fade)" stroke-width="1.2">
    <line x1="0" y1="120" x2="300" y2="0"/><line x1="120" y1="120" x2="330" y2="0"/><line x1="240" y1="120" x2="360" y2="0"/>
    <line x1="360" y1="120" x2="360" y2="0"/><line x1="480" y1="120" x2="390" y2="0"/><line x1="600" y1="120" x2="420" y2="0"/><line x1="720" y1="120" x2="450" y2="0"/>
    <line x1="0" y1="120" x2="720" y2="120"/><line x1="60" y1="80" x2="660" y2="80"/><line x1="150" y1="45" x2="570" y2="45"/><line x1="210" y1="22" x2="510" y2="22"/>
  </g>
</svg>

---

## 4. Motifs (the Re-Volt vocabulary)

- **The track grid** — perspective floor = "the world you drive through." (Already the landing hero.)
- **Level-select map** — pages linked like a toy-racing level map; missions are *tracks*.
- **HUD** — lap/checkpoint/best-time framing for progress, streaks, likes ("BEST LAP" = top-liked run).
- **Toy-scale props** — occasional oversized everyday object as a wink (a giant keyboard key, a die, a plant),
  echoing Re-Volt's Toy World set pieces. Use as decoration, never as noise.
- **Garage / pit** — the "your stuff" area (login, profile, saved runs) = your garage.

<svg width="100%" viewBox="0 0 720 90" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Level map">
  <g stroke="#ff5d8f" stroke-width="2" stroke-dasharray="6 6" fill="none"><path d="M40 70 C 160 20, 260 20, 360 55 S 560 90, 680 30"/></g>
  <g font-family="monospace" font-size="11" text-anchor="middle">
    <circle cx="40"  cy="70" r="14" fill="#39e0c8"/><text x="40"  y="74" fill="#04120f">1</text><text x="40"  y="20" fill="#888">Pat me</text>
    <circle cx="360" cy="55" r="14" fill="#2ec4ff"/><text x="360" y="59" fill="#04120f">2</text><text x="360" y="88" fill="#888">Pick&amp;place</text>
    <circle cx="680" cy="30" r="14" fill="#ffcf4d"/><text x="680" y="34" fill="#04120f">3</text><text x="680" y="80" fill="#888">Red Light</text>
  </g>
</svg>

---

## 5. Page-by-page application

| Page | Re-Volt metaphor | Notes |
|---|---|---|
| **Landing** | Start screen + level select | "PRESS START", hero track, 3 missions as levels. (Done in v1.) |
| **Tutorials / lab** | Track / time trial | Each tutorial = a track; progress bar = lap; "ghost" = a peer's run to follow. |
| **Solution gallery** | Leaderboard | Most-liked = pole position; "BEST LAP" ribbon on the top run. |
| **Login / profile** | Your garage / pit | "Enter the garage." Saved runs = your cars. |
| **Pricing / cohorts** | Unlock tracks / coins | Tiers as "unlock the full circuit"; deposit-refund = "entry token." |
| **Dashboard (Playbook)** | Map screen | Where you pick where to go next. (The viewer already leans this way.) |

---

## 6. Traps to avoid
- **Nostalgia tax on usability** — retro must never hurt contrast, tap targets, or load time. Test both themes.
- **Theme-park everything** — if *every* element is a gag, nothing reads. 80% calm, 20% playful.
- **Copyright** — evoke the *feeling*, don't copy Re-Volt's art/logos/assets. Our motifs are original.
- **Accessibility** — motion respects `prefers-reduced-motion`; color is never the only signal.

## 7. Next steps
1. Lock the palette + type tokens as CSS variables (partly done in `site/index.html`).
2. Prototype **one service page** (e.g., the gallery leaderboard) in HTML to test the theme beyond the landing.
3. Commission/draw 2–3 original toy-prop illustrations (SVG) for hero + empty states.
4. Gut-check with target developers: does it read "fun + credible," or "toy for kids"? Adjust the 80/20.

## Reference imagery (external — look, don't copy)
- [Re-Volt — Wikipedia](https://en.wikipedia.org/wiki/Re-Volt) · [Toy World level (Wiki)](https://revolt.fandom.com/wiki/Toy_World_1)
- [MobyGames screenshots](https://www.mobygames.com/game/369/re-volt/) · [Top Gear retrospective](https://www.topgear.com/car-news/gaming/absolutely-nailed-it-1999-videogame-perfected-rc-racing-formula)
- [Re-Volt community (still alive)](https://re-volt.io/) — the cult following is itself a brand lesson.
