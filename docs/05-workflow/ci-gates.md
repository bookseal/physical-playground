# CI 게이트 — 리뷰어가 없을 때, 검사가 리뷰어다

> **대상:** CI를 처음 붙여보는 사람.
> **한 줄:** `deploy.yml`은 **main에 도착한 것을 배포**하고, `ci.yml`은 **무엇이 main에
> 도착해도 되는지를 결정**한다. 전자는 실행, 후자는 게이트다.
>
> 관련: [GitHub 워크플로 표준](github-workflow.md) · [배포 & CD](../04-ops/deployment.md) ·
> [CD 구멍 메우기 기록](../engineering/cd-and-public-playbook.md)

---

## 0. CI와 CD는 다르다

가장 먼저 정리할 혼동. 둘 다 `.github/workflows/`에 있지만 **정반대 방향**을 본다.

| | 파일 | 언제 | 무엇을 |
|---|---|---|---|
| **CI** (Continuous Integration) | `ci.yml` | **머지 전** — PR이 열릴 때 | "이거 들여보내도 되나?" **묻는다** |
| **CD** (Continuous Deployment) | `deploy.yml` | **머지 후** — main에 push되면 | "들어왔으니 배포한다" **실행한다** |

```
   PR 열림 ──▶ [CI: 검사] ──✅──▶ 머지 ──▶ main ──▶ [CD: 배포] ──▶ 라이브
                   │
                   ❌  머지 버튼이 잠긴다
```

CD만 있고 CI가 없으면, **깨진 코드도 그냥 배포된다.** 어제까지 우리가 그랬다.

---

## 1. 우리에게 CI가 특히 중요한 이유

### ① 리뷰어가 없다

1인 개발에서는 **GitHub이 자기 PR을 자기가 승인하는 걸 금지**한다.
그래서 "승인 1개 필수"를 켜면 영원히 머지할 수 없다.

> **리뷰어 자리가 비어 있다. CI가 그 자리에 앉는다.**

### ② 이 레포는 곧 배포물이다

보통의 프로젝트에서 "커밋"은 그냥 코드 저장이다. **우리는 다르다.**

서버가 `git reset --hard origin/main`으로 체크아웃을 만들고, 파드가 **그 폴더를 그대로 서빙**한다.
즉 **"git에 추적된다" = "인터넷에 공개된다"** 가 같은 말이다.

파일 하나가 실수로 커밋되는 건 스타일 문제가 아니라 **릴리스**다.
그래서 우리 CI의 첫 번째 검사는 테스트가 아니라 **"공개해도 되는 것만 들어왔는가"** 다.

### ③ 실제로 오늘 필요했다

무드보드 작업에서 저작권 자료(Re-Volt 스크린샷)가 새어나가지 않았는지
**내가 손으로 `git check-ignore`를 돌려 확인**했다. 사람이 매번 기억해야 하는 검사는
언젠가 반드시 빠뜨린다. **그게 바로 CI가 해야 할 일이다.**

---

## 2. 우리가 붙인 검사 7개

`.github/workflows/ci.yml`

| # | 검사 | 무엇을 막나 |
|---|---|---|
| 1 | **공개 가능성** (`ops/ci/check-publishable.sh`) | 저작권 자료·개인 문서·8MB 초과 파일이 git에 들어오는 것 |
| 2 | **문서 링크** (`ops/ci/check-links.py`) | 공개 플레이북의 깨진 상대 링크 (= 방문자가 보는 404) |
| 3 | **파이썬 컴파일** | 파드를 재시작해야만 터지는 문법 오류 |
| 4 | **셸 문법** | `deploy.sh`가 배포 도중 죽는 것 |
| 5 | **k8s 매니페스트** (`kubeconform`) | 클러스터가 머지 후에야 거절할 잘못된 YAML |
| 6 | **`READ_ONLY` 존재** | 공개 사이트의 쓰기 API가 열리는 것 |
| 7 | **시크릿 스캔** (gitleaks) | 토큰·키가 공개 레포에 박히는 것 |

### 6번을 특히 봐라 — 문서보다 강한 방어

`k8s/site.yaml`의 `READ_ONLY: "1"`이 없으면, 공개 사이트의 `/api/save`가
**아무나 문서를 덮어쓸 수 있는 엔드포인트**가 된다.

문서에 "지우지 마세요"라고 쓸 수도 있다. 하지만 **문서는 안 읽힌다.**
CI는 **안 읽힐 수가 없다.** 지우는 순간 빌드가 깨진다.

