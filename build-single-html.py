#!/usr/bin/env python3
"""index.html을 단일 HTML 제출본으로 묶는다.

CSS·JS·이미지를 전부 한 파일에 넣어 어디서 열어도 그대로 보이게 만든다.
디자인은 건드리지 않는다 — 원본 style.css/script.js를 그대로 삽입할 뿐이다.

  python3 build-single-html.py   →   dist/주원정_포트폴리오_JYP.html
"""
import re, os, base64, mimetypes

mimetypes.add_type("image/webp", ".webp")

SITE = "https://wonjeongju.github.io/portfolio-jyp/"
OUT = "dist/주원정_포트폴리오_JYP.html"

html = open("index.html", encoding="utf-8").read()

# 1) CSS / JS 인라인 (내용 무수정)
css = open("style.css", encoding="utf-8").read()
js = open("script.js", encoding="utf-8").read()
html = html.replace('<link rel="stylesheet" href="./style.css" />', "<style>\n" + css + "\n</style>")
html = re.sub(r'<script[^>]*src="\./script\.js"[^>]*></script>', "<script>\n" + js + "\n</script>", html)


def data_uri(path: str) -> str:
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()


# 2) 이미지 → data URI (src, 라이트박스용 data-full 둘 다)
refs = sorted(set(re.findall(r'(?:src|data-full)="\./([^"]+)"', html)))
inlined = 0
for ref in refs:
    if os.path.exists(ref) and not ref.endswith((".js", ".css")):
        html = html.replace(f'"./{ref}"', '"' + data_uri(ref) + '"')
        inlined += 1

# 3) 케이스 상세 링크는 라이브 주소로 — 단일 파일에서는 상대경로가 깨진다
html = re.sub(
    r'href="\./((?:case|work|workflow)[^"]*\.html)"',
    lambda m: f'href="{SITE}{m.group(1)}" target="_blank" rel="noopener"',
    html,
)
html = html.replace('<link rel="canonical" href="./index.html" />', f'<link rel="canonical" href="{SITE}" />')
# 파일로 열 때 뜨지 않을 OG 이미지 경로는 뺀다
html = re.sub(r'<meta (?:property="og:image"|name="twitter:image") content="[^"]*" />', "", html)

os.makedirs("dist", exist_ok=True)
open(OUT, "w", encoding="utf-8").write(html)

left = len(re.findall(r'(?:src|href)="\./', html))
print(f"이미지 {inlined}개 인라인 / 남은 상대경로 {left}개")
print(f"{OUT} — {os.path.getsize(OUT) / 1024 / 1024:.2f} MB")
