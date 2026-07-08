# 온보딩 — Physical Revolt 둘러보기 🕹️

> 이 저장소가 처음이라면 여기서 시작하세요. **합류를 고민 중인 동료**, 또는 새로 합류한 분을 위한 지도입니다.
> 문서 내용은 계속 바뀌므로, 이 문서는 **"어디에 뭐가 있고 어떤 순서로 읽으면 좋은지"** 를 링크 중심으로 안내합니다.
> 프로젝트가 뭔지부터 궁금하면 → **[합류 안내(왜 지금인가)](docs/join-us.md)** · [README](README.md).

---

## 이 저장소는 어떻게 구성됐나 (Playbook)
우리는 프로젝트를 하나의 **운영 시스템(Playbook)**처럼 굴립니다. 폴더마다 역할이 하나씩:

| 폴더 | 무엇을 담나 |
|---|---|
| **[docs/](docs)** | 우리 벤처 — 제품 컨셉·시장·포지셔닝 |
| **[knowledge/](knowledge)** | 분야 이해 — physical AI 기초·잡마켓·산업 지형 |
| **[lab/](lab)** | 직접 해보기 — 시뮬 튜토리얼·하드웨어·외부 레퍼런스 |
| **[decisions/](decisions)** | 의사결정 기록(ADR) — "왜 이렇게 정했나" |
| **[design/](design)** | 디자인 시스템 (Re-Volt 무드) |
| **[site/](site)** | 실제 웹 — 랜딩·코스·합류 페이지 |
| **[logs/](logs)** | 빌드 로그 — 고심과 시행착오의 흔적 |

> (비공개 자료 — 개인 컨텍스트·멘토 리서치·초안 — 는 **별도 private 저장소**에 있습니다. 여기 공개 repo엔 안전한 것만.)

---

## 읽는 순서 (추천 경로)

### 0. 왜 이걸 하나 (5분)
- **[합류 안내 / 왜 지금인가](docs/join-us.md)** ⭐ — SaaS vs Physical AI, 시장, 우리의 각
- [README](README.md) — 한눈에 보는 프로젝트

### 1. 분야 이해 (헤매지 않으려면 이걸 먼저)
- **[기초 지식 지도](knowledge/00-foundations.md)** ⭐ — ROS 세계 vs 학습 세계, 스택 6층, 용어사전
- [잡마켓: ROS vs Physical AI](knowledge/01-job-market-ros-vs-physical-ai.md)
- [로봇 산업 지형](knowledge/02-robot-industry-landscape.md)
- [플레이어와 돈 (뇌 vs 몸)](knowledge/03-physical-ai-players-and-money.md)

### 2. 우리 벤처
- [제품 컨셉](docs/01-concept/product-concept.md) — 미션 시퀀스, "교재 vs 플랫폼"
- [시장 스캔 (미·중 경쟁사)](docs/02-market/market-landscape.md)
- [Hate Map (경쟁사 혹평 → 우리 기회)](docs/02-market/hate-map.md)
- [포지셔닝 & 피치](docs/03-positioning/positioning-and-pitch.md)

### 3. 직접 해보기 (손으로)
- **[시뮬 세팅 튜토리얼](lab/tutorials/00_sim-setup-before-pat-me.md)** — Mac에서 오늘 당장 "pat me 직전"까지
- [하드웨어 & 시뮬 가이드](lab/hardware-and-simulation.md) — RTX·클라우드 GPU·SO-101
- [튜토리얼 레퍼런스 모음](lab/references/index.md) · [HF·NVIDIA 코스 분석](lab/references/course-analysis-hf-nvidia.md)

### 4. 어떻게 결정하고 짓나
- [ADR 0001 — 코스 참고 & 기여 모델](decisions/0001-referencing-courses-and-contribution-model.md)
- [ADR 0002 — private 요소 처리](decisions/0002-handling-private-elements.md)
- [디자인 테마 (Re-Volt)](design/design-theme.md) · [빌드 로그](logs/2026-07_courses-and-game-build.md)

---

## 실제 결과물 (웹)
- **랜딩**: [`site/index.html`](site/index.html) (플레이 가능한 미니게임 포함)
- **코스**: [`site/courses/`](site/courses) — 3개 미션 동적 커리큘럼
- **합류 페이지**: [`site/join.html`](site/join.html)
- 배포되면 공개 URL로 공유 예정 (GitHub Pages).

## 기여하는 법
문서는 markdown, 저장소 하나에서 관리합니다. 고칠 게 보이면 **이슈나 PR** 환영 —
방식은 [ADR 0001의 "기여 모델"](decisions/0001-referencing-courses-and-contribution-model.md) 참고.
연락: [GitHub bookseal](https://github.com/bookseal).