> **불변 조건(invariant)은 주석이 아니라 검사로 표현하라.**
> 이게 "테스트를 쓴다"는 말의 진짜 의미에 가깝다.

---

## 3. 좋은 CI의 원칙 — 우리가 지킨 것

### ① 로컬에서 똑같이 돌아가야 한다

```bash
ops/ci/check-publishable.sh      # CI가 돌리는 바로 그 스크립트
python3 ops/ci/check-links.py    # 똑같다
```

CI 안에만 존재하는 검사는 **재현할 수 없고, 재현할 수 없으면 고칠 수 없다.**
"CI에서만 깨지는데 왜인지 모르겠다"는 말이 나오는 순간 그 CI는 죽는다.

그래서 우리는 **검사를 스크립트로 뽑아 레포에 두고**, 워크플로는 그걸 호출만 한다.
워크플로 YAML은 *언제 돌릴지*만 정하고, *무엇을 검사할지*는 스크립트가 안다.

### ② 우리가 통제할 수 없는 것으로 실패하지 마라

링크 검사는 **외부 http(s) 링크를 검사하지 않는다.** 남의 사이트가 잠깐 죽었다고
우리 PR이 빨간불이 되면 안 된다.

> **가끔 이유 없이 실패하는 CI는, 사람들이 무시하는 법을 배우는 CI다.**
> 그 순간 게이트로서의 가치가 0이 된다. 신뢰성 > 커버리지.

### ③ 빨라야 한다

머지 버튼 앞에서 10분을 기다리게 하면 사람은 우회로를 찾는다.
우리 검사는 전부 합쳐 1분 미만이다 — 빌드도, 테스트 스위트도, 클러스터 접속도 없다.

### ④ CI에 프로덕션 권한을 주지 마라

k8s 검사는 **클러스터에 접속하지 않는다.** kubeconfig도 자격증명도 없다.

> 배포 권한 없이 배포물을 검증한다. CI가 털려도 클러스터는 안전하다.
> (배포 권한은 `deploy.yml`의 forced-command 키 하나에만 있고, 그 키는
> 배포 스크립트 하나만 실행할 수 있다.)

#### ⚠️ 함정: `kubectl apply --dry-run=client`는 오프라인이 아니다

**이 CI의 첫 실행이 바로 여기서 실패했다.** 나는 "`--dry-run=client`니까 클러스터가
필요 없다"고 믿었고, 그렇게 워크플로를 짜고 **이 문서에도 그렇게 썼다.** 둘 다 틀렸다.

```
error validating "k8s/site.yaml": failed to download openapi:
Get "http://localhost:8080/openapi/v2?timeout=32s": connection refused
```

이름과 달리, `--dry-run=client`는 **스키마 검증을 위해 클러스터의 OpenAPI를
다운로드하려 한다.** 클러스터가 없으면 실패한다. `--validate=false`를 붙이면 통과하지만,
그건 **스키마 검증을 꺼버리는 것** — YAML 파싱만 남아 검사 가치가 거의 사라진다.

그래서 **`kubeconform`**을 쓴다. 스키마를 내장하고 있어 **진짜로 오프라인**이다.

> **이게 "CI가 스스로를 검증한다"의 실물이다.**
> 내 잘못된 가정이 문서와 코드 양쪽에 들어갔는데, **CI가 그걸 잡았다.**
> 사람 리뷰어였다면 놓쳤을 것이다 — 그럴듯했으니까.

### ⑤ 검사는 실패해야 의미가 있다

**절대 실패하지 않는 검사는 검사가 아니라 장식이다.**
붙이기 전에 물어라 — *"이게 실제로 무엇을 잡아본 적 있나?"*

우리 7개는 전부 **오늘 실제로 일어난 사고**에서 나왔다:
저작권 파일 누출 위험, `READ_ONLY` 삭제 위험, 매니페스트 무시,
`deploy.sh` 문법, 문서 링크. 가상의 위험이 아니다.

---

## 4. CI가 잡지 **못하는** 것 — 정직하게

CI를 붙였다고 안전해진 게 아니다. 오늘 겪은 버그 두 개는 **이 CI를 통과했을 것이다.**

| 오늘의 버그 | CI가 잡았나 | 왜 |
|---|---|---|
| `HOST` 환경변수를 선언만 하고 안 씀 → 파드 Ready 실패 | ❌ | **문법적으로 완벽한 파이썬**이다 |
| webp가 `application/octet-stream`으로 나감 | ❌ | 코드는 정상. **환경(alpine)이 다른 것** |

