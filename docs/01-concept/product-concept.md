# Product Concept — "Pat me on the back" → "Red Light, Green Light"

> Building-in-public notes for **Physical Spark** — a peer-review school for Physical AI.
> Premise: **client #1 is us.** We buy a low-cost robot arm, assemble it ourselves, and turn
> the act of learning into the product itself.

---

## 1. Core idea — an "École 42-style peer-review school for Physical AI"

Like École 42:
- **No instructor.** We hand out a reasonable project as an **assignment**.
- An online system where learners **peer-review** how each other solved it.
- Everyone rates each other, and the **most-liked solution videos rise to the top.**
- Difficulty starts **low enough that an elementary-school kid can finish mission 1** — the "42"
  of Physical AI, with a YouTube-style UGC layer on top.

**What makes it different:** the big open-source players (Hugging Face, NVIDIA) give you *content*
(courses) but **no evaluation or community system.** Closed K-12 kits give you *hardware* but a
sealed curriculum. We build the **operating system — "assignment + peer evaluation + video
gallery"** — the structure you actually learn by doing.

## 2. The mission sequence

### Mission 1 — "Pat me on the back"
- **Assemble** the robot arm → make it **pat your back** (a simple left-right sweep counts as success).
- Design intent: the first mission is about **attachment, not skill** — the robot you built comforts
  you. The bar for success is deliberately tiny, which is what drives completion rate.

### Mission 2 — Pick → place
- A difficulty ladder: release something already held → pick an object at a set position → rotate 180°
  and place it elsewhere.
- Design intent: pick & place is the "Hello World" of manipulation. Slice the steps small enough that
  everyone succeeds at their own level.

### Mission 3 — "Red Light, Green Light" ⭐
- The robot moves **while you say the phrase**, and **stops the instant you stop talking.**
- Open variations (the creative space):
  - how, and how accurately, to do speech recognition (in any language)
  - how fast you detect **end-of-speech** (minimizing latency = a real engineering problem)
  - background noise and speaker separation
  - an English version ("Red Light, Green Light"), speed changes, fake-outs…
- Design intent: listening + judgment + motor control fuse into one task — **the definition of Physical
  AI itself**, taught as a game even a child knows. There is no single right answer, which is exactly
  what makes peer review meaningful.

### Why this sequence works
1. **"Red Light, Green Light" is a top-tier demo:** a game the whole world already knows (thanks to
   *Squid Game*), understandable in 3 seconds on stage. A robot playing it is hard to forget.
2. The curve from mission 1→3 is pedagogically sound: attachment (emotion) → fundamentals (a win) →
   open problem (creativity + competition). The likes gallery explodes at mission 3.
3. The tech stack lines up exactly with what's already free/cheap: SO-101-class low-cost arms +
   LeRobot / speech APIs — all open-source or low-cost.

## 3. Textbook vs. platform — this is the fork in the road

- **Sell it as a textbook (content):** it gets copied. You compete with free YouTube lectures. That is
  the "feels like a cram-school workbook" trap.
- **Sell it as a platform:** the product is not the curriculum but **① the peer-evaluation system
  ② the likes gallery (UGC) ③ the data that accumulates** (who posted which solution, and what makes a
  good one). Copying the content doesn't help a competitor — the people and the records pile up on our
  side. Just as **École 42's value is its evaluation system, not its curriculum.**
- Conclusion: define the company as **"the operating system for learning Physical AI,"** not "a company
  that sells a workbook." Network effects (more learners → more solutions → more value) and an
  accumulating asset are what make it more than content.

> Note on investment: at this stage the goal is **not** raising money. It's to learn Physical AI in
> public, leave a trace, and build real numbers (completion rate, re-participation) first.

## 4. Revenue ladder (designed to run without outside money)

1. **Cohort fee + a retention mechanic:** time-boxed cohorts (4–6 weeks) with a deposit/forfeit
   structure (miss your weekly check-ins and it's deducted) — reusing a retention device we already
   validated over two years on a prior habit-tracking product (~90% retention). Marginal cost
   approaches zero online.
2. **Kit-bundle margin:** group-buy / bundle the robot arms (à la the Makeblock price ladder).
3. **(Later) B2B licensing:** sell the whole "assignment + evaluation system" to schools/academies —
   the operating system, not the workbook.

## 5. Six-week execution frame (goal: learning + a public trace + traction)

- **Week 1:** order the robot arm (compare SO-101-class candidates — Amazon vs. AliExpress on
  price/shipping) + start recording the unboxing/assembly.
- **Weeks 2–3:** do mission 1 ("pat me") ourselves — log every place we got stuck (that log *is* the
  first draft of the curriculum).
- **Weeks 3–4:** prototype mission 3 ("Red Light, Green Light").
- **Weeks 5–6:** turn it into pitch material — a demo video + a one-pager for the "42-style peer-review
  platform" vision.
- **Every week:** publish the learning log as content (blog / YouTube) — client #1's journey is the
  first marketing.

---

## 관련 (Related)
- [[market-landscape|시장 스캔]]
- [[positioning-and-pitch|포지셔닝 & 피치]]
- [[hate-map|Hate Map]]
