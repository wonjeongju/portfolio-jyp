# portfolio-jyp

주원정 — **JYP ENTERTAINMENT 지원용 포트폴리오** (1순위 ONE Label 콘텐츠 마케팅 / 2순위 STUDIO J SNS 마케팅)

기존 [portfolio-casefile](https://github.com/wonjeongju/portfolio-casefile)이 "판단 서사" 중심이라면,
이 버전은 공고의 **"지원자 본인의 작업물이 담긴 포트폴리오"** 요구에 맞춰 **숏폼 실물**을 앞세운다.
디자인 언어(형광펜 + 종이, Pretendard)는 기존 사이트를 그대로 잇는다.

---

## 배포

GitHub Pages로 올린다.

```bash
# 1) GitHub에 portfolio-jyp 저장소를 만든 뒤
git remote add origin https://github.com/wonjeongju/portfolio-jyp.git
git branch -M main
git push -u origin main
```

그다음 저장소 **Settings → Pages → Source: Deploy from a branch → main / (root)** 로 설정.
1~2분 뒤 `https://wonjeongju.github.io/portfolio-jyp/` 에서 열린다.

지원서에는 이 주소를 붙인다.

---

## 제출 전 점검

- [ ] `https://wonjeongju.github.io/portfolio-jyp/` 접속 확인
- [ ] 샤오홍슈 링크 3개가 아직 살아 있는지 클릭 확인
      (앱 공유 링크에는 만료 토큰 `xsec_token`이 붙어 있어 시간이 지나면 죽을 수 있다.
       죽었으면 앱에서 다시 "공유 → 링크 복사"해서 `index.html`의 `xhslink.cn` 주소를 교체)
- [ ] 특수문자 깨짐 확인: `思念`, `种草`, `×`
- [ ] 자소서 수치와 일치하는지 대조

## 수치 표기 규칙 (master DB 기준 — 바꾸지 말 것)

| 항목 | 정확한 표기 | 금지 |
|---|---|---|
| 샤오홍슈 계정 지표 | **받은 좋아요와 찜 16.2만** (2026.08 기준, 합계) | "누적 좋아요 16.2만" |
| 올리브영 추천템 | **좋아요 7,833 / 저장 포함 9,600** | "9,600 likes" 단독 |
| 팔로워 | 2.6만 (2026.07 기준) | — |
| 브랜드 협업 | 100건 이상 (미집계) | 정확한 건수 단정 |
| 개인 유튜브 | 최고 도달 구독자 9,500명 | "1만 명" 반올림 |

---

## 알려진 제약

**KNN 수상작 영상은 현재 유튜브 임베드가 막혀 있다** (오류 153 — 퍼가기 비활성).
지금은 세로 포스터 + 링크아웃으로 처리했다.

페이지 안에서 바로 재생시키려면:
1. YouTube 스튜디오 → 해당 영상 → 수정 → **고급 설정 → "퍼가기 허용" 체크**
2. `index.html`의 `<a class="feature__player">` 블록을 주석에 적힌 `<iframe>`으로 교체

**개인 유튜브 채널 영상은 내려간 상태**라 링크를 걸지 않았다. 이력에 수치만 기재.

**샤오홍슈는 외부 사이트 임베드를 지원하지 않는다.** 원본 게시물 링크로만 연결 가능.
캡처 이미지를 추가하면 링크가 죽어도 증거가 남으므로, 여유가 되면
게시물 화면(좋아요·저장 수가 보이게) 캡처를 `assets/`에 넣고 각 항목에 붙이면 좋다.

---

## 구조

```
index.html                 단일 페이지
style.css                  토큰 + 레이아웃 (기존 케이스파일 디자인 언어 상속)
assets/knn-poster.jpg      KNN 수상작 세로 포스터 (유튜브 oardefault 1080x1920 원본)
assets/guidebook/          F1 팝업 캠페인 제휴 가이드북 이미지
```