두 버그의 공통점: **문법이 아니라 행동(behavior)의 문제**다.
정적 검사로는 절대 못 잡는다. 잡으려면 **실제로 띄워서 요청을 보내봐야** 한다.

### 다음 단계 — 스모크 테스트

```yaml
# 아직 없음. 이런 모양이 될 것:
- name: The server actually serves
  run: |
    READ_ONLY=1 PORT=8799 python3 viewer/server.py &
    sleep 2
    curl -sf localhost:8799/ | grep -q "Physical Spark"        # 랜딩이 뜨나
    curl -sf localhost:8799/docs | grep -q "Playbook"          # 플레이북이 뜨나
    test "$(curl -s -o /dev/null -w '%{http_code}' -X POST localhost:8799/api/save)" = 403
    test "$(curl -s -o /dev/null -w '%{content_type}' localhost:8799/raw?path=design%2F_refs%2Fgen-1.webp)" = image/webp
```

이 4줄이 있었다면 **오늘 버그 두 개를 다 잡았다.**
`HOST` 버그는 컨테이너에서만 터지니 완전하진 않지만, MIME 버그는 확실히 잡힌다.

> **교훈: "컴파일된다"와 "동작한다"는 다른 질문이다.**
> 정적 검사는 싸고 빠르지만 얕다. 진짜 게이트는 **실제로 굴려보는 것**이다.

---

## 5. 브랜치 보호 — 검사를 "게이트"로 만들기

**검사가 돌기만 하면 게이트가 아니다.** 빨간불인데도 머지 버튼이 눌리면 아무 의미가 없다.
지금 우리 상태가 정확히 그렇다 — CI는 돌지만 **`main` 보호가 꺼져 있어서**, 실패한 PR도
머지할 수 있고 `main`에 직접 push도 된다. 이 절을 따라 켜면 비로소 게이트가 된다.

> **이건 GitHub 웹 설정이라 코드로 안 된다.** 레포 소유자(창님)가 직접 눌러야 한다.
> Claude는 대신 못 켠다 — 그래서 순서를 하나하나 적는다.

### 켜는 법 — 클릭 경로 (약 2분)

1. 레포 → **Settings** 탭 → 왼쪽 **Branches** →
   **Add branch ruleset** (또는 구식 UI면 *Add branch protection rule*).
   - 요즘 GitHub은 **Rulesets**가 기본이다. 아래는 Ruleset 기준.
2. **Ruleset Name**: `main` (아무 이름이나 되지만 알아보기 쉽게).
   **Enforcement status**: **Active** — 이걸 안 켜면 규칙이 "기록만 하고 안 막는다".
3. **Target branches** → *Add target* → **Include default branch**
   (= `main`을 자동으로 가리킨다. 브랜치명을 오타낼 일이 없다).
4. **Rules** 체크박스를 아래 표대로 켠다.

| 규칙 | 값 | 왜 |
|---|---|---|
| **Require a pull request before merging** | ✅ | `main` 직접 push 차단. 모든 변경이 PR을 거친다 |
| └ Required approvals | **0** | ⚠️ **함정** — 아래 설명 |
| **Require status checks to pass** | ✅ | **이게 진짜 게이트** |
| └ 검사 선택 | **`checks`**, **`secret scan`** | 아래 "정확한 이름" 참고 |
| └ Require branches to be up to date | ✅ | 낡은 브랜치가 통과했다 머지 후 `main`을 깨는 것 방지 |
| **Block force pushes** | ✅ | 히스토리 보호 (Ruleset은 기본으로 켜져 있다) |

5. 맨 아래 **Create** (또는 *Save changes*).

### ⚠️ 함정 1 — Required approvals는 반드시 **0**

가장 많이 하는 실수다. "리뷰 필수니까 1"로 켜는 순간 —

> **GitHub은 자기 PR을 자기가 승인하는 걸 금지한다.**
> 1인 레포에서 1로 켜면 **아무도 승인할 수 없어 영원히 머지 불가**가 된다.

승인은 0으로 둔다. **리뷰어의 빈자리는 사람이 아니라 status check가 채운다.**
(나중에 기여자가 합류하면 그때 1로 올리면 된다.)

### ⚠️ 함정 2 — `deploy`를 필수 검사로 고르지 마라

