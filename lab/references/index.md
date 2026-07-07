# Physical AI 튜토리얼 레퍼런스 모음 (외부 자료)

> 우리 커리큘럼(토닥토닥 → pick&place → Red Light Green Light)을 만들 때 참고할 **공개 튜토리얼 원자료**.
> 조사일 2026-07-07. 각 항목: 무엇인지 · 링크 · **하드웨어/OS 요구** · 우리 미션과의 연결.
> ⚠️ **핵심 결론**: SO-101을 *시뮬레이션*으로 돌리는 NVIDIA 경로는 전부 **Ubuntu Linux + NVIDIA RTX GPU 전용**.
> macOS에서 당장 되는 건 **HF LeRobot + MuJoCo gym**(SO-101 아님). 자세한 건 `lab/tutorials/00_sim-setup-before-pat-me.md`.

---

## A. NVIDIA — SO-101 Sim-to-Real (가장 공식적·본격적)

### A1. 공식 학습 경로: "Train an SO-101 Robot From Sim-to-Real With NVIDIA Isaac" ⭐
- **링크**: https://docs.nvidia.com/learning/physical-ai/sim-to-real-so-101/
- **내용**: SO-101 팔로 pick-and-place(원심분리기 vial 꽂기)를 **먼저 sim에서, 그다음 실물에서** — VLA 모델(GR00T) 후훈련까지 엔드투엔드.
- **요구**: Ubuntu Linux + RTX GPU (아래 A2 참조). **macOS 불가.**
- **전체 목차**(우리가 "세팅 단계"로 참고할 앞부분 굵게):
  - 01 Overview · 02 How to take this course · 03 Sim-to-Real 개념 · 04 LeRobot 배경
  - **05 Build the workspace · 06 Get the code & models · 07 Calibrate SO-101 · 08 Operate SO-101**
  - 09 Strategy1 도메인 랜덤화(teleop) · 10 GR00T · 11 Sim 평가 · 12 실물 평가
  - 13 co-training · 14 Cosmos 합성데이터 · 15 SAGE · 16 결론
  - Reference: quick_reference / datasets-and-models / troubleshooting
- **우리 연결**: 05~08이 "pat me 직전까지 세팅"의 정석 뼈대. 우리 Red Light Green Light 과제의 sim-to-real 논리도 여기서 차용.

### A2. 코드: isaac-sim/Sim-to-Real-SO-101-Workshop (Docker)
- **링크**: https://github.com/isaac-sim/Sim-to-Real-SO-101-Workshop
- **요구 (README 명시)**: OS **Ubuntu Linux >22.04**, GPU **RTX 6000 Pro/5090(Blackwell) 또는 RTX 6000(Ada)** 검증됨, Docker + CUDA Toolkit + NVIDIA Container Toolkit. **Linux 전용.**
- **핵심 커맨드**: `git clone` → `docker build -t teleop-docker -f docker/sim/Dockerfile .` → `docker run ... teleop-docker` 안에서 `list_envs` / `lerobot_agent`(teleop) / `lerobot_eval`.
- **배너 이미지**: https://github.com/isaac-sim/Sim-to-Real-SO-101-Workshop/raw/main/images/so101_banner.png

### A3. LeIsaac (Lightwheel) + Seeed Studio 위키 — 가장 구체적인 sim 세팅
- **링크**: https://wiki.seeedstudio.com/simulate_soarm101_by_leisaac/ · 코드 https://github.com/LightwheelAI/leisaac
- **요구**: Ubuntu 22.04, **RTX 3080 이상 권장** (A2보다 문턱 낮음).
- **세팅 흐름**: conda(py3.10) → CUDA 11.8 → PyTorch(cu118) → `isaacsim[all]==4.5.0` → IsaacLab v2.1.0 `./isaaclab.sh --install` → `leisaac` 설치 → USD 에셋(so101_follower.usd, kitchen scene) 다운 → `teleop_se3_agent.py --task=LeIsaac-SO101-PickOrange-v0`로 키보드 teleop.
- **우리 연결**: SO-101이 실제로 sim 씬에 로드되는 걸 보고 키보드로 움직이는 지점 = "pat me 직전". RTX 3080↑ 있으면 A 중 가장 현실적.

## B. Hugging Face LeRobot — Mac에서 되는 경로 (표준 툴체인)

