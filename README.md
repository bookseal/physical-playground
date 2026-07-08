# Physical Revolt

*(product name; the repo keeps its original `physical-playground` name)*

A peer-review school for **Physical AI** — **a revolt against boring tutorials**, for developers who want to break into robotics.

We give a student a robot-arm mission. They build it, they solve it, and
they upload a short video of the result. Then students review each other's
work. The solutions that get the most likes rise to the top of the gallery.

![Physical Playground — landing page](assets/screenshot-landing.png)

The idea mixes two things:

- The **peer-review** learning model of École 42 — students learn by
  reviewing each other's work, not by listening to a teacher.
- **Playground games** — the kind of simple games you saw in *Squid Game*.

## The missions

We start very easy — your first win comes fast, even if you've never touched a robot.

1. **"Pat me on the back"** — Build the robot arm and make it gently pat your
   back, left and right. (Goal: a warm first win, with a low bar for success.)
2. **Pick & place** — Grab an object and move it. A ladder of small steps that
   slowly get harder.
3. **"Red Light, Green Light"** — The robot moves while
   you speak, and stops the moment you stop talking. Voice input, end-of-speech
   detection, background noise, and many languages make this an open problem —
   which is exactly why peer review matters here.

## Why this is different

This is not a textbook. It is a **learning operating system**.

Content is easy to copy. A community and its records are not. The real product
is the peer review, the video gallery made by the users, and the data that
builds up over time.

## Tech direction

- **Hardware:** low-cost, open-source robot arms (SO-101 class).
- **Software:** the Hugging Face **LeRobot** ecosystem.
- **Platform (the part we build):** post a mission → upload a solution video →
  peer review → a "most-liked" gallery.

## Notes (building in public)

- [Product concept](docs/01-concept/product-concept.md) — the missions, and why "textbook vs. platform" is the fork in the road.
- [Market landscape](docs/02-market/market-landscape.md) — US & China scan: HF/LeRobot, NVIDIA, Makeblock, DJI, and the gaps.
- [Positioning & pitch](docs/03-positioning/positioning-and-pitch.md) — value proposition, a glossary for developers, and the pitch.

## Hands-on lab (learning in public)

- [Simulation setup — up to just before "pat me"](lab/tutorials/00_sim-setup-before-pat-me.md) — get a Physical AI dev environment running in sim (Mac path + NVIDIA Isaac path).
- [Tutorial reference collection](lab/references/index.md) — curated NVIDIA / Hugging Face LeRobot tutorials, with hardware/OS requirements.

## The project, run as a system

This isn't just a repo of docs — it's run like an operating system for the venture. A local
**Playbook** dashboard turns every product/market/strategy note, hands-on lab, and design decision
into a browsable, searchable board (built with zero dependencies — a tiny Python server + one HTML file).
Decisions are logged as [ADRs](decisions/), the public/private boundary is enforced by structure, and the
whole thing doubles as a build-in-public trail.

![Physical Playground — Playbook dashboard](assets/screenshot-playbook.png)

## The thinking (building in public)

I'm *new* to Physical AI. But being new doesn't mean being shallow — I go deep on the "why," and I try
really hard to make the learning **fun**. This repo keeps the trail of that thinking, on purpose:

- **[Design theme](design/design-theme.md)** — why the whole thing borrows the *feeling* of the 1999 RC-racing
  game **Re-Volt** (toy-scale wonder), and how that becomes a color/type/motif system.
- **[Decision records (ADRs)](decisions/)** — the calls I didn't want to re-litigate later: how to reference
  open courses, how to handle public vs. private, etc. Each one logs the *context* and the *why*.
- **[Foundations map](knowledge/00-foundations.md)** — the "two worlds" (classical ROS vs. learning-based
  Physical AI) I had to draw for myself before any course made sense.
- **[Industry & job-market notes](knowledge/)** — where the money and the jobs actually are.

The bet: *how* someone learns to build should itself be built with care and joy. This whole workspace is that,
run as a system.

## Status

Early work in progress. We are building in public. Week 1: choosing and
ordering the first robot arm.

---

Built by [bookseal](https://github.com/bookseal) · portfolio: [bit-habit.com](https://bit-habit.com)
