# 문서에서 코드까지 — 이슈·PR·프로젝트로 굴리는 개발 흐름

> **대상:** 창업 프로세스 초심자. 혼자(혹은 둘이) 개발하지만
> **"팀이 하는 방식"을 지금부터 몸에 붙이고 싶은 사람.**
> **한 줄:** 우리가 쌓은 수십 개의 `.md`가 **의사결정의 근거**가 되고,
> 그 결정이 **이슈 → 브랜치 → PR → 머지 → 배포**를 거쳐 코드가 되는 한 바퀴.
>
> 관련: [배포 & CD](../04-ops/deployment.md) · [CD와 플레이북 공개 기록](../engineering/cd-and-public-playbook.md)

---

## 0. 지금 우리의 정직한 상태

| 항목 | 현재 | 평가 |
|---|---|---|
| 커밋 메시지 | `feat(site):`, `fix(viewer):`, `ci:`, `docs(deploy):` | ✅ **이미 업계 표준**(Conventional Commits) |
| 커밋 본문 | "무엇을"이 아니라 **"왜"**를 씀 | ✅ 아주 좋음 |
| 브랜치 | `main` 하나. 전부 직접 커밋 | ❌ |
| 이슈 | **0개** | ❌ |
| PR | **0개** | ❌ |
| 프로젝트 보드 | 없음 (`quali-fit`엔 있음) | ❌ |
| ADR (`decisions/`) | 2건 | 🟡 있지만 코드와 안 이어져 있음 |

**즉 재료는 다 있는데 흐름이 없다.** 문서는 문서대로, 코드는 코드대로 굴러간다.
둘을 잇는 게 이슈와 PR이다.

---

## 1. 혼자인데 왜 이슈와 PR을 쓰나?

가장 먼저 드는 의문이고, 정당한 의문이다.
**"내가 만들고 내가 머지하는데 리뷰가 무슨 의미냐?"**

솔직히 말하면 — **코드 리뷰로서의 가치는 거의 없다.** 다른 데 있다.

### ① 미래의 나에게 남기는 "왜"의 기록

6개월 뒤 `k8s/site.yaml`을 보다가 `READ_ONLY: "1"`을 발견한다.
"이거 왜 있지? 지워도 되나?" — **이 순간이 사고가 나는 순간이다.**

`git blame` → 커밋 → **PR** → 거기 붙은 이슈에 이렇게 쓰여 있다면:

> `/api/save`는 인증 없는 쓰기 엔드포인트다. 로컬(127.0.0.1)에선 안전하지만
> 공개 서버에선 아무나 문서를 덮어쓸 수 있다. 이 플래그가 유일한 방어선이다.

**지우지 않는다.** 커밋 메시지만으론 이 맥락을 담기 어렵다. PR은 담을 수 있다.

### ② 게이트 — 자동 검사가 통과해야만 머지

PR이 없으면 CI를 **강제**할 방법이 없다. "테스트 깨진 채로 main에 push" 가
구조적으로 불가능해진다.

### ③ 트랙션 — 이게 우리에겐 특히 크다

이 프로젝트의 목표는 [PnP 피칭 → 트랙션](../03-positioning/positioning-and-pitch.md)이다.
**공개 레포의 이슈와 PR은 그 자체로 "이 사람이 실제로 만들고 있다"는 증거물**이다.

- 커밋 20개 = "코드를 썼다"
- 이슈 20개 + PR 20개 = **"문제를 정의하고, 결정하고, 검증하며 만들었다"**

투자자·채용 담당자가 보는 건 후자다.
**building in public에서 'building'은 코드가 아니라 과정이다.**

### ④ 나중에 사람이 늘어날 때 (수강생·기여자)

기수제 학생이 풀이를 올리고 피어 리뷰를 하는 게 이 제품의 본질이다.
**우리가 먼저 그 방식으로 일하지 않으면, 그 문화를 가르칠 수 없다.**

---

## 2. 전체 흐름 — 한 바퀴

