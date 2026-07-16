# Physical AI 기업 지도 — 큰 나무부터 (가치사슬 × 응용 산업)

> "지금 누가 로봇을 현실에 배치하나"의 기업 지도. **가치사슬(큰 나무) → 응용 산업 버티컬(잔가지)** 순으로 짚는다. 조사일 2026-07-15 (주장마다 출처 링크).
> 이 문서는 [[02-robot-industry-landscape|산업 지형(규모)]]·[[03-physical-ai-players-and-money|플레이어와 돈(뇌 vs 몸)]]의 **확장판** — 저기가 "얼마나 큰가/누가 돈 받나"라면, 여기는 **"버티컬마다 누가 있나"**.
> ⚠️ 원본은 링크드인 인포그래픽 + 현업 댓글(약칭·오탈자 포함). **웹으로 교차검증해 이름을 바로잡고, 확인 안 되는 건 "⚠️ 미확인"으로 남겼다** — 지우지 않는 게 지도의 정직함.

---

## 0. 한 장 요약 — 돈과 병목은 어느 "층"에 있나

Physical AI를 한 산업으로 세우면 **5층 가치사슬**이 된다. 응용 산업(국방·제조·휴머노이드…)은 맨 위 **잎사귀**일 뿐, 돈과 방어력은 아래 특정 층에 몰린다.

| 층 | 무엇 | 성격 | 돈/병목 |
|---|---|---|---|
| ⑤ **응용 산업** | 국방·제조·물류·우주·농업… | 실수요가 있는 시장 | 자본(특히 국방 예산)이 빠르게 유입 |
| ④ **배포·통합 (FDE)** | 현장 세팅·안전·모션플래닝 | **진짜 병목** — 이론↔현실의 간극 | 사람이 부족 (우리 각) |
| ③ **파운데이션 모델 (뇌)** | 어떤 로봇에도 얹는 범용 제어 AI(VLA) | 소프트웨어 레버리지·카피 어려움 | **자본이 가장 집중** |
| ② **센서·인지 (눈)** | 카메라·인지 모델 | 조작의 남은 난제 | → [[04-arm-hand-eye|팔·손·눈]] |
| ① **액추에이터·기체 (몸)** | 팔·손·모터·휴머노이드 바디 | **상품화(commodity)** 진행 | 원가 경쟁, 마진 압박 |

