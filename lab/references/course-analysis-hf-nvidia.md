# 코스 분석 — HF LeRobot vs NVIDIA Physical AI (커리큘럼 raw material)

> 두 대표 코스를 실제로 뜯어본 분석. **우리 커리큘럼을 어떻게 짤지**의 원자료.
> 조사일 2026-07-07. 출처: [HF Robotics Course](https://huggingface.co/learn/robotics-course) ·
> [NVIDIA Physical AI Learning](https://docs.nvidia.com/learning/physical-ai/).
> 관점 지도는 [[00-foundations|기초 지식 지도]] 참조.

---

## 1. HF LeRobot "Robotics Course" — 무료 유닛제

**구조 (6유닛, 순차):**
| Unit | 제목 | 상태 |
|---|---|---|
| 0 | Welcome to the Robotics Course | ✅ |
| 1 | Course Introduction | ✅ |
| 2 | Classical Robotics | ✅ |
| 5 | Reinforcement Learning | 🔜 |
| 6 | Imitation Learning | 🔜 |
| 7 | Foundation Models | 🔜 |

**교수법 (pedagogy):**
- 유닛당 **30~45분**(읽기+개념+코딩), **자율 진도**.
- **유닛 끝 퀴즈**로 이해 점검.
- **핸즈온 코드**(LeRobot 프레임워크) + **시뮬 환경**(하드웨어 없이 참여 가능).
- 점진적 스캐폴딩(입문→고급), 실사례 연결.
- **선수지식**: 파이썬 기초(변수·함수·루프) 필수, 선형대수/미적분/ML은 있으면 좋음. **1순위 = 호기심**.

**랜딩 구조**: 히어로 → 가치 제안 → **신텍스(syllabus) 표** → 선수지식 → FAQ → 커뮤니티/기여.

**성격**: 개념→코드→퀴즈의 **교과서형**. 흐름(🅱 학습 세계)이 명확하고, 무료+오픈이라 우리 커리큘럼의 **한국어·놀이화 큐레이션 원본**으로 최적.

## 2. NVIDIA "Physical AI Learning" — 다중 경로 허브

**탐색 구조**: **topic / product / task** 3중 내비 + course finder(의도 기반 매칭).

**코스 목록 (레벨·시간 명시):**
| 코스 | 레벨 | 시간 | 내용 |
|---|---|---|---|
| Train an SO-101 (Sim-to-Real) | Int | 6~10h | 캘리브레이션·시연·sim2real 전략 |
| Getting Started w/ Isaac Sim | **Beg** | 2~3h | 로봇 빌드·물리·센서 |
| Getting Started w/ Isaac Lab | Int | 3~4h | RL·GPU 가속 학습 |
| Getting Started w/ Isaac ROS | Int | 2~3h | ROS2 + Isaac ROS |
| Humanoid End-to-End (GR00T+Unitree G1) | Int | 4~12h | teleop·데이터·정책·배포 |
| Digital Twins (Omniverse/OpenUSD) | Int | 3~4h | 공장/창고 씬 |
| Learn OpenUSD | Beg~Adv | — | +전문 인증 |

**교수법**: **프로젝트 기반**, 시뮬(Isaac) 중심, **레벨+시간 태그**, **Brev 클라우드 GPU**(로컬 설치 없이), 인증 경로, Discord/포럼/유튜브.

**성격**: **레퍼런스·역량 카탈로그형**. 각 코스가 독립 모듈, 레벨/시간으로 진입 결정. 강력하지만 **커뮤니티/피드백 루프는 약함**(혼자 함).

## 3. 나란히 비교

| | HF LeRobot | NVIDIA Physical AI |
|---|---|---|
| 형태 | 순차 유닛 교과서 | 모듈 카탈로그 |
| 진입 | 파이썬만 | 레벨별(Beg~Adv) |
| 하드웨어 | 없이 가능(sim) | Brev 클라우드 GPU |
| 세계([[00-foundations]]) | 🅱 학습 중심 | 🅰+🅱 (Isaac·ROS·GR00T) |
| 약점 | 아직 유닛 미완(5~7) | 고사양·혼자·피드백 없음 |

## 4. 우리 커리큘럼에 훔칠 것 (steal list)
1. **레벨 + 예상시간 태그** (NVIDIA식) — 미션마다 "Beginner · ~1h" 붙이기. 진입 판단이 쉬워짐.
2. **30~45분 청크 + 유닛 끝 퀴즈** (HF식) — 완주율·리텐션 장치와 결합.
3. **Sim-first, 하드웨어 없이 시작** (둘 다) — 우리 "GPU 없어도" 논지와 정합. [[hardware-and-simulation]] 참조.
4. **클라우드 GPU 옵션** (NVIDIA Brev) — 심화 미션의 표준 경로로 안내.
5. **우리만의 결정타 = 피어리뷰 커뮤니티** — 둘 다 없는 것(HF=혼자 코드, NVIDIA=혼자 프로젝트). 이게 우리 해자. [[hate-map|Hate Map]]·[[market-landscape|시장 스캔]]과 일치.
6. **무료 유닛으로 모객 → 유료 코호트** (HF 무료 + Vizuara 유료 부트캠프 모델 혼합).

## 5. 제안 — 우리 커리큘럼 v0 매핑
- **입문 트랙(무료)**: HF Unit 0~2를 한국어·놀이화로 큐레이션 + 우리 "토닥토닥" 미션. 레벨: Beginner · Mac-OK.
- **핵심 트랙(유료 코호트)**: pick&place → Red Light, Green Light. sim(무료 경로) → 클라우드 GPU(심화). 각 미션 = 30~45분 청크 + 퀴즈 + **피어리뷰 제출**.
- **심화**: NVIDIA SO-101 Sim-to-Real·GR00T를 "다음 스텝"으로 링크(우리가 다시 안 만듦 — [[0001-referencing-courses-and-contribution-model|ADR 0001]]: 링크+재작성).

---

## 관련 (Related)
- [[00-foundations|기초 지식 지도]]
- [[hardware-and-simulation|하드웨어/시뮬 가이드]]
- [[index|튜토리얼 레퍼런스 모음]]
- [[market-landscape|시장 스캔]]
- [[hate-map|Hate Map]]
