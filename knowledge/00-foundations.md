# Physical AI 기초 지식 지도 (입문자용)

> 왜 이 문서? The Construct(ROS)나 NVIDIA/LeRobot 코스를 들으면 맥락이 안 잡히는 건 당신 탓이 아니다 —
> 그 코스들은 **당신이 이미 가졌다고 가정하는 멘탈 모델**을 안 알려주기 때문. 그 지도를 여기서 먼저 그린다.
> 목표: 용어와 큰 그림을 잡아서, 어떤 코스를 들어도 "아 이건 그 층 얘기구나"가 되게.

---

## 0. 가장 중요한 한 장 — 로봇을 움직이는 두 세계

로봇 소프트웨어에는 **두 개의 큰 세계**가 있고, 코스마다 어느 쪽인지 안 밝혀서 헷갈린다.

| | 🅰 고전 로봇공학 (ROS 세계) | 🅱 학습 기반 (Physical AI 세계) |
|---|---|---|
| 사고방식 | **사람이 규칙을 프로그래밍** ("이 각도로 가라") | **AI가 시연에서 배움** ("이렇게 하는 걸 보여줘") |
| 핵심 도구 | **ROS/ROS2**, Gazebo, MoveIt | **LeRobot**, Isaac, GR00T, MuJoCo |
| 대표 강좌 | **The Construct**, 대학 로봇공학 | HF LeRobot, NVIDIA Physical AI |
| 잘하는 것 | 정밀 제어, 산업/연구 로봇, 안전 | 잡기·조작 등 "규칙으로 못 짜는" 것 |
| 개발 비유 | 손으로 짠 **if/else 로직** | **머신러닝 모델** 학습 |

> **당신의 위치**: 우리 [[product-concept|제품 컨셉]]의 미션(토닥토닥→pick&place→Red Light)은 **🅱 학습 기반**에서 시작한다.
> The Construct는 **🅰 ROS 세계**라, 지금 당장 다 이해할 필요 없다. (나중에 제어가 필요해지면 그때 ROS.)
> 둘은 경쟁이 아니라 **층이 다름** — ROS는 "로봇의 운영체제/배선", 학습은 "로봇의 뇌".

---

## 1. 스택을 층으로 (아래→위)

로봇은 이 층들이 쌓인 것. 코스는 보통 한두 층만 다룬다.

```
⑥ 학습/정책   ← "무엇을 할지" AI가 결정 (imitation/RL, VLA, GR00T)      🅱
⑤ 시뮬레이션  ← 실물 없이 연습 (Gazebo / Isaac / MuJoCo)
④ 미들웨어    ← 부품끼리 메시지 주고받는 배선 (ROS/ROS2)                🅰
③ 제어        ← 모터를 실제로 얼마나 돌릴지 (kinematics, PID)
② 펌웨어/드라이버 ← 모터·센서와 직접 통신
① 하드웨어    ← 팔, 모터(actuator), 센서, 그리퍼(end-effector)
```

- The Construct = 주로 **④ ROS + ③ 제어 + ⑤ 시뮬**.
- 우리(LeRobot) = 주로 **⑥ 학습 + ⑤ 시뮬**, 하드웨어는 ①(SO-101).
- **핵심**: 층이 다르면 용어도 다르다. "맥락이 안 온다" = 대개 다른 층 얘기를 듣고 있어서.

---

## 2. 용어 사전 (층별 — 이것만 알면 90% 뚫림)

### ① 하드웨어
- **DOF (자유도, Degrees of Freedom)**: 관절이 독립적으로 움직이는 축의 수. SO-101 = **6-DOF**(사람 팔과 비슷).
- **Actuator / Servo (액추에이터/서보모터)**: 관절을 움직이는 모터. SO-101은 Feetech 서보.
- **End-effector (엔드이펙터)**: 팔 끝의 도구 — 보통 **그리퍼(집게)**.
- **Teleoperation (텔레오퍼레이션/teleop)**: 사람이 **리더 팔**을 손으로 움직이면 **팔로워 팔**이 따라함 → 이게 학습 데이터가 됨.

### ③ 제어 / 기구학
- **Kinematics (기구학)**: 관절 각도 ↔ 손끝 위치의 수학.
  - **Forward(정기구학)**: 관절 각도 → 손끝 어디? (쉬움)
  - **Inverse(역기구학, IK)**: 손끝을 여기 두려면 관절을 몇 도? (어려움, 로봇의 핵심 문제)
- **PID 제어**: "목표에 부드럽게 도달"시키는 고전 제어 공식.

