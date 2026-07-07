# 포지셔닝 & 피치 — Value Proposition + Madlibs Pitch

> 스타트업 트레이닝 과정의 포지셔닝 실습을, 우리 프로젝트(**Physical Playground** — Physical AI 피어리뷰 학교)에
> 맞춰 푼 작업 기록.

---

## 💡 개발자를 위한 스타트업 용어 해설 (어원과 비유)

비즈니스 용어가 낯선 개발자를 위해 어원과 프로그래밍 비유로 풀어본 해설.

**1. Value Proposition (가치 제안)**
- **원어 뉘앙스**: *Value*(가치) + *Proposition*(제안). "네가 내 지갑을 열게 만들 만한 **결정적인 한 방을 제안해 봐**"라는
  뉘앙스. 단순한 '기능(Feature) 설명'이 아니라 '고객이 궁극적으로 얻는 혜택(Benefit)'을 증명하는 선언문.
- **개발 비유**: 제품의 **백엔드 비즈니스 로직(핵심 뼈대)**. "우리는 A라는 사람의 B라는 고통을 C라는 방법으로 해결한다"는
  엄밀한 논리 공식.

**2. Pitch / Madlibs Pitch (피치 / 빈칸 채우기 피칭)**
- **원어 뉘앙스**:
  - *Pitch*: 야구 투수가 공을 던지듯(pitch), 짧은 시간에 상대(투자자/고객)에게 아이디어를 빠르고 강렬하게 꽂는 행위. (예:
    엘리베이터 피치)
  - *Madlibs*: 미국에서 유명한 '빈칸 채우기 단어 놀이'. 즉 정해진 템플릿의 빈칸에 내 아이템 단어만 끼워 넣어 쉽고 빠르게
    완성하는 피칭 대본.
- **개발 비유**: 제품의 **프론트엔드 UI (발표 대본)**. 백엔드(Value Proposition)의 딱딱한 논리를 듣기 편하게 포장한 30초
  자기소개 대사.

**3. ICP (Ideal Customer Profile) vs BP (Buyer Persona)**
- **ICP (이상적 고객 프로필)**: 우리 제품을 가장 필요로 하고 돈을 지불할 확률이 높은 **고객 집단**의 조건.
  - **개발 비유**: `Class` (집단 템플릿). 예: "소프트웨어 개발자 집단".
- **BP (구매자 페르소나)**: *Persona*(고대 연극 배우의 가면)에서 유래. 타겟 집단 안에서 뽑아낸 **구체적인 가상의 1명**을
  실존 인물처럼(이름·나이·고민까지) 묘사한 것.
  - **개발 비유**: 특정 속성값을 가진 `Instance / Object` (개인). 예: "파이썬은 잘하지만 아두이노 선 연결하다 보드 태워먹은
    적 있는 30대 백엔드 개발자 김코딩".

---

## 숙제 A — Customer Value Proposition

**빈칸 틀:**

> For **[buyer persona]**, who **[pain point or goal]**, our **[product/service]** helps **[key benefit]**
> by **[how it works]**, unlike **[alternative or status quo]**.

### 우리 프로젝트 원재료 (빈칸에 쓸 부품들)

| 칸 | 우리가 가진 후보 |
|---|---|
| product/service | 저가 로봇팔 **미션 + 피어 리뷰 학습 플랫폼** (교재가 아니라 **학습 운영 OS**) |
| key benefit | 혼자서는 못 넘는 physical AI 진입 장벽을, **단계별 성취 + 동료 피드백**으로 넘게 함 |
| how it works | 로봇팔 미션(토닥토닥→pick&place→무궁화꽃) → 풀이 영상 업로드 → **피어 리뷰** → 좋아요 갤러리로 좋은 풀이가 위로 |
| unlike (대안) | ① 유튜브 튜토리얼(피드백 0, 완주 안 됨) ② 비싼 부트캠프(일회성·고가) ③ 완제품 교구(정답만 따라함, 기록 안 남음) |
| 차별점 | **피어 리뷰 + UGC 갤러리 + 축적 데이터** — 콘텐츠는 카피되지만 커뮤니티·기록은 카피 안 됨 |

### 후보 초안 (persona별로 달라진다 — 이게 핵심)