status check 목록에는 **`checks` · `secret scan` · `deploy`** 세 개가 뜬다.
`deploy`는 **CD**다 — `main`에 들어온 *뒤* 도는 배포. 이걸 "머지 전 필수"로 걸면
논리가 뒤집힌다("배포돼야 머지 가능"). **`checks`와 `secret scan`만** 고른다.

> 검사 이름이 목록에 안 보이면, 그 워크플로가 **아직 한 번도 안 돈** 것이다.
> PR을 한 번 열어 CI를 돌리면 이름이 등록되고, 그때 고를 수 있다.
> (그래서 브랜치 보호는 CI를 먼저 붙인 *다음에* 켠다 — 순서가 중요하다.)

### 켜졌는지 확인 — 일부러 뚫어본다

설정은 "저장했다"가 아니라 "실제로 막나"로 확인한다.

```bash
# main에 직접 push가 막히나?
echo "test" >> README.md && git commit -qam "test: should be blocked"
git push origin main
#  → ! [remote rejected] main -> main (protected branch hook declined)  이러면 성공
git reset --hard @~1      # 되돌리기
```

막히면 게이트가 살아있는 것이다. 통과되면 3번(Enforcement: Active)이나
1번(Require a pull request)을 다시 확인한다.

> API로도 볼 수 있다: `gh api repos/OWNER/REPO/rulesets`.
> 규칙이 하나도 없으면 `[]` — 지금 우리가 그 상태다.

### 켠 뒤 달라지는 것

- `main`에 직접 커밋 → **거부**된다. 브랜치를 파고 PR을 열어야 한다.
- CI 빨간불인 PR → **머지 버튼이 회색**으로 잠긴다.
- 이게 오늘 내가 두 번 저지른 "브랜치 착각하고 main에 push" 사고를
  **구조적으로 불가능**하게 만든다. 사람의 습관이 아니라 시스템이 막는다.

---

## 6. 실패했을 때 — 읽는 법

```
✗ publishable check FAILED
  ✗ Re-Volt screenshots are tracked — these must stay local:
      design/_refs/rv-toyworld.webp
```

우리 검사는 **무엇이 왜 틀렸고 어떻게 고치는지**를 한 화면에 말하도록 썼다.
`Error: exit code 1`만 뱉는 검사는 사람을 GitHub 로그 속으로 밀어 넣는다.

**고칠 땐 로컬에서 같은 스크립트를 돌려라.** CI를 다시 돌리며 추측하지 말고.

```bash
ops/ci/check-publishable.sh     # 여기서 초록불이면 CI에서도 초록불
```

---

## ✅ 지금 남은 일 (이 문서를 읽는 창님에게)

CI는 붙었고 돌고 있다. **하지만 게이트는 아직 안 잠겼다.** 남은 건 클릭 두 번이다.

- [ ] **§5를 따라 `main` 브랜치 보호를 켠다** — 지금은 실패한 PR도 머지되고
      `main` 직접 push도 된다. Settings → Branches → Add branch ruleset.
- [ ] status check는 **`checks`와 `secret scan`만**. `deploy`는 고르지 마라(§5 함정 2).
- [ ] Required approvals는 **0**(§5 함정 1).
- [ ] 켠 뒤 §5의 "일부러 뚫어본다"로 실제로 막히는지 확인.

이 두 가지가 끝나면, 다음 계층은 **스모크 테스트**(§4) — 오늘의 `HOST`·MIME 버그처럼
"컴파일은 되는데 동작은 안 하는" 버그를 잡는 층이다.

---

## 요약

1. **CI는 게이트, CD는 실행기.** 하나는 묻고 하나는 한다.
2. **혼자면 CI가 리뷰어다.** 승인 필수는 켜지 마라 — 자기 PR은 자기가 승인 못 한다.
3. **이 레포는 배포물이다.** 커밋 = 공개. 그래서 첫 검사가 "공개해도 되는가"다.
4. **불변 조건은 주석이 아니라 검사로 써라.** `READ_ONLY` 검사가 문서보다 강하다.
5. **로컬에서 못 돌리는 검사는 죽는다.** 워크플로는 스크립트를 호출만 하게.
6. **가끔 실패하는 CI는 무시당한다.** 신뢰성이 커버리지보다 중요하다.
7. **"컴파일된다" ≠ "동작한다".** 정적 검사는 얕다 — 다음은 스모크 테스트다.