> **돈의 흐름 (2025):** 로보틱스·physical AI 스타트업이 1,009건 딜에서 기록적 **$27.6B** 조달(전년 2배+). 이 중 **"AI 플랫폼(뇌)" 층은 딜 수의 16%인데 자본의 30%를 흡수** — 딜당 수표가 몸체 제조보다 훨씬 크다. ([The New Stack](https://thenewstack.io/physical-ai-models-frontier/) · [State of Robotics 2026](https://www.roboticscenter.ai/state-of-robotics-2026)) 뇌(③)가 여러 몸에 이식되는 범용 자산이라 가장 방어 가능하다는 논리 (→ [[03-physical-ai-players-and-money|뇌 vs 몸]]).
>
> **핵심:** 잎(⑤ 산업)이 아무리 화려해도, **몸(①)은 상품화되고 뇌(③)에 돈이 몰리며, 정작 현실 배치(④)는 사람이 없다.** 이 문서의 §9가 그 지점.

---

## 1. 큰 나무 — 가치사슬 5층 자세히

- **① 액추에이터·기체(몸)** — 팔은 이미 상품($100~250 오픈소스 SO-101). 휴머노이드 바디도 중국산 부품으로 원가 경쟁. IP는 **손(그리퍼)**에 있음 (→ [[04-arm-hand-eye|팔·손·눈]]).
- **② 센서·인지(눈)** — 좌표 이동은 풀린 문제, **보고 판단하는 인지가 남은 병목.** 2026 최상위 조작 모델은 전부 RGB 카메라만 씀.
- **③ 파운데이션 모델(뇌)** — VLA(Vision-Language-Action). "한 모델로 모든 로봇" 베팅. 자본 집중 (→ [[06-robot-learning-ladder|러닝 사다리]] §5).
- **④ 배포·통합(FDE)** — 안전(FORT)·모션플래닝(Realtime)·현장 로봇 브레인(Sereact)·배포 플랫폼(Vention)이 이 층. **가장 안 팔리는 게 사람.**
- **⑤ 응용 산업** — 아래 §2~8. 국방이 가장 빠르고 확실한 자본(정부 예산).

---

## 2. 국방·공공안전 (Defense & Public Safety)

가장 빠르게 자본(정부 예산)이 몰리는 잎. ⑤ 산업이자 일부는 ③ 뇌(Scout AI)에 걸침.

| 기업 | 무엇 | 본사 | 최근 상태 (2025~2026) |
|---|---|---|---|
| **Ghost Robotics** | 군용 4족보행(Vision 60 "로봇개") | 🇺🇸 필라델피아 | **한국 LIG넥스원이 지분 60% 인수**(~$240M, 2024). 2026 팔·방수 업그레이드 ([The Robot Report](https://www.therobotreport.com/lig-nex1-announces-intent-to-acquire-quadruped-maker-ghost-robotics/)) |
| **Scout AI** | 방산용 **VLA 파운데이션 모델 "Fury"** (드론·UGV 자율화) | 🇺🇸 캘리포니아 | Series A **$100M**(2026.04). Booz Allen·DoD 계약 ([TechCrunch](https://techcrunch.com/2026/04/29/coby-adcocks-scout-ai-raises-100-million-to-train-models-for-war-we-visited-its-bootcamp/)) |
| **FORT Robotics** | 자율기계용 **안전·보안 제어**(무선 E-stop) = ④ 배포층 | 🇺🇸 필라델피아 | Series B +$18.9M(2025.08), 누적 $60.5M, ~12,000대 배치 ([The Robot Report](https://www.therobotreport.com/fort-robotics-adds-18-9m-series-b-funding-robotic-safety/)) |
| **Hypercraft** | 소프트웨어 정의 무인지상차(UGV) "Razorback", 개방형 차량 OS "Carbon" | 🇺🇸 유타 | 2026 Razorback 공개, Fortem 파트너십 ([Defense Advancement](https://www.defenseadvancement.com/news/hypercraft-debuts-razorback-hybrid-ugv-for-software-defined-tactical-operations/)) |
| **Havoc AI** | 자율 무인수상정(USV) 군집 "Rampage" | 🇺🇸 로드아일랜드 | **$85M**(2025), 누적 ~$100M. In-Q-Tel·Lockheed·한화 ([The Robot Report](https://www.therobotreport.com/havocai-obtains-85m-to-scale-autonomous-marine-systems/)) |
| **Swarm Aero** | 다임무 UAV + 군집 소프트웨어 | 🇺🇸 캘리포니아 | Series A **$35M**(2026.03), DIU 선정 ([Business Wire](https://www.businesswire.com/news/home/20260310673101/en/)) |
| **ACS = Allen Control Systems** | 자율 대(對)드론 무기 스테이션 "Bullfrog" | 🇺🇸 오스틴 | Series A $30M(Craft Ventures) ([OODA Loop](https://oodaloop.com/company-profiles/defense-tech/allen-control-systems/)) |
| **ARK** ⚠️ 미확인 | 약칭 — 최유력 후보 **Ark Robotics**(드론 군집 OS, 우크라이나) | 🇪🇪/🇺🇦? | ARK Electronics·ARK Invest와 혼동 여지. 원문 재확인 필요 ([ark-robotics.com](https://ark-robotics.com/)) |

---

## 3. 제조·자동화 (Manufacturing & Automation)

스마트팩토리 = 피지컬 스파크 타겟과 가장 직접적인 잎. ④ 배포층(Vention)과 겹침.

| 기업 | 무엇 | 본사 | 최근 상태 (2025~2026) |
|---|---|---|---|
| **Hadrian** (Hadrian Automation) | 항공우주·방산 정밀부품 **자율 공장** | 🇺🇸 캘리포니아 | Series C **$260M**(2025.07). Factory 3 신설, Hadrian Maritime 출범 ([TechCrunch](https://techcrunch.com/2025/07/17/hadrian-raises-260m-to-build-out-automated-factories-for-space-and-defense-parts/)) |
| **Vention** | 브라우저에서 자동화 셀 설계→배포하는 **클라우드 제조 플랫폼** = ④ 배포층 | 🇨🇦 몬트리올 | MachineMotion AI 컨트롤러 출시(2025). 고객 4,000+ ([Vention](https://vention.com/about)) |
| **Novarc Technologies** | 파이프 용접 협동로봇 + AI 비전 NovAI | 🇨🇦 밴쿠버 | Series B **$50M**(2025.03) ([GlobeNewswire](https://www.globenewswire.com/news-release/2025/03/11/3040831/0/en/NOVARC-RAISES-50-MILLION-SERIES-B-TO-EXPAND-ITS-AI-POWERED-MACHINE-VISION-NOVAI-FOR-AUTOMATED-WELDING-SOLUTIONS.html)) |
| **O-HIVE.AI** | 3D 공간지능 플랫폼(저가 카메라로 공간 캡처·분석) | 🇺🇸 델라웨어 | ⚠️ 실존하나 **매우 초기**(ARR ~$1.5M, Series A 모집 중). 언론 검증 빈약 ([o-hive.ai](https://o-hive.ai/)) |
| **FR** ⚠️ 미확인 | 약칭 — 최유력 후보 **Fairino**(중국 협동로봇, 제품군이 FR3·FR5… 시리즈) | 🇨🇳 쑤저우? | Formic/Fanuc/FarmWise 가능성 낮음. 원문 재확인 필요 ([Fairino](https://www.fairino.us/)) |

---

## 4. 휴머노이드 (Humanoids)

관심은 최대, 성숙도는 최저. 대부분 1회 충전 ~2시간이라 8시간 교대는 아직 멀다 ([IEEE Spectrum](https://spectrum.ieee.org/humanoid-robot-scaling)). 층으로는 ① 몸(바디)이 핵심.

| 기업 | 무엇 | 본사 | 최근 상태 (2025~2026) |
|---|---|---|---|
| **Tesla (Optimus)** | 자사 공장용 범용 휴머노이드, 대량생산 목표 | 🇺🇸 텍사스 | Gen3 1,000+대 사내 가동, V3 바디 2026 하반기 공개 예정. 목표가 $20~30K ([The Robot Report](https://www.therobotreport.com/from-evs-to-robotics-tesla-targets-10m-optimus-units-with-new-texas-plant/)) |
| **Agility Robotics** | 물류·창고용 이족 휴머노이드 Digit (세계 최다 상업 배치) | 🇺🇸 오리건 | Series C $400M(2025). **2026.06 SPAC 상장 발표(~$2.5B, Nasdaq: AGLT)**, Foxconn 참여 ([GeekWire](https://www.geekwire.com/2026/digit-maker-agility-robotics-to-go-public-in-2-5b-deal-heres-what-the-filings-say-about-its-finances/)) |
| **Neura Robotics** | 유럽 최대 풀스택 휴머노이드·물리 AI | 🇩🇪 메칭엔 | **Series C up to $1.4B @ $7B**(2026.06) — 풀스택 로봇 사상 최대. Amazon·NVIDIA·Bosch ([CNBC](https://www.cnbc.com/2026/06/10/neura-robotics-funding-ai-humanoid-robots.html)) |
| **Figure AI** | 실환경 배치용 범용 휴머노이드(Figure 02/03) | 🇺🇸 캘리포니아 | Series C **$1B+ @ $39B**(2025.09). 2024 대비 15배 ([TechCrunch](https://techcrunch.com/2025/09/16/figure-reaches-39b-valuation-in-latest-funding-round/)) |
| **1X Technologies** | 가정용 휴머노이드 NEO 소비자 직판(OpenAI 투자) | 🇳🇴/🇺🇸 오슬로 | NEO 사전주문($20K/월$499), 5일 만에 1만 대. 2026 양산. ⚠️ 초기엔 원격조작 의존 지적 ([The Robot Report](https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/)) |
| **Sanctuary AI** | 정교한 로봇 손·인지 SW. **2026 완제품 대신 SW·손 라이선스로 피벗** | 🇨🇦 밴쿠버 | Phoenix 8세대, 누적 $140M+. 대형 신규 라운드 미확인 ([Sanctuary](https://sanctuary.ai/news/)) |
| **FF AI-Robotics = Faraday Future** | 휴머노이드+로봇개+이동형 매니퓰레이터 (상장 EAI) | 🇺🇸 LA | Nasdaq: FFAI. "FF EAI Robot World" 공개(2026.06). **Fourier 아님** ([Business Wire](https://www.businesswire.com/news/home/20260622927175/en/)) |
| **SURE** ⚠️ 미확인 | 대응 기업 확인 실패. 후보: **Sunday Robotics**(가사 휴머노이드 Memo, $165M @ $1.15B, 2026.03) — 전사 오류 가능성 | 미확인 | 원문 철자 재확인 필요 ([TechCrunch(후보)](https://techcrunch.com/2026/03/12/humanoid-robotics-maker-sunday-reaches-1-15b-valuation-to-build-household-robots/)) |

---

## 5. 파운데이션 모델 · AI 두뇌 (Foundation Models = ③ 뇌)

소프트웨어 엔지니어가 하드웨어와 가장 쉽게 접점을 찾는 층. **자본이 가장 집중**되는 곳.

| 기업 | 무엇 | 본사 | 최근 상태 (2025~2026) |
|---|---|---|---|
| **Physical Intelligence (π)** | 범용 로봇 VLA **π0(pi-zero)** — 빨래·식탁정리 등 | 🇺🇸 샌프란시스코 | Series B **$600M @ $5.6B**(2025.11 확정). $11B+ 추가 조달 협상 중(미확정) ([The Robot Report](https://www.therobotreport.com/physical-intelligence-raises-600m-advance-robot-foundation-models/)) |
| **Skild AI** | **"omni-bodied"** 통합 파운데이션 모델(Skild Brain) — 어떤 몸체든 재학습 없이 | 🇺🇸 피츠버그 | Series C **~$1.4B @ $14B+**(2026.01, SoftBank 주도). 삼성·LG 참여 ([The Robot Report](https://www.therobotreport.com/skild-ai-raises-1-4b-building-omni-bodied-robot-skild-brain/)) |
| **Field AI (FieldAI)** | 지도·GPS 없이 자율주행하는 embodiment-agnostic 파운데이션 모델 | 🇺🇸 캘리포니아 | **$405M @ $2B**(2025.08). Bezos Expeditions·NVIDIA ([CNBC](https://www.cnbc.com/2025/08/20/gates-nvidia-fieldai-robotics.html)) |
| **RLWRLD** | 🇰🇷 한국 physical AI 파운데이션 모델(공장·물류). 창업 류중희(전 올라웍스→Intel) | 🇰🇷 서울 | Seed 누적 ~$41M(2026.02 $26M). LG·SKT·KDDI·ANA ([The Robot Report](https://www.therobotreport.com/physical-ai-startup-rlwrld-raises-26m/)) |
| **Dyna Robotics** (DYNACOSI ⚠️) | 상용 배포 로봇 파운데이션 모델 **DYNA-1**(무인 반복작업 99.4%) | 🇺🇸 캘리포니아 | Series A **$120M**(2025.09). "DYNACOSI"는 미확인 → Dyna Robotics로 추정 대체 ([The Robot Report](https://www.therobotreport.com/dyna-robotics-closes-120m-funding-round-to-scale-robotics-foundation-model/)) |
| **Covariant** | 창고 로봇 파운데이션 모델. **인수 아님** → Amazon이 창업자·직원 채용 + 비독점 라이선스($380M)한 **역인수(reverse acqui-hire)**, 회사 존속 | 🇺🇸 에머리빌 | 2024.08~09. COO Ted Stinson이 CEO ([GeekWire](https://www.geekwire.com/2024/amazon-hires-covariant-founders-inks-licensing-deal-with-robotics-ai-startup-in-latest-reverse-acquihire-deal/)) |
| **Realtime Robotics** | 실시간 **충돌회피 모션플래닝**(RapidPlan) = ④ 배포층에 가까움(순수 VLA 아님) | 🇺🇸 보스턴 | 미쓰비시전기 전략투자(2024), 누적 $60M+. Resolver 공개 ([The Robot Report](https://www.therobotreport.com/realtime-robotics-gets-series-b-funding-from-mitsubishi-electric/)) |
| **Shield AI** (SHILD 오타) | 드론·항공기 **국방 자율비행 AI "Hivemind"** — 파운데이션 모델보다 방산 자율에 가까움 | 🇺🇸 샌디에이고 | Series G **$2B @ $12.7B**(2026.03) ([Fortune](https://fortune.com/2026/03/26/shield-ai-revenue-series-g-funding-12-billion-valuation/)) |

> 🔐 **임베디드 보안 각도:** 2025년 로봇 대상 공격 45%↑, HF 등에서 오염 모델 100+ 발견, 단일 음성 명령으로 휴머노이드 제어 탈취 시연까지 ([IOActive](https://www.ioactive.com/from-skynet-to-ai-agents-the-state-of-robot-security-nine-years-later/) · [SoK arXiv](https://arxiv.org/pdf/2606.16788)). **로봇 두뇌 코드 보호**가 미래 핵심 레이어 — 창업자의 차량 보안(현대오토에버)·42 C 배경과 직결되는 차별화 포인트.

---

## 6. 우주 (Space Robotics)

| 기업 | 무엇 | 본사 | 최근 상태 (2025~2026) |
|---|---|---|---|
| **GITAI** | 우주용 로봇팔·궤도상 조립·위성 서비싱 (→ 우주기반 요격체로 방산 확장) | 🇺🇸 토런스 | ⚠️ **일본 아니라 미국**(2023 본사 이전). MDA SHIELD·우주군 SBI 선정 ([SpaceNews](https://spacenews.com/gitai-gets-funds-to-develop-in-orbit-robotic-servicer/)) |
| **Katalyst Space Technologies** | 위성 서비싱·궤도상 로지스틱스(NEXUS 우주선) | 🇺🇸 애리조나 | $12M(2026.06). NASA $30M 계약 ([SpaceNews](https://spacenews.com/katalyst-space-raises-12-million-for-geo-servicing-demo-mission/)) |
| **Icarus Robotics** | 궤도상 "창고 노동" 임바디드 AI 로봇("Joy", 2개 팔) | 🇺🇸 뉴욕 | 시드 $6.1M(2025.09). Voyager와 ISS 실증(2027) ([TechCrunch](https://techcrunch.com/2025/09/17/icarus-raises-6-1m-to-take-on-spaces-warehouse-work-with-embodied-ai-robots/)) |
| **PIAP Space** | 우주 로봇(위성통합·우주쓰레기 제거·매니퓰레이터 "TITAN") | 🇵🇱 바르샤바 | ESA MANUS(달) 매니퓰레이터 개발 ([The Robot Report](https://www.therobotreport.com/titan-robotic-arm-from-piap-space-automate-in-orbit-inspection/)) |
| **FWR** ⚠️ 미확인 | 우주 로봇 문맥에서 확정 실패. 후보: NASA **FFR** 미션 오기, 또는 Orbital Robotics | 미확인 | 원문 철자 재확인 필요 ([NASA FFR](https://www.nasa.gov/mission/fly-foundational-robots/)) |

---

## 7. 물류·창고 & 건설·인프라 (Warehouse/Logistics & Construction)

로봇 시장의 최대 조각(물류 39%, → [[02-robot-industry-landscape|산업 지형]]). 이미 실전·규모의 게임.

| 기업 | 무엇 | 본사 | 최근 상태 (2025~2026) |
|---|---|---|---|
| **Exotec** | 고밀도 창고 자동화 Skypod(3D 이동 AMR) | 🇫🇷 릴 | 누적 $477M @ $2B(프랑스 1호 산업 유니콘), 매출 $1B 돌파 ([Exotec](https://www.exotec.com/en-gb/news/exotec-leves-335-million-dollars-and-becomes-frances-first-industrial-unicorn/)) |
| **Sereact** | 어떤 로봇에도 도는 **AI "로봇 브레인" Cortex**(창고 picking) = ④ 배포층 | 🇩🇪 슈투트가르트 | Series B **$110M**(2026.04), 미국 진출 ([The Robot Report](https://www.therobotreport.com/sereact-gets-series-b-funding-expand-cortex-2-robot-brain-enter-u-s-market/)) |
| **Built Robotics** | 기존 중장비를 자율화하는 리트로핏 키트 "Exosystem" | 🇺🇸 샌프란시스코 | 2025 미 건설 로보틱스 투자 $1.36B(+125%)의 주요 플레이어 ([Built Robotics](https://www.builtrobotics.com/about/press)) |
| **Dusty Robotics** | BIM 도면을 현장 바닥에 인쇄하는 자율 레이아웃 로봇 FieldPrinter | 🇺🇸 마운틴뷰 | Series B **$45M**, 누적 $68.7M ([IRONPROS](https://www.ironpros.com/construction-robotics/article/22908766/dusty-robotics-to-use-45m-in-series-b-funding-to-scale-digital-floorplan-printing)) |

---

## 8. 틈새 · 필수 레이어 (Niche & Infrastructure)

- **공급망·부품:** **Sentinel Automata** ⚠️ **미확인** — "미국산 로봇 부품/공급망" 정의에 맞는 동명 기업을 공개 웹에서 확인 못 함. 유사 후보(Sentinel Robotic Solutions 등)와 불일치 → **산업 지도에 넣지 않기를 권장.**
- **농업(AgTech):** 회사가 아니라 **범주명.** 2026 대표: [**Carbon Robotics**](https://carbonrobotics.com/)(AI 레이저 제초 LaserWeeder) · [**Monarch Tractor**](https://www.monarchtractor.com/)(전기·자율 트랙터 MK-V) · **John Deere**(Level 4 자율 트랙터, 대형 강자). ⚠️ FarmWise는 2025 사업종료·Taylor Farms 인수 → 현역 사례로 쓰지 말 것.

---

## 9. 병목은 '배포(Deployment)' — 왜 이 지도가 우리 각인가

위 40여 개 기업의 공통 병목: **이론(랩의 코드)은 완벽해도, 현실 세계 배치(④층)는 엉망이다.** 몸(①)은 상품화되고 뇌(③)엔 수십억이 몰리는데, 그 로봇을 **현장(스마트팩토리·국방·물류)에서 세팅하고 물리적으로 최적화할 사람**이 태부족이다 — 휴머노이드조차 "통제된 파일럿에서 소수만 배치"된 상태 ([Bain](https://www.bain.com/insights/humanoid-robots-from-demos-to-deployment-technology-report-2025/)).

피지컬 스파크의 각: **이 수많은 글로벌 로봇을 한국 현장에 들여왔을 때, SW로 세팅하고 최적화하는 '디플로이먼트 엔지니어(FDE)'를 길러내는 훈련소.** 위 기업들이 곧 우리 수강생의 미래 취업·파트너십 시장이다. (한국 실탄: Ghost Robotics ← LIG넥스원, RLWRLD, Skild·Neura·Physical Intelligence에 삼성·LG·SK 투자.)

---

## 관련 (Related)
- [[02-robot-industry-landscape|로봇 산업 지형(규모)]]
- [[03-physical-ai-players-and-money|플레이어와 돈(뇌 vs 몸)]]
- [[04-arm-hand-eye|팔·손·눈(부위별)]]
- [[06-robot-learning-ladder|로봇 러닝 사다리(기술)]]
- [[00-foundations|기초 지식 지도]]
- [[market-landscape|경쟁사 스캔(교육시장)]]