```
  ┌─ 참고 문서 (.md) ──────────────────────────────┐
  │  knowledge/   배경 지식 — 잘 안 변함             │
  │  docs/01-03   제품·시장·포지셔닝 — 전략           │
  │  decisions/   ADR — 되돌리기 어려운 선택          │
  │  docs/engineering/  어떻게 만들었나               │
  └────────────────────┬───────────────────────────┘
                       │ 인용·근거
                       ▼
                 ① Issue  ── "무엇을, 왜"
                       │        (라벨·프로젝트 보드에 올라감)
                       ▼
              (필요시) ADR 작성 ── 구조적 결정이면
                       │
                       ▼
                 ② Branch ── feat/read-only-viewer
                       │
                       ▼
                 ③ PR    ── "어떻게" + 검증 결과
                       │        "Closes #12"
                       ▼
                 ④ CI 통과 → Merge (squash)
                       │
                       ▼
                 ⑤ 배포 (자동) ── push to main → 라이브
                       │
                       ▼
                 ⑥ 문서 갱신 ── 배운 걸 다시 .md로
                       │
                       └──────► 다시 참고 문서가 된다 (순환)
```

**핵심은 ⑥이 ①로 되돌아간다는 것.** 문서가 코드를 낳고, 코드가 다시 문서를 낳는다.
이 순환이 없으면 문서는 죽고, 코드는 이유를 잃는다.

---

## 3. 각 단계 — 업계 표준은 이렇게 한다

### ① Issue — "해결책"이 아니라 "문제"를 쓴다

**초심자가 가장 많이 하는 실수:** 이슈에 해결책을 쓴다.

| ❌ 나쁜 이슈 | ✅ 좋은 이슈 |
|---|---|
| "deploy.sh에 kubectl apply 추가하기" | "매니페스트를 고쳐도 클러스터에 반영되지 않는다" |
| 해결책이 이미 정해짐 → 더 나은 방법을 못 찾음 | 문제를 정의 → 여러 해법을 비교할 수 있음 |

좋은 이슈의 구조:

```markdown
## 문제 (Problem)
k8s/site.yaml을 고쳐서 push해도 클러스터에 아무 일도 일어나지 않는다.
에러도 안 난다. 조용히 무시된다.

## 왜 중요한가 (Why)
가장 위험한 종류의 버그다 — 실패했다는 신호가 없다.
매니페스트를 신뢰할 수 없으면 인프라를 코드로 관리하는 의미가 없다.

## 근거 문서 (Context)
- docs/04-ops/deployment.md — 현재 배포 스크립트는 git pull + auth 빌드만 함

## 완료 조건 (Done when)
- [ ] 매니페스트를 고쳐 push하면 클러스터에 반영된다
- [ ] 손으로 클러스터를 만져도 다음 배포가 되돌린다
```

**"완료 조건(Acceptance Criteria)"이 있으면 이슈가 스스로 닫힐 때를 안다.**
이게 없는 이슈는 영원히 열려 있다.

### 라벨 — 최소한만

라벨은 늘리면 아무도 안 쓴다. **세 축**이면 충분하다.

| 축 | 라벨 | 용도 |
|---|---|---|
| **종류** | `bug` `feature` `docs` `infra` `research` | 무엇인가 |
| **영역** | `area:site` `area:auth` `area:robot` `area:curriculum` | 어디인가 |
| **크기** | `size:S` `size:M` `size:L` | 얼마나 걸리나 |

우선순위 라벨(`P0`/`P1`)은 **넣지 마라.** 프로젝트 보드의 순서가 곧 우선순위다.
라벨과 보드가 우선순위를 이중으로 관리하면 반드시 어긋난다.

### ② Branch — 이름에 의도를 담는다

```
feat/read-only-viewer       새 기능
fix/host-bind               버그 수정
docs/github-workflow        문서
chore/bump-ssh-agent        잡일
```

`main`에 직접 커밋하지 않는다. 이유는 단순하다 —
**되돌릴 수 있는 단위**를 만들기 위해서다. 브랜치는 "이 시도가 실패해도
main은 멀쩡하다"는 보험이다.

> 여러 AI 에이전트를 병렬로 굴린다면 브랜치별 폴더 격리가 필요하다.
> → [git worktree 문서](../engineering/multi-agent-git-worktrees.md)

### ③ Commit — 이미 잘하고 있다

우리는 이미 **Conventional Commits**를 쓰고 있다.

```
<type>(<scope>): <제목 — 명령형, 소문자, 마침표 없음>

<본문 — "무엇을"이 아니라 "왜". 코드는 무엇을 하는지 이미 보여준다.>
```

`type`: `feat` `fix` `docs` `ci` `refactor` `test` `chore`

**왜 이 형식이 표준이 됐나:** 기계가 읽을 수 있다.
`feat`/`fix`만 모아 자동으로 CHANGELOG를 만들고, 버전을 올릴 수 있다.

