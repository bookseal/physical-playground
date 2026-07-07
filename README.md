# Physical Playground

*(working name — this may change)*

A peer-review school for **Physical AI**, made for kids.

We give a student a robot-arm mission. They build it, they solve it, and
they upload a short video of the result. Then students review each other's
work. The solutions that get the most likes rise to the top of the gallery.

The idea mixes two things:

- The **peer-review** learning model of École 42 — students learn by
  reviewing each other's work, not by listening to a teacher.
- Korean **playground games** — the same kind of games you saw in *Squid Game*.

## The missions

We start very easy, so even an elementary-school kid can finish mission 1.

1. **"Pat me on the back"** — Build the robot arm and make it gently pat your
   back, left and right. (Goal: a warm first win, with a low bar for success.)
2. **Pick & place** — Grab an object and move it. A ladder of small steps that
   slowly get harder.
3. **"Red Light, Green Light"** (무궁화꽃이 피었습니다) — The robot moves while
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

## Status

Early work in progress. We are building in public. Week 1: choosing and
ordering the first robot arm.

---

Built by [bookseal](https://github.com/bookseal).
