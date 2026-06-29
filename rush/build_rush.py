#!/usr/bin/env python3
"""Build 'The Morning Rush' static pages from markdown sources.

Reads every rush/src/morning-rush-YYYY-MM-DD.md and renders:
  rush/<date>.html   - one page per edition
  rush/index.html    - latest edition inline + archive of all editions
Self-contained: no external dependencies. Non-destructive to the rest of the repo.
"""
import re, html
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
SITE_SECTION = "/rush"

CSS = """
*{box-sizing:border-box}
body{margin:0;background:#f5f3ee;color:#1a1a1a;
  font-family:Georgia,'Times New Roman',serif;line-height:1.62;}
.wrap{max-width:680px;margin:0 auto;padding:32px 22px 64px;}
.nav{font-family:-apple-system,Segoe UI,Roboto,sans-serif;font-size:13px;
  letter-spacing:.04em;text-transform:uppercase;color:#8a7f6a;margin-bottom:24px;}
.nav a{color:#8a7f6a;text-decoration:none;border-bottom:1px solid #d8cfb8;}
.nav a:hover{color:#1a1a1a;}
h1{font-size:30px;letter-spacing:.5px;margin:0 0 4px;line-height:1.15;}
h2{font-size:21px;margin:30px 0 6px;line-height:1.2;}
h3{font-size:18px;margin:28px 0 6px;}
p{font-size:17.5px;margin:0 0 16px;}
.tagline{font-style:italic;color:#6b6256;font-size:15px;margin:0 0 4px;}
.meta{font-weight:bold;font-size:14px;color:#3a3530;
  font-family:-apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.02em;}
hr{border:none;border-top:1px solid #d8cfb8;margin:26px 0;}
a{color:#7a5c1e;}
.archive{list-style:none;padding:0;margin:8px 0 0;}
.archive li{padding:9px 0;border-bottom:1px solid #e3dcc9;font-size:17px;}
.archive a{text-decoration:none;border-bottom:1px solid transparent;}
.archive a:hover{border-bottom:1px solid #7a5c1e;}
.archive .d{font-family:-apple-system,Segoe UI,Roboto,sans-serif;font-size:13px;
  color:#8a7f6a;display:inline-block;min-width:64px;}
footer{margin-top:42px;font-size:13px;color:#8a7f6a;
  font-family:-apple-system,Segoe UI,Roboto,sans-serif;}
"""

def inline(t):
    t = html.escape(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', t)
    return t

def md_to_html(md):
    out, para = [], []
    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()
    for raw in md.splitlines():
        line = raw.rstrip()
        s = line.strip()
        if not s:
            flush(); continue
        if s == "---":
            flush(); out.append("<hr>"); continue
        if s.startswith("### "):
            flush(); out.append("<h3>" + inline(s[4:]) + "</h3>"); continue
        if s.startswith("## "):
            flush(); out.append("<h2>" + inline(s[3:]) + "</h2>"); continue
        if s.startswith("# "):
            flush(); out.append("<h1>" + inline(s[2:]) + "</h1>"); continue
        para.append(s)
    flush()
    return "\n".join(out)

def page(title, body, is_index=False):
    nav = ('<div class="nav"><a href="/">&larr; AI Daily Brief</a></div>' if is_index
           else '<div class="nav"><a href="%s/">&larr; The Morning Rush</a> &middot; <a href="/">AI Daily Brief</a></div>' % SITE_SECTION)
    return f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><style>{CSS}</style></head>
<body><div class="wrap">{nav}
{body}
<footer>The Morning Rush &middot; a daily brief on AI in medicine and the world it's moving through.</footer>
</div></body></html>"""

def parse(md):
    d = {"issue": None, "weekday": None}
    m = re.search(r'Issue\s+(\d+)', md)
    if m: d["issue"] = m.group(1)
    return d

def main():
    eds = []
    for f in sorted(SRC.glob("morning-rush-*.md")):
        m = re.match(r'morning-rush-(\d{4}-\d{2}-\d{2})\.md', f.name)
        if not m: continue
        date = m.group(1)
        md = f.read_text()
        meta = parse(md)
        body = md_to_html(md)
        (ROOT / f"{date}.html").write_text(page("The Morning Rush — " + date, body))
        dt = datetime.strptime(date, "%Y-%m-%d")
        eds.append({"date": date, "dt": dt, "issue": meta["issue"], "body": body})
    eds.sort(key=lambda e: e["date"], reverse=True)
    if not eds:
        print("No editions found in rush/src/"); return
    latest = eds[0]
    items = []
    for e in eds:
        label = e["dt"].strftime("%a %d %b %Y")
        iss = f"Issue {e['issue']}" if e["issue"] else "Edition"
        items.append(f'<li><span class="d">{e["dt"].strftime("%d %b")}</span> '
                     f'<a href="{SITE_SECTION}/{e["date"]}.html">{label} — {iss}</a></li>')
    archive = ('<h2>Archive</h2><ul class="archive">' + "\n".join(items[1:]) + "</ul>"
               if len(items) > 1 else "")
    idx_body = latest["body"] + ("<hr>" + archive if archive else "")
    (ROOT / "index.html").write_text(page("The Morning Rush", idx_body, is_index=True))
    print(f"Built {len(eds)} edition(s); latest {latest['date']} (Issue {latest['issue']}).")

if __name__ == "__main__":
    main()