> **우리 규칙:** 문서는 한국어, 하지만 **git workflow(커밋 메시지·PR 설명·`.github/`)는
> 전부 영어.** 오픈소스 기여자와 협업자를 위한 것.

### ④ PR — "어떻게"와 "검증"

커밋이 *무엇을 왜* 라면, PR은 *전체 변경을 어떻게 검증했는가* 다.

```markdown
## What
Merge the docs playbook into the site process; expose it at /docs.

## Why
Building in public is the point, but the playbook was local-only.

Closes #12          ← 이 한 줄이 머지 시 이슈를 자동으로 닫는다

## How it was verified
- curl -X POST /api/save on the live server → 403, README unchanged
- 29 docs listed on the server vs 30 locally (CLAUDE.md is gitignored) ✓
- /courses/, /join.html, /api/auth/me → no regression

## Risk
/api/save is an unauthenticated write endpoint. READ_ONLY=1 is load-bearing.
```

**`Closes #12`** — GitHub이 인식하는 마법의 문구다.
PR이 머지되면 이슈가 자동으로 닫히고, 이슈와 코드가 영구히 연결된다.
(`Fixes`, `Resolves`도 동일)

**Draft PR** — 작업을 시작하자마자 PR을 연다(초안 상태로).
"지금 뭐 하고 있는지"가 공개되고, 스스로도 목표를 잃지 않는다.

### 머지 방식 — Squash를 기본으로

| 방식 | 결과 | 언제 |
|---|---|---|
| **Squash and merge** | PR의 커밋 여러 개 → **main에 1개** | ✅ 기본값으로 |
| Merge commit | 커밋 전부 보존 + 병합 커밋 | 큰 기능, 히스토리가 의미 있을 때 |
| Rebase and merge | 커밋 전부 보존, 병합 커밋 없음 | 잘 안 씀 |

**Squash를 쓰는 이유:** main의 히스토리가 "논리적 변경 하나 = 커밋 하나"가 된다.
`fix typo`, `wip`, `oops` 같은 커밋이 main을 더럽히지 않는다.
되돌리기(`git revert`)도 커밋 하나만 되돌리면 끝난다.

### ⑤ 브랜치 보호 — 1인 개발의 함정

`main`에 branch protection을 걸 때 **주의할 점이 있다.**

> **GitHub에서는 자기 PR을 자기가 승인(approve)할 수 없다.**
> "Require 1 approval"을 켜면 **혼자서는 영원히 머지할 수 없다.**

1인 개발의 올바른 설정:

| 설정 | 값 | 이유 |
|---|---|---|
| Require a pull request | ✅ | main 직접 push 차단 |
| Require approvals | ❌ **0** | 혼자면 자기 승인 불가 → 잠긴다 |
| Require status checks | ✅ | **이게 진짜 게이트** |
| Allow force push | ❌ | 히스토리 보호 |

**리뷰어가 없으니 CI가 리뷰어다.** 그래서 status check가 핵심이다.

### ⑥ 프로젝트 보드 — 이슈를 "언제 할지"로 바꾼다

이슈는 *무엇을* 정의하고, 보드는 *언제/지금 뭘* 정한다.

> **우리 보드는 이미 있다** → [프로젝트 보드 — 지금 어떻게 굴러가나](project-board.md).
> 실제 칸 구성·하루 흐름·지금 켜야 할 자동화까지 그 문서에 있다.

**GitHub Projects (v2)** — 무료, 레포와 자동 연결.

권장 필드:

| 필드 | 값 |
|---|---|
| **Status** | `Backlog` → `Ready` → `In progress` → `In review` → `Done` |
| **Size** | `S` / `M` / `L` |
| **Week** | 6주 프레임의 주차 (주1~주6) |

**자동화(Workflows)를 반드시 켜라** — Projects 설정에 내장돼 있다:

- 이슈가 열리면 → `Backlog`에 자동 추가
- PR이 열리면 → `In review`로 이동
- 이슈가 닫히면 → `Done`으로 이동

**손으로 카드를 옮기는 보드는 반드시 죽는다.** 자동화가 곧 생명이다.

> **Plane vs GitHub Projects:** `plane.bit-habit.com`을 자체 호스팅하고 있지만,
> 이 프로젝트는 **GitHub Projects를 권한다.** 이유는 하나다 —
> **공개 트랙션.** 이슈·PR·보드가 한 곳에 있어야 외부인이 과정을 볼 수 있다.
> Plane은 비공개 운영(개인 할 일, 로봇팔 주문 추적 등)에 쓰면 된다.

---

