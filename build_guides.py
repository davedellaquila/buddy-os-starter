#!/usr/bin/env python3
"""Render the human guides (START-HERE.md, TESTING.md) as web pages.

The markdown files are the sources of truth; start-here.html and
testing.html are generated from them so the reading surface can never
drift from the repo documents. Re-run after editing either guide:

    python3 build_guides.py        (requires the 'markdown' package)

SETUP.md is deliberately NOT rendered: it stays in the repo as the
executable guide for the user's Muse.
"""
import sys

try:
    import markdown
except ImportError:
    sys.exit("build_guides.py needs the 'markdown' package: pip install markdown")

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__ — Buddy OS Starter</title>
<style>
:root { color-scheme: light dark; --ink:#1d2733; --muted:#5b6b7c; --bg:#fdfcfa; --card:#ffffff; --line:#e3ded4; --accent:#0f6f5c; }
@media (prefers-color-scheme: dark) {
  :root { --ink:#e8e4da; --muted:#a7a294; --bg:#16181d; --card:#1e2126; --line:#33363d; --accent:#5ec9ae; }
}
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--ink);
  font:17px/1.65 -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }
header.site { border-bottom:1px solid var(--line); background:var(--card); }
header.site .in { max-width:760px; margin:0 auto; padding:14px 22px; display:flex; gap:18px; align-items:baseline; flex-wrap:wrap; }
header.site .brand { font-weight:700; letter-spacing:.02em; }
header.site nav a { color:var(--muted); text-decoration:none; margin-right:14px; }
header.site nav a.here { color:var(--accent); font-weight:600; }
main { max-width:760px; margin:0 auto; padding:28px 22px 56px; }
h1 { font-size:30px; line-height:1.25; margin:0 0 18px; }
h2 { font-size:22px; margin:34px 0 10px; }
h3 { font-size:18px; margin:26px 0 8px; }
a { color:var(--accent); }
code { background:var(--card); border:1px solid var(--line); border-radius:5px; padding:0 5px; font-size:.92em; }
hr { border:none; border-top:1px solid var(--line); margin:30px 0; }
footer { max-width:760px; margin:0 auto; padding:0 22px 40px; color:var(--muted); font-size:14px; }
</style>
</head>
<body>
<header class="site"><div class="in">
  <span class="brand">🧭 Buddy OS Starter</span>
  <nav>__NAV__</nav>
</div></header>
<main>
__BODY__
</main>
<footer>Generated from __SRC__ — edit the markdown, not this page.
Buddy OS Starter is MIT-licensed; your copy of it is yours.</footer>
</body>
</html>
"""

GUIDES = [
    ("START-HERE.md", "start-here.html", "Start Here"),
    ("TESTING.md", "testing.html", "Testing Guide"),
]

def render(src, out, title):
    text = open(src, encoding="utf-8").read()
    body = markdown.markdown(text)
    # The guides cross-link as markdown; on the web they link as pages.
    body = body.replace('href="START-HERE.md"', 'href="start-here.html"')
    body = body.replace('href="TESTING.md"', 'href="testing.html"')
    nav = "".join(
        '<a href="%s"%s>%s</a>' % (o, ' class="here"' if o == out else "", t)
        for _, o, t in GUIDES)
    page = (TEMPLATE.replace("__TITLE__", title).replace("__NAV__", nav)
            .replace("__BODY__", body).replace("__SRC__", src))
    open(out, "w", encoding="utf-8").write(page)
    print("wrote %s (%d bytes)" % (out, len(page)))

if __name__ == "__main__":
    for src, out, title in GUIDES:
        render(src, out, title)
