# 잡마켓 — ROS vs Physical AI (커리어 관점)

> 질문: "ROS 쪽이 클까, Physical AI 쪽이 클까?" 데이터로 본 답. 조사일 2026-07-07 (출처 링크).
> 요약: **ROS = 안정적 기반기술(nice-to-have), Physical AI/ML = 성장 엣지·최고 수요·최고 희소성.**
> [기초 지도](00-foundations.md)의 🅰(ROS)/🅱(학습) 두 세계를 커리어 렌즈로 다시 본 것.

---

## 한 장 요약

| | 🅰 ROS/고전 로봇공학 | 🅱 Physical AI / 로봇 ML |
|---|---|---|
| 채용 포스팅 요구도 | 로봇 포지션의 **37%만** ROS 요구 (대개 "우대") | AI/ML·perception = **최고 수요, 뽑기 어려움** |
| 시장 성장 | ROS 시장 $243M(2026)→$2.12B(2034), **CAGR 31%** | embodied AI 시장 ~$4.44B(2025), **CAGR ~39%** |
| 성격 | 성숙·기반·필수 인프라 | 폭발 성장·프리미엄·인재 부족 |
| 최고 몸값 | — | **하이브리드**(하드웨어 ↔ 지능 SW를 잇는 사람) = 가장 귀함 |

출처: [robotics job market 분석](https://careersinrobotics.com/guides/most-in-demand-robotics-jobs) · [ROS 시장](https://www.intelmarketresearch.com/robot-operating-system-market-43598) · [로봇 커리어 가이드](https://research.com/careers/robotic-careers-a-guide-to-career-paths-options-and-salary)

---

## 1. 숫자로 본 로봇 엔지니어 시장
- **연봉**: 미국 평균 ~$101k(엔트리 ~$83k), 고급직 ~$144k. 중위 연봉 **2024 대비 +14%**. ([Glassdoor](https://www.glassdoor.com/Salaries/robotics-engineer-salary-SRCH_KO0,17.htm))
- **성장**: BLS, 로봇 엔지니어 **2032까지 +10%**(평균 이상). ([Coursera](https://www.coursera.org/articles/robotics-jobs))
- **핵심 스킬**: Python·C++ + **AI/ML·control·computer vision**. ([Research.com](https://research.com/careers/robotic-careers-a-guide-to-career-paths-options-and-salary))

## 2. ROS의 위치 — "필수는 아니지만, 사라지지도 않음"
- 로봇 포지션의 **37%만 ROS 명시**, 다수는 "우대사항". ROS 외 프레임워크(독점·대안)도 부상 중.
- 그런데 **ROS 시장 자체는 CAGR 31%로 큼** — 산업·물류 로봇의 사실상 표준 배선이라, **기반으로서 계속 필요**.
- 커리어 해석: ROS는 **"있으면 문 열리는 기본기"** — 로봇 SW로 밥 먹으려면 알아두면 좋지만, 그것만으론 차별화 약함.

## 3. Physical AI의 위치 — "성장은 여기, 인재는 부족"
- **가장 뜨거운 이동**: embodied AI(=physical AI) — ML 모델이 데이터가 아니라 **실제 세계의 로봇**을 제어. 시장 CAGR ~39%.
- 채용에서 **AI/ML·perception 인재는 고수요·고희소**. "하드웨어와 지능 SW를 잇는 **하이브리드 엔지니어**"가 가장 몸값 높음.
- "블루칼라 로보틱스" 직군도 등장 — **4년제 학위 없이도** 기술·정밀함으로 들어가는 역할. ([job market 분석](https://careersinrobotics.com/guides/most-in-demand-robotics-jobs))

## 4. 결론 — 그래서 어디로?
- **큰 쪽·빠른 쪽 = Physical AI**(성장·연봉·수요·희소성 전부). 단 **ROS는 죽지 않는 기반**이라, 이상적 조합은 **🅱를 주력 + 🅰를 교양**으로.
- **"하이브리드"가 정답**: 우리가 [기초 지도](00-foundations.md)에서 본 두 세계를 **둘 다** 아는 사람이 시장의 스윗스팟.

### 우리 프로젝트에의 함의
- 우리가 **Physical AI(LeRobot·VLA) 우선**으로 잡은 게 잡마켓 성장 방향과 정확히 일치 — 커리큘럼이 "취업되는 스킬"과 붙는다.
- 제품 서사에 쓸 한 줄: *"로봇계에서 가장 부족한 인재는 하드웨어와 AI를 잇는 사람. 우리는 그 다리를 놀이로 건너게 한다."*

---

## 관련 (Related)
- [[00-foundations|기초 지식 지도]]
- [[02-robot-industry-landscape|산업 지형]]
- [[03-physical-ai-players-and-money|플레이어와 돈]]
