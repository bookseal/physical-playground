# Material — 하드웨어 & 시뮬레이션 가이드

> "실물 로봇을 사기 전에 시뮬레이션으로 먼저 익힌다"는 전제에서, **무엇으로 돌릴 수 있나**를 정리.
> 두 축으로 나눔: **① Simulation (지금)** vs **② 실물 로봇 (나중)**. 조사일 2026-07-07.

---

## ① Simulation — 어떤 컴퓨터로 되나

### 결론 먼저 (TL;DR)
| 장비 | Isaac Sim (SO-101 sim) | LeRobot + MuJoCo (Mac 경로) |
|---|---|---|
| **Mac (Apple Silicon)** | ❌ 불가 (NVIDIA GPU 필요) | ✅ 됨 |
| **MSI GF76 (RTX 3060 랩탑, 6GB VRAM, 16GB RAM)** | ⚠️ **공식 최소 미달** (아래) | ✅ 됨 |
| **클라우드 GPU (RTX 8GB+)** | ✅ 됨 (권장) | ✅ 됨 |

### MSI GF76 (RTX 3060 랩탑)으로 Isaac Sim 되나?
**공식 최소 사양에 못 미칩니다.** NVIDIA Isaac Sim은 **RTX GPU + 최소 8GB VRAM**을 요구하는데, 랩탑용 RTX 3060은 보통 **6GB VRAM**입니다. RAM도 권장 32GB에 비해 16GB는 낮음.
- [Isaac Sim 공식 요구사양](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html): 8GB VRAM 미만은 "복잡한 씬(16MP/frame 이상) 렌더 불가", 일부 튜토리얼·벤치마크 실행 안 됨.
- 현실적 판정: **작은 씬은 겨우 뜰 수 있지만, SO-101 워크숍/GR00T 학습은 버겁습니다.** 시간 낭비 위험.
- 참고: 같은 RTX 3060도 **데스크탑판(12GB VRAM)** 이면 최소 사양을 넘겨 됩니다. 랩탑 6GB가 문제.

→ **권장: GF76은 Windows에서 LeRobot+MuJoCo(가벼운 경로)에 쓰고, 진짜 SO-101 sim은 클라우드 GPU로.**

### Mac 사용자(그리고 GPU 부족자)는 클라우드 GPU를 어떻게 빌리나
Isaac Sim은 **컨테이너로 클라우드에서 돌리고 화면만 스트리밍**하는 방식을 공식 지원합니다 — 로컬에 NVIDIA GPU가 없어도 됨.

| 방법 | 무엇 | 난이도/비용 | 비고 |
|---|---|---|---|
| **NVIDIA Brev** ⭐ | Isaac Sim을 **원클릭**으로 클라우드 GPU에 띄우고 스트리밍 | 쉬움 · 시간당 과금 | Mac 사용자 1순위. [developer.nvidia.com/isaac/sim](https://developer.nvidia.com/isaac/sim) |
| **Isaac Automator** | AWS/GCP/Azure/Alibaba에 Isaac Sim/Lab 자동 배포 | 중간 · 클라우드 요금 | [공식 클라우드 배포 문서](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/cloud_installation.html) |
| **RunPod / Vast.ai** | 값싼 시간당 GPU 대여 | 중간 · **가장 저렴** | Isaac Sim 공식 지원 X(직접 세팅). Vast가 보통 최저가, RunPod가 편의성. ([비교](https://medium.com/@velinxs/vast-ai-vs-runpod-pricing-in-2026-which-gpu-cloud-is-cheaper-bd4104aa591b)) |

- **추천 흐름**: 개념·툴체인은 Mac에서 LeRobot(무료) → SO-101 sim을 실제로 돌려볼 땐 **Brev로 몇 시간 빌려서**(RTX 8GB+ 인스턴스) 워크숍 수행. 상시 켜둘 필요 없이 쓸 때만.
- **팁**: 클라우드는 시간당 과금이라 **미리 할 일 정리 → 짧게 집중** 하는 게 비용 최적. 데이터셋·결과는 로컬로 내려받기.

세부 세팅 단계는 → [`lab/tutorials/00_sim-setup-before-pat-me.md`](tutorials/00_sim-setup-before-pat-me.md).

---

## ② 실물 로봇 — 나중에 살 것

- **SO-101** (LeRobot 표준 6-DOF 팔): 오픈소스 키트, 수백 달러대. 보통 **leader(텔레옵용)+follower(정책 구동용) 페어**로 판매.
  - [SO-101 키트 리뷰](https://thinkrobotics.com/blogs/product-reviews-buying-guides/thinkrobotics-lerobot-so-101-6-axis-robotic-arm-review-ai-ready-open-source-and-built-for-learning)
  - 조달: 아마존 vs 알리익스프레스 가격·배송 비교(우리 검증 액션).
- **언제 사나**: 시뮬로 "Red Light, Green Light 직전"까지 익힌 뒤 — 실물은 teleop 데이터 수집·실전 평가 때 진짜 가치. 그 전엔 sim으로 충분.
- 실물 붙일 때 소프트웨어: LeRobot `.[feetech]`(SO-101 모터) 설치 → 캘리브레이션 → teleop 기록.

---

## 우리 커리큘럼 관점
- **"초등학생도"가 아니라 "GPU 없어도"** 시작 가능해야 문턱이 낮다 — 그래서 **Mac/CPU LeRobot 경로가 진입 과제(토닥토닥)의 기본**, 클라우드/실물은 심화 단계에 배치.
- 학습자마다 장비가 다르므로, 각 과제에 **"필요 장비 등급"**(Mac-OK / GPU 필요 / 실물 필요)을 태그로 붙이면 좋음.

---

## 관련 (Related)
- [[00-foundations|기초 지도]]
- [[00_sim-setup-before-pat-me|시뮬 세팅 튜토리얼]]
- [[index|튜토리얼 레퍼런스 모음]]
