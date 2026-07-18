# Physical AI in Korea — a strategy playbook for a non-engineering founder

> **What this is.** A candid strategy note for Physical Spark: how to win **without a
> mechanical/robotics engineering base**, whether pitching **Plug and Play** makes
> sense, and how to actually get ahead in **Physical AI in Korea**. It combines a
> mentor's field advice with **cross-verified external research** — where the two
> disagree, the sourced evidence wins and the note says so.
>
> Sourcing: mentor input is a Seattle-based immigrant founder's view, kept generic on
> purpose. Everything load-bearing is checked against a primary or reputable source,
> linked inline. Research window: **2026-07**. Treat fast-moving numbers as "verify
> before you spend money."

---

## TL;DR (bottom line up front)

The strongest evidence-backed version of the plan:

> **Physical Spark is a peer-review school whose *real product* is a vetted talent pool
> plus a teleoperation/behavior-data flywheel — feeding Korea's under-served SME robot
> systems-integration (SI) layer. You run the software/orchestration side; a robotics
> co-founder (whom the school itself recruits) owns hardware. Fund it with government
> deep-tech grants + a domestic accelerator → TIPS, use CES for credibility, and steer
> relentlessly toward deployment metrics — not award-collecting.**

Three specific course-corrections the research forces on the mentor's advice:

1. Keep the **demographic / skills-gap** framing; **drop "replace migrant labor"** (Korea *cut* the foreign-worker quota ~40% for 2026).
2. **Don't pitch Plug and Play now** — wrong shape, and its Korea office is fintech/smart-city.
3. **Never present this as a solo non-technical hardware bet** — that's the single biggest fundraising red flag; a robotics co-founder is non-optional.

---

## 1. The core question — winning without an engineering base

The honest starting point: the founder is a ~4-yr **AI product engineer** (École 42 Seoul; strong in LLM/agents/infra), **not** a mechanical or robotics engineer. Can that win in Physical AI?

**Yes — but only on a specific layer, and not alone.**