## 4. 우리 `.md`들의 지형도 — 어떤 문서가 무슨 역할인가

문서가 많아지면 **"어디에 뭘 써야 하지?"**가 문제가 된다. 우리 구조는 이렇다.

| 폴더 | 무엇 | 언제 쓰나 | 수명 |
|---|---|---|---|
| `knowledge/` | 배경 지식 (산업·시장·기술 지형) | 리서치했을 때 | **길다** — 잘 안 변함 |
| `docs/01-concept` | 제품이 무엇인가 | 제품 정의가 바뀔 때 | 길다 |
| `docs/02-market` | 시장·경쟁 | 리서치했을 때 | 중간 |
| `docs/03-positioning` | 우리는 누구인가·피칭 | 포지셔닝이 바뀔 때 | 중간 |
| `docs/04-ops` | 어떻게 운영하나 (배포 등) | 인프라가 바뀔 때 | **레퍼런스** — 계속 갱신 |
| `docs/05-workflow` | 어떻게 일하나 (이 문서) | 프로세스가 바뀔 때 | 레퍼런스 |
| `docs/engineering/` | 어떻게 만들었나 (설명·기록) | 뭔가 만들고 나서 | **불변** — 그때의 기록 |
| `decisions/` (ADR) | **되돌리기 어려운 선택과 그 이유** | 구조적 결정을 할 때 | **불변** |
| `lab/` | 직접 해본 실험 | 실험할 때 | 중간 |
| `logs/` | 시간순 작업 일지 | 수시로 | 불변 |

### 갱신 문서 vs 기록 문서 — 헷갈리면 안 된다

- **레퍼런스(`docs/04-ops`, `05-workflow`)** = **"지금 사실은 이렇다."**
  틀리면 **고친다.** 과거를 남기지 않는다. (과거는 git이 안다)
- **기록(`docs/engineering/`, `logs/`, `decisions/`)** = **"그때 이렇게 결정했다."**
  틀렸다고 고치지 않는다. **새 문서를 쓰고 이전 것을 supersede 한다.**

오늘 `deployment.md`(레퍼런스)는 **고쳤고**,
`cd-and-public-playbook.md`(기록)는 **새로 썼다.** 그 차이다.

### ADR — 언제 쓰나

**ADR(Architecture Decision Record)**은 "되돌리기 어려운 선택"을 기록한다.

이 질문에 하나라도 Yes면 ADR을 쓴다:

- 6개월 뒤의 내가 "왜 이렇게 했지?"라고 물을 것 같은가?
- 다른 합리적인 선택지가 있었는가?
- 되돌리는 데 하루 이상 걸리는가?

**오늘 ADR감이었던 것:**
"매니페스트를 매번 apply할 것인가, 바뀔 때만 할 것인가" —
자가 치유 vs 속도의 트레이드오프, 다른 선택지가 실재했고, 시스템 성격을 바꾼다.

**ADR감이 아닌 것:** "403이냐 404냐" — 5분이면 바꾼다. 커밋 메시지로 충분.

ADR 형식(우리 `decisions/`가 이미 따르는 것):

```markdown
# 0003. 배포 시 k8s 매니페스트를 매번 apply 한다

## Status
Accepted (2026-07-13)

## Context
매니페스트를 고쳐도 클러스터에 반영되지 않았다. 두 가지 선택지가 있었다.

## Decision
매번 무조건 apply 한다.

## Consequences
+ 자가 치유: 손으로 만진 클러스터가 git 상태로 되돌아온다
+ "파일이 진실"이라는 GitOps 사상을 도구 설치 없이 얻는다
− 매 배포마다 몇 초 추가, 로그가 조금 길어진다
```

---

## 5. 오늘 작업을 이 표준으로 다시 쓴다면

가장 이해가 빠른 방법이다. **오늘 실제로 한 일**을 표준 흐름에 얹어보자.

| 실제로 한 것 | 표준대로였다면 |
|---|---|
| "CD가 매니페스트를 무시한다" 발견 | **Issue #1** `infra` `size:S`<br>제목: "Manifest changes are silently ignored on deploy" |
| 매번 apply로 결정 | **ADR 0003** — 자가 치유 vs 속도 |
| `ops/deploy.sh` 작성 | 브랜치 `fix/apply-manifests-on-deploy` |
| main에 직접 push | **PR #2** `Closes #1` + 검증 로그 첨부 |
| — | CI 통과 → squash merge → 자동 배포 |
| viewer 공개 | **Issue #3** `feature` `area:site`<br>"Publish the playbook — building in public" |
| `/api/save` 위험 발견 | **Issue #4** `bug` — 별도 이슈로 분리!<br>"Unauthenticated write endpoint would be public" |
| READ_ONLY 구현 | 브랜치 `feat/read-only-viewer` → **PR #5** `Closes #3, #4` |
| HOST 바인딩 버그 | **Issue #6** `bug` → `fix/host-bind` → **PR #7** |
| 문서 정리 | `docs/deployment-and-workflow` → **PR #8** |

