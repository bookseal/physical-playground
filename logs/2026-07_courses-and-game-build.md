# 밤샘 빌드 로그 — 코스 + 게임 (overnight session)

> 창업자가 자는 동안 Claude가 자율로 빌드한 기록. 계획 → 시도 → 됨/안됨 → 결정을 남긴다.
> 아침에 읽는 용도. 커밋은 마일스톤마다, 안 되면 되돌릴 수 있게.

## 목표 (창업자 지시)
1. **코스들을 직접 만들기** — 동적으로 화려하게. 마지막 프로젝트 **"무궁화 꽃이 피었습니다"**(Red Light, Green Light)까지.
2. **게임을 적당히 즐길 수 있게** — 처음에 시선 끌고 빠지게. Re-Volt식 **미끄러지는 타이어 자국**.
3. 중간중간 commit, 안 되면 롤백. 시도 흔적을 .md로.

## 계획 (내 로드맵)
- **A. 서버 정적 서빙** — 뷰어가 `site/` 하위(courses 등)를 서빙하게 (GitHub Pages와 동일 동작).
- **B. 코스 엔진** — `site/courses/index.html`: JS 데이터 기반 동적 코스 앱. 해시 라우팅(#/m1), 진도 저장(localStorage), 화려한 웜 테마.
  - 3개 미션: (1) 토닥토닥 (2) pick&place (3) 무궁화꽃. 각: 히어로 → 배울 것 → 레벨/시간/장비 태그 → 레슨 스텝(개념+코드+체크포인트) → 진도바 → 다음.
  - 내용은 lab/tutorials·foundations·course-analysis에서 grounded. **v0 초안**임을 정직하게.
- **C. 랜딩 연결** — 미션 카드 → 코스 링크.
- **D. 게임 개선** — 타이어 스키드 자국(드리프트 트레일), 점수 juice, 시선 끌기. "적당히".
- **E. 로그·커밋·테스트** — 마일스톤마다 스샷+커밋, 이 로그 갱신.

## 진행 (append-only)
- [시작] 로그 생성 + 계획 확정. 다음: 서버 정적 서빙(A).
- [A ✅] server.py: 미지정 GET는 `site/<path>` 서빙 폴백(디렉토리는 index.html). `/courses/` 200 확인.
- [B ✅] 코스 앱 `site/courses/index.html` — JS COURSES 데이터 3미션, 해시라우팅(#/m1), 진도 localStorage,
  진도 링/바, 레슨 아코디언(개념+코드+copy+체크포인트), 토스트. 스샷으로 허브·m1 렌더 확인. **잘 됨.**
  - 시도/결정: 카드가 `<a>`라 제목이 링크색(빨강) 상속됨 → `.mcard h3{color:var(--fg)}`로 교정.
  - 정직성: 내용은 v0 초안. Mac에선 SO-101 sim 불가라 "모션 개념은 gym으로" note를 각 미션에 명시.
- [C ✅] 랜딩 미션카드 onclick→courses/#/mN, "Open the full curriculum" CTA, 히어로 버튼→courses/.
- [커밋] 여기까지 커밋. 다음: 게임 개선(D) — 타이어 스키드 자국 + juice.