- **The AI-generalist / orchestrator thesis is real, with a ceiling.** Solo-founded ventures are now ~36% of new starts, and one operator can now run team-scale *software* via agent orchestration. But every serious source flags the ceiling explicitly: solo + AI carries **software**, not physical deployment, safety, hardware ops. ([Fortune, 2026-05](https://fortune.com/2026/05/18/solo-founders-ai-automation-entire-teams-entrepreneurs/); ["Solo Founder Ceiling," Foundra 2026-05](https://www.foundra.ai/key-reads/solo-founder-ceiling-ai-stack-hire-first-may-2026-fortune)) The founder's profile fits **orchestrating robotics *software***, not building robot mechanics.
- **Stay on the software / policy / deployment layer, on COTS hardware.** Industry guidance is blunt: a **software-first play on commodity hardware (SO-101 / LeRobot)** is "faster, cheaper, and the right approach for most application-layer robotics startups," and **the training dataset is more defensible than the model or the code**. ([Silicon Valley Robotics startup guide, 2026](https://www.roboticscenter.ai/blog/robot-startup-guide)) This is *already* the curriculum's stance — it deliberately cuts ROS/embedded/LiDAR/5-finger hands to teach the learning-policy layer ([`curriculum-vision.md`](../01-concept/curriculum-vision.md), [`04-arm-hand-eye.md`](../../knowledge/04-arm-hand-eye.md)).
- **A robotics / ME co-founder is non-optional.** The same sources call a **solo non-technical robotics founder a fundraising red flag**, and say "robotics companies fail when the team lacks either hardware or software depth." ([SVRC](https://www.roboticscenter.ai/blog/robot-startup-guide)) The winning move: **the school is the recruiting funnel** — you meet the strongest robotics builder in Korea by teaching hundreds of them.
- **TIPS is designed for exactly your gap.** You don't need a hardware pedigree yourself if a **deep-tech operator (accelerator/VC) invests first and vouches for you** — that's the whole TIPS mechanism (§3). The operator supplies the technical credibility a grant panel wants.

> **Mental reframe:** you're not "a non-engineer trying to do robotics." You're the **AI-orchestration + go-to-market + community** half of a robotics team, assembling the other half through the school. That is a fundable shape; a solo hardware claim is not.

---

## 2. Plug and Play — go / no-go

**Verdict: no, not now.** Two different things share the name "Plug and Play," so separate them:

**(a) The mentor's "Plug and Play" *mental model* — keep it.** "Put your idea into an accelerator/competitor pool, benchmark yourself, find where you actually rank, learn everyone else's pain." That's good discipline and matches the repo's own [positioning work](../03-positioning/positioning-and-pitch.md). Do it.

**(b) The real Plug and Play Tech Center accelerator — wrong door for now.**

| | Reality |
|---|---|
| What it is | **Corporate-innovation matchmaker**, not a seed fund — it sells startups access to 500+ corporates for **pilots/POCs**, across 25+ verticals. ([PnP accelerator](https://www.plugandplaytechcenter.com/innovation-services/startups/accelerator-programs)) |
| Terms | Accelerator is **equity-free / fee-free** (the product is corporate access, not capital). ([PnP](https://www.plugandplaytechcenter.com/innovation-services/startups/accelerator-programs)) |
| Selects for | A **deployable product a corporate can pilot now**, mapped to a partner's problem. |
| **Korea office** | Scoped to **fintech / insurtech and smart-city / mobility** — *not* edtech, *not* robotics education. Partners: KB, Shinhan, POSCO, LG, Hanwha, CJ. ([PnP Korea launch, 2021](https://www.prnewswire.com/news-releases/plug-and-play-korea-launches-in-seoul-301277348.html); [PnP Korea](https://www.plugandplaykorea.com/)) |
| Fit for Physical Spark today | **Low.** Pre-revenue, education/community, solo non-engineer — fails all three of PnP's filters, in the wrong Korean vertical. |

**Revisit PnP only later**, once there's a B2B "Physical AI workforce reskilling" product a large manufacturer/mobility corporate could pilot. That's a 2–3-year-out corporate-matchmaking play, not a now pitch.

---

## 3. The real funding ladder (Korea)

Money for this profile exists — it's just **not** at PnP. In order:

1. **예비창업패키지 — 딥테크 트랙 (로봇/AI).** Pre-startup grant, **~₩50M**, for people *not yet incorporated*. Deep-tech track explicitly includes **로봇 and AI**, and eligibility is **background-agnostic (no degree/major restriction)**. This is the best-fit **first, non-dilutive** move. ([MSS 공고](https://www.mss.go.kr/site/smba/ex/bbs/View.do?cbIdx=310&bcIdx=1060210&parentSeq=1060210); [KISED](https://www.kised.or.kr/menu.es?mid=a10205010000))
2. **초기창업패키지 — 딥테크** (within 3 yrs of incorporation, avg ~₩70M) as step two. ([bizinfo](https://www.bizinfo.go.kr/web/lay1/bbs/S1T122C128/AS/74/view.do?pblancId=PBLN_000000000112196))
3. **A domestic deep-tech accelerator** — which then becomes your **TIPS operator**:
   - **블루포인트파트너스** — Korea's flagship deep-tech AC (392+ portfolio, robotics-heavy, TIPS operator). Best target for the *deep-tech* framing. ([THE VC](https://thevc.kr/bluepointpartners))
   - **퓨처플레이** — deep-tech "company builder," actively invests in robotics, supplies technical rigor a non-engineer lacks. ([FuturePlay](https://fpco-dev.futureplay.co/investment))
   - Edtech-fit seed: **매쉬업엔젤스** (explicit edtech thesis) ([Mashup](https://www.mashupventures.co/contents/5-tips-for-startup-support-programs)), **프라이머** (founder-driven generalist), **스파크랩** (edtech precedent, demo day).
4. **TIPS — deep-tech track:** operator invests ≥₩300M, government matches **R&D up to ~₩1.5B**. This is how you get real money **without a personal hardware pedigree** — the operator underwrites you. ([TIPS](https://www.jointips.or.kr/); [Kakao Ventures TIPS guide](https://www.kakao.vc/blog/TIPS-eligibility-2025))
5. **Stretch, in parallel: Y Combinator.** Genuinely solo-founder-friendly (W26 ~11% solo) and at its most hardware/edu-friendly ever; **$500K standard deal**; weights founder + rate-of-progress over pedigree. The one that most rewards the "42-style peer-learning + LeRobot" story. ([YC deal](https://www.ycombinator.com/deal); [Apply](https://www.ycombinator.com/apply))

> **Framing tip — you have two decks, don't blend them.** *Edtech/community* ("42-style peer-review robotics school") opens Mashup/Primer/SparkLabs/YC and AI-upskilling programs, and your non-engineer profile is an *asset* there. *Physical-AI deep-tech* ("operator-training + manipulation-data pipeline") opens 블루포인트/퓨처플레이/TIPS and the 딥테크 로봇/AI grants. **Recommended umbrella: a "Physical AI talent pipeline"** that produces both a scarce operator workforce *and* real LeRobot manipulation data — it qualifies for the deep-tech grants now and still tells a clean edtech story.

---

## 4. Leading Physical AI in Korea — cross-verified strategy

### The landscape (2026)

- **Physical AI is now explicit national strategy** — Phase 1 (Sept 2025), **Phase 2 (2026-06-19)**: a "K-Physical AI full stack," goal to lead the world in physical AI. ([Seoul Economic Daily, 2026-06-19](https://en.sedaily.com/technology/2026/06/19/korea-targets-top-spot-in-physical-ai-aims-to-cut-foreign)) The **K-Humanoid Alliance** targets humanoid leadership by 2030. ([Korea.net](https://www.korea.net/NewsFocus/Sci-Tech/view?articleId=269677))
- **Government names *behavior data* as the national bottleneck** — not chips, not models — and is building behavior-data training centers on **teleoperation + digital-twin** tracks. ([The Elec, 2026](https://www.thelec.net/news/articleView.html?idxno=11898)) *This is directly your cohorts' output.*
- **Direct comparators (teaching):** **동국대 DAPIER** — Korea's first Physical-AI-specific KDT bootcamp (656h, ROS2 + Isaac + MuJoCo, **capstone on LeRobot SO-101**, free/government-funded, hardware provided). ([DAPIER](https://semibootcamp.dongguk.edu/)) Plus Doosan ROKEY, 패스트캠퍼스 robotics KDT. **You cannot out-subsidize a free, hardware-provided government bootcamp** — so don't compete on curriculum/price.
- **The real gap for a small player:** the **robot SI layer is huge and starved** — ~20,000 SI firms, **98.7% SMEs, ~63.7% under ₩1B revenue**, and demand-side SMEs "can't find suitable providers." Experts prescribe **standardized, industry-specific, modular** solutions. ([irobotnews](https://www.irobotnews.com/news/articleView.html?idxno=44101); [HelloT SI 진단](https://www.hellot.net/news/article.html?no=112879))

### The mentor's five claims, cross-checked

| Claim | Verdict | Why (source) |
|---|---|---|
| "Physical AI = replace migrant labor" | **Oversimplified** | Real driver is demographic/skills-gap, but Korea **cut the E-9 quota ~40% to 80,000 for 2026** and extended stays — not 1-for-1 substitution. Keep the demographic framing; drop "replace migrants." ([Korea Herald, 2025-12](https://www.koreaherald.com/article/10641758)) |
| "3-way edge: small factories / can't use Chinese systems / need custom robots" | **Mixed** | Small varied factories + customization demand **hold up** ([SI data](https://www.hellot.net/news/article.html?no=112879)). "Can't use Chinese systems" is **wrong for Korea** — that's *US* policy; Korea has no ban and **Neubility just partnered with Unitree**. Reframe as **data-sovereignty / a coming security-procurement wedge**. ([Sedaily, 2026-06-26](https://en.sedaily.com/technology/2026/06/26/neubility-partners-with-unitree-to-co-develop-robot); [IEEE Spectrum](https://spectrum.ieee.org/chinese-robots-us-ban)) |
| "Non-engineer wins via deployment/customization, not hardware" | **Holds up** | Software-first on COTS is the recommended path; **dataset > model > code** for defensibility. Caveat: not *solo*. ([SVRC](https://www.roboticscenter.ai/blog/robot-startup-guide)) |
| "Get rich selling the tech/company, not the product; VCs won't fund a sales play" | **Half-true** | Exit-heavy market (**995 acquisitions vs 62 IPOs, 2025**) supports "sell the company" ([SG Analytics](https://www.sganalytics.com/blog/vc-based-companies-are-driving-mergers-and-acquisitions/)), but VCs *do* fund **recurring/usage-based** revenue (RaaS). Productize deployment; don't do bespoke consulting. |
| "Grants + a CES award unlock more money (상장 > 매출)" | **Directionally holds** | Government money is central (**MSS ₩3.46T** 2026 budget) and **Korea took ~60% of CES 2026 Innovation Awards** ([KoreaTechDesk / barchart](https://www.barchart.com/story/news/36830561/korean-startups-step-into-the-next-stage-at-ces-2026)). But CES is a **wedge, not a business model**, and policy is tilting toward traction — an award-only, no-revenue play is increasingly fragile. |

### The wedge — what Physical Spark actually sells

Not curriculum (free DAPIER wins that). Your defensible assets:

1. **A vetted talent pool** the fragmented 20,000-firm SI market desperately needs — peer-review + completion data is the vetting signal. Cohort courses hit **40–70% completion vs 5–15% for MOOCs**; the durable value is "**sell the outcome/completion, not the content**." ([Forte Labs on cohort courses](https://fortelabs.com/blog/the-rise-of-cohort-based-courses/))
2. **A behavior-data flywheel** — cohorts collect **teleoperation demonstrations on SO-101**, which is *more defensible than model or code* and maps straight onto the government-declared national bottleneck (a fundable wedge + a partnership hook with the K-Humanoid / behavior-data-center program). ([SVRC](https://www.roboticscenter.ai/blog/robot-startup-guide); [The Elec](https://www.thelec.net/news/articleView.html?idxno=11898))
3. **The government B2B channel** you already scoped in [`funding.html`](../../site/funding.html): supply the curriculum to *offline* KDT bootcamps and teach as a K-디지털 교·강사 — the government arm, run in parallel to the direct online product.

---

## 5. Closing the engineering-base gap — concrete moves

1. **Recruit a robotics/ME co-founder or found-engineer before raising.** Sources rate this the decisive factor. The school is your funnel — use it. ([SVRC](https://www.roboticscenter.ai/blog/robot-startup-guide))
2. **Stay on the software/deployment/data layer with COTS (SO-101/LeRobot).** Avoid custom actuators ($500–$5,000 and 6–12 months each). ([SVRC](https://www.roboticscenter.ai/blog/robot-startup-guide))
3. **Productize for the SME long tail — standardized, modular, recurring (RaaS)**, not bespoke consulting. ([HelloT](https://www.hellot.net/news/article.html?no=112879))
4. **Make the data flywheel the company.** Cohort-collected teleop/behavior data is the fundable, partnership-worthy asset.
5. **Add named advisors who have *deployed real robots*.** SVRC warns specifically against teams of "excellent software engineers who have never operated a physical robot."
6. **Use CES + KDT/KOSME grants as credential/runway, but drive to deployment metrics** (task-success >85%, 3+ pilots, 5,000+ demonstrations by month 12) so you don't become an "상장-only, no-매출" statistic. ([SVRC](https://www.roboticscenter.ai/blog/robot-startup-guide))

---

## 6. Next-step checklist

- [ ] Register in the **K-디지털 교·강사 Pool** (KOREATECH) — immediate, paid, no institution (see [`funding.html`](../../site/funding.html)).
- [ ] Apply to **예비창업패키지 딥테크 (로봇/AI)** — non-dilutive, background-agnostic, ~₩50M.
- [ ] Draft **two decks** (edtech + Physical-AI deep-tech) under the "talent pipeline" umbrella.
- [ ] Warm intros to **블루포인트 / 퓨처플레이** (deep-tech) and **매쉬업엔젤스 / 프라이머** (edtech) — any investment becomes your **TIPS operator**.
- [ ] Start the **teleop-data flywheel** now: every cohort submission is a LeRobot demonstration you keep.
- [ ] Identify 3–5 **robotics co-founder candidates** from your own learners.
- [ ] **Do not** pitch Plug and Play yet; revisit as a corporate-reskilling pilot later.

---

## 7. Sources

**Korea Physical AI strategy & landscape:** [Seoul Economic Daily (national strategy, 2026-06-19)](https://en.sedaily.com/technology/2026/06/19/korea-targets-top-spot-in-physical-ai-aims-to-cut-foreign) · [Korea.net (K-Humanoid Alliance)](https://www.korea.net/NewsFocus/Sci-Tech/view?articleId=269677) · [The Elec (behavior data = bottleneck)](https://www.thelec.net/news/articleView.html?idxno=11898) · [withnews (regional build-out)](https://car.withnews.kr/economy/physical-ai-in-korea) · [Sedaily (Neubility × Unitree)](https://en.sedaily.com/technology/2026/06/26/neubility-partners-with-unitree-to-co-develop-robot) · [IEEE Spectrum (China robots / US ban)](https://spectrum.ieee.org/chinese-robots-us-ban)
**Comparators / SI market:** [DAPIER bootcamp](https://semibootcamp.dongguk.edu/) · [irobotnews (SI cover story)](https://www.irobotnews.com/news/articleView.html?idxno=44101) · [HelloT (SI 실태 진단)](https://www.hellot.net/news/article.html?no=112879)
**Labor / demographics:** [Korea Herald (E-9 quota cut, 2025-12)](https://www.koreaherald.com/article/10641758)
**Funding:** [MSS 예비창업 딥테크](https://www.mss.go.kr/site/smba/ex/bbs/View.do?cbIdx=310&bcIdx=1060210&parentSeq=1060210) · [KISED](https://www.kised.or.kr/menu.es?mid=a10205010000) · [TIPS](https://www.jointips.or.kr/) · [Kakao Ventures TIPS guide](https://www.kakao.vc/blog/TIPS-eligibility-2025) · [Bluepoint](https://thevc.kr/bluepointpartners) · [FuturePlay](https://fpco-dev.futureplay.co/investment) · [Mashup](https://www.mashupventures.co/contents/5-tips-for-startup-support-programs) · [KOSME ₩11.5T fund](https://koreatechdesk.com/kosme-11-5-trillion-startup-promotion-fund)
**Plug and Play:** [Accelerator program](https://www.plugandplaytechcenter.com/innovation-services/startups/accelerator-programs) · [PnP Korea launch (2021)](https://www.prnewswire.com/news-releases/plug-and-play-korea-launches-in-seoul-301277348.html) · [PnP Korea](https://www.plugandplaykorea.com/)
**Founder strategy / robotics startups:** [Silicon Valley Robotics startup guide](https://www.roboticscenter.ai/blog/robot-startup-guide) · [Fortune (solo founders + AI)](https://fortune.com/2026/05/18/solo-founders-ai-automation-entire-teams-entrepreneurs/) · [Foundra (solo-founder ceiling)](https://www.foundra.ai/key-reads/solo-founder-ceiling-ai-stack-hire-first-may-2026-fortune) · [Forte Labs (cohort courses)](https://fortelabs.com/blog/the-rise-of-cohort-based-courses/) · [SG Analytics (M&A vs IPO 2025)](https://www.sganalytics.com/blog/vc-based-companies-are-driving-mergers-and-acquisitions/) · [YC deal](https://www.ycombinator.com/deal)

### Caveats / verify before spending money
- The Samsung "~$649B physical-AI" figure is **secondary/unconfirmed** — the clean sourced number is a *national* >₩1,000T AI-data-center blueprint by 2035. Don't cite the Samsung figure as fact.
- **National Robot Test Field (Daegu)** specifics: referenced but not primary-source-confirmed this pass — verify.
- **CES → grant** is a **scoring/credibility input**, not an automatic grant tranche.
- Government package open-call dates and TIPS caps shift annually — confirm current 공고 on K-Startup / 창업진흥원 before relying on figures.

---

*Living document · built in public · this is analysis, not investment or legal advice.*