**얻는 것:** GitHub에 남는 8개의 이슈/PR = "이 사람이 문제를 정의하고
결정하고 검증하며 만들었다"는 **공개 증거**. 커밋 5개보다 훨씬 강력하다.

**그리고 오늘 진짜 겪은 사고 하나가 예방된다.**
나는 `git add -A`로 무관한 문서 2개를 엉뚱한 커밋에 딸려 넣었다.
브랜치와 PR이 있었다면 **머지 전 diff를 보는 순간** 잡혔을 일이다.

---

## 6. 1인 창업자가 **생략해도 되는 것**

업계 표준을 통째로 가져오면 **의식(ceremony)에 짓눌려 아무것도 못 한다.**
지금 단계에서 안 해도 되는 것들:

| 생략 | 이유 |
|---|---|
| 코드 리뷰 승인 필수 | 혼자면 구조적으로 불가능 (자기 승인 불가) |
| `CODEOWNERS` | 오너가 한 명 |
| 릴리스 태그·시맨틱 버저닝 | 배포가 곧 릴리스. 버전 번호를 볼 사람이 없다 |
| 스프린트·번다운 차트 | 6주 프레임이 이미 있다 |
| 모든 커밋에 이슈 번호 | 오타 수정에까지 이슈를 만들지 마라 |
| 이슈 템플릿 (초기엔) | 혼자면 형식보다 습관이 먼저 |

**규칙: 그 절차가 "미래의 나 또는 외부인에게 남는 기록"이 아니면 생략하라.**

---

## 7. 다음 단계 — 이렇게 시작한다

작게 시작한다. 한 번에 다 하려면 못 한다.

### 1주차: 이슈부터
- [ ] 라벨 세트 만들기 (종류 5개 + 영역 4개 + 크기 3개)
- [ ] **지금 머릿속에 있는 할 일을 전부 이슈로 옮긴다**
      (로봇팔 기종 선정, 과제1 수행, 무궁화꽃 프로토타입 …)
- [ ] 각 이슈에 **완료 조건** 한 줄씩

### 2주차: 보드
- [ ] GitHub Project 생성 (`Physical Spark 로드맵`)
- [ ] Status / Size / Week 필드
- [ ] **자동화 켜기** (이슈 열림 → Backlog, 닫힘 → Done)

### 3주차: 브랜치 + PR
- [ ] `main` 브랜치 보호 (PR 필수, **승인 0개**, status check 필수)
- [ ] 다음 기능부터 브랜치 → PR → squash merge
- [ ] PR에 `Closes #N` 습관화

### 그 다음: CI 게이트
현재 `.github/workflows/deploy.yml`은 **push 후 배포**만 한다.
PR 시점에 도는 **검사** 워크플로가 아직 없다. 붙일 만한 것:

- YAML 문법 검사 (`kubectl apply --dry-run=client`)
- `python3 -m py_compile viewer/server.py auth/*.py`
- gitleaks (이미 로컬 pre-commit에는 있음)
- 링크 체크 (`.md`의 깨진 상대 링크)

**이게 갖춰지면 "리뷰어 없는 PR"이 진짜 게이트가 된다.**

---

## 요약

1. **이슈는 해결책이 아니라 문제를 쓴다.** 완료 조건이 없으면 영원히 열려 있다.
2. **PR은 "왜"의 영구 보관소다.** 6개월 뒤의 내가 `READ_ONLY`를 지우려 할 때 막아준다.
3. **혼자면 CI가 리뷰어다.** 승인 필수는 켜지 마라 — 자기 PR은 자기가 승인 못 한다.
4. **손으로 옮기는 보드는 죽는다.** 자동화가 곧 생명.
5. **레퍼런스는 고치고, 기록은 남긴다.** 둘을 섞지 마라.
6. **공개 이슈와 PR은 트랙션이다.** building in public에서 building은 코드가 아니라 과정이다.
7. **의식에 짓눌리지 마라.** 미래의 나에게 남는 기록이 아니면 생략하라.
