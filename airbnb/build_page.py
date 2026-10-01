"""Build the GitHub Pages copy of the Airbnb visualizer.

airbnb/visualizer.html is page content without a document skeleton (it is also published as a Claude
artifact, which adds its own). This wraps it into a full document at docs/airbnb/index.html.

    python3 airbnb/build_page.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "airbnb" / "visualizer.html"
OUT = ROOT / "docs" / "airbnb" / "index.html"

HEAD = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Step-through animations for 8 high-frequency Airbnb interview problems.">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
"""


def main():
    body = SRC.read_text()
    split = body.index("<div class=\"wrap\">")          # everything before it belongs in <head>
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(HEAD + body[:split] + "</head>\n<body>\n" + body[split:] + "\n</body>\n</html>\n")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
