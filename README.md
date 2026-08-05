# portfolio-jyp

**JYP ENTERTAINMENT 지원용 포트폴리오** (1순위 ONE Label 콘텐츠 마케팅 / 2순위 STUDIO J SNS 마케팅)

[portfolio-casefile](https://github.com/wonjeongju/portfolio-casefile)을 **그대로 가져와 문구만 바꾼** 회사별 버전이다.
구조·디자인·케이스 구성은 손대지 않는다. 새로 만들지 않는다.

## 원본에서 바꾼 것

| 구분 | 원본 | 이 버전 |
|---|---|---|
| 직무 라벨 | AE 케이스 파일 / AE 지원 / AE Case File | 콘텐츠 마케팅 케이스 파일 / **JYP ENTERTAINMENT 콘텐츠 마케팅 지원** / Case File |
| 직무 정의 문장 | "AE의 역할은…" | "콘텐츠 마케터의 역할은…" |
| 단독 강조 | "혼자 키운 2.6만", "대행사 없이 혼자", "구현 단독", "개인 단독" | 전부 제거 — **혼자·단독·개인 성과를 강조하지 않는다** |

## 제출물

- **URL** — https://wonjeongju.github.io/portfolio-jyp/
- **파일** — `dist/주원정_포트폴리오_JYP.pdf` (A4)

## PDF 만드는 법

```bash
python3 -m http.server 8899 &
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="dist/주원정_포트폴리오_JYP.pdf" \
  --virtual-time-budget=15000 http://localhost:8899/
```

### 인쇄 CSS에서 조심할 것 (`style.css` 맨 아래 `@media print`)

실제로 사고가 났던 지점들이라 건드리기 전에 읽을 것.

1. **`button.zoom`을 숨기면 안 된다.** 증거 스크린샷이 이 버튼 안에 들어 있어서, 숨기면 폰 목업 화면이 통째로 하얗게 비어 나온다.
2. **`* { transform: none }`을 걸면 안 된다.** 폰 목업 두 대가 transform으로 겹쳐 있어서, 초기화하면 뒤 기기가 앞 기기에 완전히 가려 화면이 빈다.
3. **스크롤 구동 애니메이션(`animation-timeline: view()`)은 반드시 죽여야 한다.** 안 그러면 케이스가 opacity 0인 채로 인쇄돼 지면이 빈다.
4. 페이지 경계는 `break-before: page`로 **케이스 단위로 못 박아** 어중간한 여백을 없앤다.

### 지면 미리보기 (PDF 뷰어 캡처가 안 될 때)

`@media print` 블록을 `@media screen`으로 바꾼 CSS 사본을 만들고, `body{width:188mm}`(A4 − 좌우 여백)로 두면 브라우저에서 지면을 그대로 눈으로 볼 수 있다.

## 제출 전 점검

- [ ] https://wonjeongju.github.io/portfolio-jyp/ 접속 확인
- [ ] PDF 열어서 페이지 넘김·빈 지면 확인
- [ ] 수치 대조: 팔로워 2.6만 / **받은 좋아요·찜 16.2만**(누적 좋아요 아님) / 협업 100건 이상 / 좋아요 **7,833**(저장 포함 9,600) / 대만 구독자 **9,500명**(1만 아님)
- [ ] 470만은 **채널 수치** — "제가 제안한 시리즈가 채널 누적 470만" 식으로만. "단독 성과가 아니다" 같은 부정문은 쓰지 않는다