**초안 ①  persona = 커리어 전환 개발자 / physical AI 입문 취미러**
> **SaaS·웹은 익숙하지만 로봇·physical AI는 혼자 시작하기 막막한 개발자**에게,
> **"미래는 physical AI인데 하드웨어가 무섭고 혼자선 피드백이 없어 중간에 포기한다"** 는 고민이 있다면,
> 우리 **로봇팔 미션 + 피어 리뷰 학습 플랫폼**은 **실제로 로봇을 움직이는 단계별 성취와 동료의 피드백으로 완주하게** 돕는다.
> 방법은 **저가 로봇팔로 미션을 주고 → 풀이 영상을 올리고 → 서로 리뷰하고 → 좋아요로 좋은 풀이가 떠오르는 것**.
> **유튜브 튜토리얼이나 비싼 부트캠프와 달리, 실제로 굴러가는 코드와 동료 피드백이 기록으로 남는다.**

**초안 ②  persona = 초등 자녀를 둔 학부모**
> **AI 시대에 아이를 준비시키고 싶지만 "코딩학원이 진짜 미래 역량인지" 확신 못 하는 학부모**에게,
> 우리 플랫폼은 **아이가 진짜 로봇팔을 직접 움직여 "나를 토닥여줘" 같은 미션을 성공시키고, 또래의 풀이를 보고 배우는** 경험을 준다.
> **화면 안 코딩 앱이나 완제품 로봇 장난감과 달리, 실물 로봇 + 또래 커뮤니티 + 성장 기록이 남는다.**

> 두 초안의 **product/benefit/how는 거의 같고, persona와 pain point만 다르다.**
> → "누구에게 팔 것인가" 하나만 정하면 문장이 확정된다.

### 확정 — 개발자 persona로 좁힌 버전

> For **소프트웨어 개발 지식은 있지만 하드웨어·Physical AI 입문을 두려워하는 개발자**,
> who **Physical AI가 대세인 건 알지만 뭐부터 접근해야 할지 몰라 막막한** 이들에게,
> our **로봇팔 놀이터 플랫폼**은 **부담 없이 놀면서 자연스럽게 하드웨어에 대한 관심과 재미를 붙이도록** 돕는다,
> by **기본 로봇팔로 하는 재밌는 미션을 소개하고 서로 결과물을 자랑하며 피드백을 주고받게 함으로써**,
> unlike **혼자 하다 포기하게 만드는 단방향 튜토리얼이나 딱딱하고 비싼 기존 교육 과정**.

*(English)*
> For **software developers** who **know software but are intimidated by where to start with Physical AI
> and hardware**, our **robotics playground** helps them **overcome that fear and naturally build interest**
> by **introducing fun missions with a basic robot arm, where they play, share, show off, and get peer
> feedback**, unlike **dry one-way tutorials or stiff, expensive traditional courses**.

---

## 숙제 B — Madlibs Pitch

**빈칸 틀:**

> Hi, I'm **\<name\>**, and my company **\<company\>** — the problem I'm solving is **\<problem\>**. Our
> product **\<product\>** is designed for our target customer of **\<target customer\>**.

### 확정 (발표용)

> 안녕하세요, 저는 **이기찬**이고 제 프로젝트는 **Physical Playground** 입니다.
> 제가 푸는 문제는 **"저 자신을 포함한 수많은 소프트웨어 개발자들이 Physical AI가 미래인 건 알지만, 하드웨어가 막막하고
> 두려워 시작조차 못 하는 문제"** 입니다.
> 우리 제품은 **기본 로봇팔로 할 수 있는 재밌는 미션을 주고, 서로의 결과물을 공유·자랑하며 피드백을 주고받는 놀이터**이며,
> **스트레스 없이 재밌게 Physical AI에 입문하고 싶은 소프트웨어 개발자**를 위해 설계되었습니다.

*(English — for class)*
> Hi, I'm **Gichan Lee**, and my project is **Physical Playground**.
> The problem I'm solving: software developers *know* Physical AI is the future, but they're too
> **intimidated** by hardware to even start.
> Our product is a **playground** — you get a basic robot arm, tackle fun missions, and get peer feedback.
> It's designed for developers who want a **fun, stress-free way to break into Physical AI.**

---

## 포지셔닝 원칙 메모

- **A(밸류프롭) → B(피치)**: 피치는 밸류프롭을 입말로 줄인 것. A를 먼저 확정하면 B는 거의 자동으로 나온다.
- **고객을 좁혀라**: 초안 ①/② 둘 다 노리지 말 것. 하나로 좁혀야 persona 테스트가 가능하다. → 우리는 **①(개발자 입문자)** 로 확정.
- **피치는 테스트다**: 아무한테나(=randos) 말하지 말고, 우리 ICP/BP에게 던져 A/B 테스트한다. 초기 테스트 대상 = 개발자 커뮤니티(=우리와 닮은 사람들) 우선.