### B1. LeRobot 설치 문서 (macOS Apple Silicon 지원) ⭐
- **링크**: https://huggingface.co/docs/lerobot/en/installation
- **요구**: Python ≥3.12(conda/miniforge 권장). **macOS Apple Silicon 지원**(MPS/CPU, 영상은 pyav 폴백). Linux는 CUDA 휠 자동.
- **핵심**: `conda create -n lerobot python=3.12` → `git clone huggingface/lerobot` → `pip install -e ".[all]"` (또는 `.[pusht]`,`.[aloha]` 시뮬레이션 익스트라, `.[feetech]` = SO-101 모터).

### B2. LeRobot 시뮬레이션(gym) — 로봇 없이 sim
- **gym-pusht**(2D 밀기), **gym-aloha**(양팔 조작 MuJoCo): `pip install -e ".[pusht]"` / `".[aloha]"`. **Mac에서 CPU/MPS로 구동.** 데이터셋 replay·정책 eval·시각화 가능.
- **gym_hil (HIL-RL, MuJoCo Franka Panda 큐브 집기)**: https://huggingface.co/docs/lerobot/en/hilserl_sim — `pip install -e ".[hilserl]"`. 태스크 `PandaPickCubeKeyboard-v0` 등. ⚠️ 문서상 **RL 학습엔 Nvidia GPU 요구** 명시(렌더/텔레옵 자체는 Mac MuJoCo로 가능).

### B3. HF Robotics Course (무료, 개념→실습)
- **링크**: https://huggingface.co/learn/robotics-course/unit0/1
- **내용**: 고전 로보틱스 → 학습기반 → LeRobot 실습 → SOTA. 유닛당 30~45분 자율진도. **우리 커리큘럼 큐레이션의 원본.**

## C. NVIDIA GR00T × LeRobot (모델 후훈련) — 심화

- **Isaac GR00T in LeRobot**: https://huggingface.co/blog/nvidia/nvidia-isaac-gr00t-in-lerobot
- **GR00T N1.5 SO-101 튜닝**: https://huggingface.co/blog/nvidia/gr00t-n1-5-so101-tuning
- **IsaacLab-Arena에서 정책 평가**: https://huggingface.co/blog/nvidia/generalist-robotpolicy-eval-isaaclab-arena-lerobot · 문서 https://isaac-sim.github.io/IsaacLab-Arena/
- **우리 연결**: Red Light Green Light(음성→정지)까지 가면 VLA/정책 학습 단계에서 참고. 지금 단계(세팅)에선 읽기만.

## D. 커뮤니티 / 참고

- **Seeed: GR00T N1.5 파인튜닝 → Jetson Thor 배포**: https://wiki.seeedstudio.com/fine_tune_gr00t_n1.5_for_lerobot_so_arm_and_deploy_on_jetson_thor/
- **Isaac Lab에서 SO-100 큐브 리프팅(skrl RL)** — Medium: https://medium.com/@kabilankb2003/training-so-100-robot-for-cube-lifting-in-isaac-lab-from-simulation-to-intelligent-control-with-9e81f94c6d6e
- **로보틱스 gym 실험기(개인 블로그)**: https://www.tinystruggles.com/posts/robotics_gyms_and_experiments/
- **SO-101 오픈소스 키트 리뷰**: https://thinkrobotics.com/blogs/product-reviews-buying-guides/thinkrobotics-lerobot-so-101-6-axis-robotic-arm-review-ai-ready-open-source-and-built-for-learning

---

## 요약 표 — 무엇을 어디서 돌리나

| 경로 | SO-101 sim? | OS | GPU | 우리 지금 쓸모 |
|---|---|---|---|---|
| A1 NVIDIA 공식 학습경로 | ✅ | Linux | RTX(고사양) | 커리큘럼 논리·목차 뼈대 |
| A2 Workshop(Docker) | ✅ | Linux only | RTX 6000/5090급 | 클라우드 GPU에서 재현 |
| A3 LeIsaac+Seeed | ✅ | Ubuntu 22.04 | RTX 3080↑ | SO-101 sim 최단 경로(Linux 있으면) |
| B1/B2 LeRobot gym | ❌(Panda/pusht) | **macOS OK** | 불필요 | **오늘 Mac에서 툴체인 익히기** |
| B3 HF Course | 개념 | 무관 | 무관 | 커리큘럼 원본 |

---

## 관련 (Related)
- [[00_sim-setup-before-pat-me|시뮬 세팅 튜토리얼]]
- [[hardware-and-simulation|하드웨어/시뮬 가이드]]
- [[00-foundations|기초 지도]]
