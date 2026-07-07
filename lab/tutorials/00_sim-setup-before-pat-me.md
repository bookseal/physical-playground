# 튜토리얼 00 — 시뮬레이션 세팅 ("나를 토닥여줘" 직전까지)

> 목표: **로봇팔을 아직 안 산 상태에서**, 시뮬레이션으로 physical AI 개발 환경을 끝까지 세팅한다.
> 이 문서는 "pat me(토닥토닥) 모션을 짜기 **직전**"에서 멈춘다 — 즉 팔이 sim 안에 떠서 움직일 준비가 된 상태까지.
> 원자료 모음: `lab/references/index.md`. 명령어는 버전에 따라 바뀔 수 있으니 각 단계의 **공식 링크로 교차확인**.

![SO-101 Sim-to-Real](https://github.com/isaac-sim/Sim-to-Real-SO-101-Workshop/raw/main/images/so101_banner.png)

---

## 0. 먼저 — 현실 점검 (당신은 Mac이다)

SO-101 팔을 **시뮬레이션 안에 띄우는** 유일한 길은 NVIDIA Isaac Lab 계열인데, 이건 전부 **Ubuntu Linux + NVIDIA RTX GPU 전용**이다. macOS에선 로컬로 안 돈다. 그래서 두 갈래로 나눈다:

| | Path A — Mac 로컬 | Path B — SO-101 sim |
|---|---|---|
| 뭘 하나 | HF LeRobot + MuJoCo gym(Panda/pusht)로 **툴체인 전체를 손에 익힘** | Isaac Lab/LeIsaac로 **진짜 SO-101을 sim에 띄워 teleop** |
| SO-101? | ❌ (대체 로봇으로 워크플로우만) | ✅ |
| 필요 | **당신 Mac 그대로** | Ubuntu + RTX 3080↑ (없으면 클라우드 GPU) |
| 언제 | **오늘 바로** | Linux/클라우드 준비되면 |

**추천 순서**: 오늘 **Path A**로 LeRobot 감을 잡는다 → 팔 살 때쯤 **Path B**(또는 실물)로 SO-101을 붙인다.
"pat me"는 SO-101 모션이라 최종적으론 Path B(또는 실물)에서 완성되지만, Path A에서 **동일한 개념(teleop·데이터셋·eval)**을 미리 다 익힐 수 있다.

---

## Path A — Mac에서 오늘 (LeRobot + MuJoCo)

> 근거: [LeRobot 설치 문서](https://huggingface.co/docs/lerobot/en/installation) — Apple Silicon 지원(MPS/CPU).

### A-1. 파이썬 환경
```bash
# miniforge(conda) 없으면 먼저 설치: https://conda-forge.org/download/
conda create -y -n lerobot python=3.12
conda activate lerobot
```

### A-2. LeRobot + 시뮬레이션 환경 설치
```bash
git clone https://github.com/huggingface/lerobot.git
cd lerobot
# 시뮬레이션 gym 환경(둘 다 Mac에서 CPU/MPS로 돎)
pip install -e ".[pusht,aloha]"
# (나중에 SO-101 실물 모터 붙일 때) pip install -e ".[feetech]"
```
> Apple Silicon은 영상 디코딩이 자동으로 `pyav` 폴백이라 `ffmpeg` 없어도 시작 가능.

### A-3. 설치 확인 (팔이 대신, Panda/pusht가 뜬다)
```bash
python -c "import gym_pusht, gymnasium as gym; print('pusht OK'); print(gym.envs.registry.keys().__len__(), 'envs registered')"
```
- 그다음 **데이터셋 시각화**나 **사전학습 정책 eval**로 sim 창을 실제로 띄워본다 —
  현재 CLI는 `lerobot-dataset-viz`, `lerobot-eval` 계열. 정확한 인자는
  [HF Robotics Course Unit 0](https://huggingface.co/learn/robotics-course/unit0/1)의 실습을 따라간다.
- 여기까지 오면 **"Mac에서 LeRobot 스택이 돈다"**가 증명된 것. teleop·기록·재생·평가의 개념이 손에 붙는다.

> 🟢 **Path A 도착점 = "pat me 직전"**: LeRobot 워크플로우 준비 완료. 남은 건 "이 팔을 좌우로 왕복시켜 등을 토닥이는 모션을 스크립트로 짜는 것" 하나 — 그건 다음 튜토리얼(01)에서, SO-101(Path B/실물)이 준비되면.

---

## Path B — SO-101을 시뮬레이션에 띄우기 (Linux + RTX)

> 근거: [Seeed × LeIsaac 위키](https://wiki.seeedstudio.com/simulate_soarm101_by_leisaac/) (RTX 3080↑ 권장, A2 워크숍보다 문턱 낮음).
> **GPU 없으면**: 클라우드 GPU(NVIDIA Brev, vast.ai, Lightning AI 등)에서 Ubuntu+RTX 인스턴스를 빌려 아래를 그대로.

### B-1. 환경 + Isaac Sim/Lab
```bash
conda create -n leisaac python=3.10 && conda activate leisaac
conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit
pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu118
pip install --upgrade pip
pip install 'isaacsim[all,extscache]==4.5.0' --extra-index-url https://pypi.nvidia.com
```

### B-2. Isaac Lab
```bash
git clone https://github.com/isaac-sim/IsaacLab.git
sudo apt install cmake build-essential
cd IsaacLab && git checkout v2.1.0 && ./isaaclab.sh --install && cd ..
```

### B-3. LeIsaac + SO-101 에셋
```bash
git clone https://github.com/LightwheelAI/leisaac.git && cd leisaac
pip install -e source/leisaac
pip install pynput pyserial deepdiff feetech-servo-sdk
```
- [LeIsaac releases](https://github.com/LightwheelAI/leisaac/releases/tag/v0.1.0)에서 에셋 다운 → `assets/`에 풀기.
  구조에 `robots/so101_follower.usd`, `scenes/kitchen_with_orange/scene.usd` 등이 있어야 한다.

### B-4. SO-101이 sim에 뜨고 움직인다 (= pat me 직전)
```bash
python scripts/environments/teleoperation/teleop_se3_agent.py \
    --task=LeIsaac-SO101-PickOrange-v0 \
    --teleop_device=keyboard \
    --num_envs=1 --device=cpu --enable_cameras
```
- 키보드: `b` 시작 · `n` 성공 리셋 · `r` 실패 리셋. (leader 팔 있으면 `--teleop_device=so101leader --port=/dev/ttyACM0`)
- **이 창에 SO-101이 떠서 키보드로 관절이 움직이면 세팅 끝.**

> 🟢 **Path B 도착점 = "pat me 직전"**: SO-101이 시뮬레이션 씬에 로드되고 teleop으로 움직인다.
> 남은 건 "오렌지 집기" 대신 **"좌우 왕복 토닥이기" 태스크/모션을 정의**하는 것 — 다음 튜토리얼(01).

---

## 다음 (튜토리얼 01 예고)
- **과제 1 "나를 토닥여줘"**: 위에서 준비된 팔로 **좌우 왕복 모션**을 스크립트/teleop으로 만들고, 그 시연을 **데이터셋으로 기록**한다.
- 세팅 중 막힌 지점은 전부 여기(또는 학습 로그)에 적는다 — 그게 우리 커리큘럼의 초안이 된다.

## 참고 (전체 목록은 `lab/references/index.md`)
- NVIDIA 공식 SO-101 학습경로: https://docs.nvidia.com/learning/physical-ai/sim-to-real-so-101/
- NVIDIA Workshop 코드(Docker, Linux): https://github.com/isaac-sim/Sim-to-Real-SO-101-Workshop
- LeRobot 설치/시뮬레이션: https://huggingface.co/docs/lerobot/en/installation