### ④ 미들웨어 — ROS
- **ROS / ROS2 (Robot Operating System)**: OS가 아니라 **로봇 부품들이 메시지를 주고받는 배선/규약**. 산업·연구 표준.
  - **Node(노드)**: 하나의 작은 프로그램(예: 카메라 노드, 모터 노드).
  - **Topic(토픽)**: 노드들이 주고받는 **메시지 채널**(예: `/camera/image`). pub/sub 구조.
  - 개발 비유: **마이크로서비스 + 메시지 큐**. 노드=서비스, 토픽=Kafka 채널.
- **URDF**: 로봇의 생김새(관절·링크)를 적은 **XML 명세**. 시뮬레이터가 이걸 읽어 로봇을 그림.
- **MoveIt**: ROS의 모션 플래닝(경로 계획) 라이브러리.

### ⑤ 시뮬레이션
- **Gazebo**: ROS 세계의 대표 물리 시뮬레이터.
- **MuJoCo**: 가볍고 빠른 물리엔진 (Mac에서도 돔 — LeRobot이 여기 얹힘).
- **Isaac Sim / Isaac Lab (NVIDIA)**: 고사양 GPU용 사실적 시뮬 + RL 대량학습. (Mac 불가 — `hardware-and-simulation.md` 참조)
- **Sim-to-Real (심투리얼)**: 시뮬에서 배운 걸 **실물로 옮기는** 것. 시뮬과 현실의 차이(sim-to-real gap)가 난제.

### ⑥ 학습 / 정책
- **Policy (정책)**: "이 상황에서 무슨 동작을 할지"를 정하는 **AI 모델**. 로봇의 뇌.
- **Imitation Learning (모방학습)**: 사람 시연(teleop 데이터)을 **따라 배우는** 방식. LeRobot의 기본.
- **Reinforcement Learning (강화학습, RL)**: 시행착오 + 보상으로 배우는 방식. 시뮬에서 대량으로.
- **VLA (Vision-Language-Action) 모델**: **눈(카메라)+말(지시)+행동(모터)** 을 한 모델로. 로봇계의 "파운데이션 모델".
- **GR00T (NVIDIA)**: 대표적 로봇 파운데이션 모델(VLA). LeRobot에서 파인튜닝 가능.
- **LeRobot (Hugging Face)**: 데이터 수집·학습·평가를 묶은 **오픈소스 로봇 학습 프레임워크**. 우리 스택의 중심.
- **Dataset (데이터셋)**: teleop으로 모은 (영상+관절값+행동) 기록. 정책은 이걸로 배움.

---

## 3. "You are here" — 학습 순서 제안

당신은 입문자니, **🅱 학습 세계 + 시뮬 우선**으로 간다. ROS는 필요해질 때.

1. **개념**: 이 문서 + [HF Robotics Course Unit 0](https://huggingface.co/learn/robotics-course/unit0/1) (큰 그림).
2. **손으로**: `lab/tutorials/00_sim-setup-before-pat-me.md` — Mac에서 LeRobot+MuJoCo 돌려보기.
3. **개념 보강**: 위 용어사전에서 막히는 단어를 그때그때 찾기.
4. **The Construct는 나중에**: 제어·ROS가 궁금해질 때. 그때는 "④⑤층 강좌구나" 하고 들으면 들어옴.

---

## 4. The Construct가 이제 왜 안 들어왔는지 (요약)
- 그건 **🅰 ROS 세계, ③④⑤층** 강좌다. **노드·토픽·URDF·Gazebo**를 당연히 안다고 가정한다.
- 우리가 지금 하는 건 **🅱 학습 세계, ⑤⑥층**(LeRobot·정책·teleop). **용어도 목표도 다르다.**
- 그래서 "맥락이 안 온다"가 정상. 위 지도를 옆에 두고 들으면 **"아 이건 미들웨어 얘기"** 로 정리된다.

## 참고 (입문 친화)
- [HF Robotics Course](https://huggingface.co/learn/robotics-course/) · [LeRobot](https://github.com/huggingface/lerobot)
- [ROS2 공식 튜토리얼](https://docs.ros.org/en/rolling/Tutorials.html) (🅰 세계 궁금할 때)
- 우리 문서: `lab/references/index.md` (튜토리얼 모음) · `lab/hardware-and-simulation.md` (장비/시뮬)

---

## 관련 (Related)
- [[06-robot-learning-ladder|로봇 러닝 사다리]] — 🅱 학습 세계를 한 단계 깊게 (RL→모방→VLA)
- [[01-job-market-ros-vs-physical-ai|잡마켓: ROS vs Physical AI]]
- [[02-robot-industry-landscape|로봇 산업 지형]]
- [[03-physical-ai-players-and-money|플레이어와 돈]]
- [[00_sim-setup-before-pat-me|시뮬 세팅 튜토리얼]]
- [[hardware-and-simulation|하드웨어/시뮬 가이드]]
