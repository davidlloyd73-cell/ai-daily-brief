#!/usr/bin/env python3
"""
Build David's AI Daily Brief page from aidailybrief.ai machine-readable feeds.

Usage:
    python3 build.py            # build latest edition
    python3 build.py 2026-06-12 # build a specific date

Reads optional GP's-corner notes from notes/<date>.json:
    {"items": [{"title": "...", "body": "..."}]}

Outputs (in repo root, alongside this script):
    a/<date>.html   - permanent archive page
    index.html      - copy of the latest edition
    archive.html    - list of all editions
    data/editions.json - manifest
"""
import json
import sys
import urllib.request
from datetime import datetime
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://aidailybrief.ai"
SITE_URL = "https://davids-ai-brief.netlify.app"  # this site's own public URL (for RSS)

# "← All projects" pill — shows only when opened from the portfolio site (?nav=1)
BACK_PILL = """<a id="all-projects-link" href="https://things-we-have-built.netlify.app/"
   style="display:none;position:fixed;top:14px;left:14px;z-index:99999;
          font:600 14px/1 'Segoe UI',system-ui,sans-serif;color:#fff;
          background:rgba(0,0,0,0.6);padding:10px 16px;border-radius:999px;
          text-decoration:none;backdrop-filter:blur(6px);">&larr; All projects</a>
<script>
  if (new URLSearchParams(location.search).get('nav') === '1') {
    document.getElementById('all-projects-link').style.display = 'inline-block';
  }
</script>"""


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "davids-daily-brief/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


CSS = """
:root{--ink:#1a1a1a;--soft:#555;--faint:#888;--rule:#e2ddd3;--bg:#faf7f0;--card:#ffffff;
--accent:#0f6f5c;--accent2:#8a3324;--chip:#eee8da;}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Georgia,'Times New Roman',serif;background:var(--bg);color:var(--ink);
line-height:1.55;font-size:19px}
.wrap{max-width:760px;margin:0 auto;padding:28px 20px 60px}
header.mast{border-bottom:3px double var(--ink);padding-bottom:14px;margin-bottom:6px}
.kicker{font-family:Verdana,Arial,sans-serif;font-size:12px;letter-spacing:.18em;
text-transform:uppercase;color:var(--soft)}
h1.mast{font-size:34px;letter-spacing:.01em;margin-top:4px}
.dateline{font-family:Verdana,Arial,sans-serif;font-size:13px;color:var(--soft);
margin:10px 0 26px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:6px}
.dateline a{color:var(--accent)}
h2.ep{font-size:27px;line-height:1.25;margin-bottom:8px}
p.dek{color:var(--soft);font-style:italic;margin-bottom:8px}
.srcline{font-family:Verdana,Arial,sans-serif;font-size:12.5px;color:var(--faint);margin-bottom:30px}
.srcline a{color:var(--accent)}
section{margin-bottom:38px}
h3.sec{font-family:Verdana,Arial,sans-serif;font-size:13px;letter-spacing:.15em;
text-transform:uppercase;color:var(--accent2);border-bottom:1px solid var(--rule);
padding-bottom:6px;margin-bottom:16px}
.idea{background:var(--card);border:1px solid var(--rule);border-left:5px solid var(--accent);
padding:20px 22px;border-radius:4px}
.idea h4{font-size:22px;line-height:1.3;margin-bottom:10px}
.idea p{color:var(--soft);font-size:17.5px}
.take{padding:14px 0;border-bottom:1px solid var(--rule)}
.take:last-child{border-bottom:none}
.take h4{font-size:19px;margin-bottom:6px}
.take p{color:var(--soft);font-size:17px}
.other{background:var(--card);border:1px solid var(--rule);border-left:5px solid var(--accent2);
padding:20px 22px;border-radius:4px}
.other p{color:var(--soft);font-size:17.5px}
.other .srcnote{font-family:Verdana,Arial,sans-serif;font-size:12.5px;color:var(--faint);
margin-top:12px}
.other .srcnote a{color:var(--accent2)}
.truth{background:#f3f1ec;border:1px solid var(--rule);border-left:5px solid #4a4a4a;
padding:20px 22px;border-radius:4px}
.truth p{color:#3d3d3d;font-size:17.5px}
.nocounter{font-family:Verdana,Arial,sans-serif;font-size:13px;color:var(--faint);
font-style:italic;margin-bottom:38px}
.gp{background:#eef4f1;border:1px solid #cfe0d8;border-left:5px solid var(--accent);
padding:20px 22px;border-radius:4px}
.gp .gpnote{font-family:Verdana,Arial,sans-serif;font-size:12px;color:var(--faint);margin-bottom:14px}
.gp h4{font-size:19px;margin-bottom:5px}
.gp p{color:#3c4f48;font-size:17px;margin-bottom:14px}
.gp p:last-child{margin-bottom:0}
ul.heads{list-style:none}
ul.heads li{padding:9px 0;border-bottom:1px dotted var(--rule);font-size:18px}
ul.heads li a{color:var(--ink);text-decoration:none}
ul.heads li a:hover{color:var(--accent);text-decoration:underline}
.q{font-style:italic}
.attr{font-family:Verdana,Arial,sans-serif;font-size:13px;color:var(--faint)}
.tchip{display:inline-block;font-family:Verdana,Arial,sans-serif;font-size:11px;
background:var(--chip);border-radius:3px;padding:1px 7px;margin-left:8px;color:var(--soft);
vertical-align:2px}
.listen{background:var(--card);border:1px solid var(--rule);border-radius:4px;
padding:12px 16px;margin:0 0 26px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.listen-label{font-family:Verdana,Arial,sans-serif;font-size:13.5px;color:var(--accent2);
font-weight:bold;white-space:nowrap}
.listen audio{flex:1;min-width:220px;height:36px}
footer{border-top:3px double var(--ink);padding-top:14px;font-family:Verdana,Arial,sans-serif;
font-size:13px;color:var(--soft)}
footer a{color:var(--accent)}
@media(max-width:480px){body{font-size:17px}h1.mast{font-size:26px}h2.ep{font-size:22px}}
"""


def nugget_li(n):
    anchor = f"{n.get('canonical', SITE)}#{n['id']}" if n.get("id") else SITE
    chip = f"<span class='tchip'>{escape(n.get('ts',''))}</span>" if n.get("ts") else ""
    if n.get("type") == "quote":
        attr = f" <span class='attr'>— {escape(n.get('attribution',''))}</span>" if n.get("attribution") else ""
        return f"<li><a class='q' href='{escape(anchor)}'>&ldquo;{escape(n['headline'])}&rdquo;</a>{attr}{chip}</li>"
    return f"<li><a href='{escape(anchor)}'>{escape(n['headline'])}</a>{chip}</li>"


def render(ed, notes):
    date = ed["date"]
    nice = datetime.strptime(date, "%Y-%m-%d").strftime("%A %d %B %Y")
    canonical = ed.get("canonicalUrl", f"{SITE}/e/{date}")
    nuggets = ed.get("nuggets", [])
    for n in nuggets:
        n["canonical"] = canonical
    takes = [n for n in nuggets if n.get("type") == "take"]

    thesis = ed.get("thesis") or {}
    idea = ""
    if thesis:
        idea = f"""<section><h3 class='sec'>The One Idea</h3>
<div class='idea'><h4>{escape(thesis.get('headline',''))}</h4>
<p>{escape(thesis.get('sub',''))}</p></div></section>"""

    takes_html = ""
    if takes:
        items = "".join(
            f"<div class='take'><h4>{escape(t['headline'])}</h4><p>{escape(t['body'])}</p></div>"
            for t in takes)
        takes_html = f"<section><h3 class='sec'>NLW&rsquo;s Takes</h3>{items}</section>"

    # The Other Side / The Truth Beneath — from zitron/<date>.json (written daily by
    # the scheduled run, ONLY from material Zitron actually published; never invented)
    contrast_html = ""
    zpath = ROOT / "zitron" / f"{date}.json"
    z = json.loads(zpath.read_text()) if zpath.exists() else None
    if z and z.get("match"):
        nice_src = datetime.strptime(z["source_date"], "%Y-%m-%d").strftime("%-d %B")
        agetag = "" if z.get("same_day") else f" <em>(from {nice_src}&rsquo;s edition)</em>"
        contrast_html = f"""<section><h3 class='sec'>The Other Side</h3>
<div class='other'><p>{escape(z['other_side'])}</p>
<div class='srcnote'>Source: Ed Zitron, <a href='{escape(z['source_url'])}'>&ldquo;{escape(z['source_title'])}&rdquo;</a>,
{nice_src} {z['source_date'][:4]}{agetag}</div></div></section>
<section><h3 class='sec'>The Truth Beneath</h3>
<div class='truth'><p>{escape(z['truth_beneath'])}</p></div></section>"""
    elif z is not None:
        contrast_html = "<p class='nocounter'>No fresh counter-source this edition.</p>"

    gp_html = ""
    if notes and notes.get("items"):
        items = "".join(
            f"<h4>{escape(i['title'])}</h4><p>{escape(i['body'])}</p>"
            for i in notes["items"])
        gp_html = f"""<section><h3 class='sec'>GP&rsquo;s Corner</h3>
<div class='gp'><div class='gpnote'>Claude&rsquo;s notes on what today means for general practice
and the NHS — commentary, not from the podcast itself.</div>{items}</div></section>"""

    heads = "".join(nugget_li(n) for n in nuggets)
    heads_html = f"<section><h3 class='sec'>All Headlines, Briefly</h3><ul class='heads'>{heads}</ul></section>" if heads else ""

    listen = (ed.get("listen") or {}).get("all", "https://pod.link/1680633614")
    dur = f" &middot; {ed['durationMin']} min listen" if ed.get("durationMin") else ""

    audio_html = ""
    mp3 = ROOT / "audio" / f"{date}.mp3"
    if mp3.exists():
        mins = max(1, round(mp3.stat().st_size * 8 / 48000 / 60))  # 48 kbps estimate
        audio_html = f"""<div class='listen'><span class='listen-label'>&#9654; Listen — today&rsquo;s
brief ({mins} min)</span><audio controls preload='none' src='/audio/{date}.mp3'></audio></div>"""

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>David&rsquo;s AI Daily Brief — {escape(date)}</title>
<meta name="robots" content="noindex">
<link rel="alternate" type="application/rss+xml"
      title="David's AI Daily Brief" href="/feed.xml">
<style>{CSS}</style></head><body>{BACK_PILL}<div class="wrap">
<header class="mast"><div class="kicker">Distilled from The AI Daily Brief podcast</div>
<h1 class="mast">David&rsquo;s AI Daily Brief</h1></header>
<div class="dateline"><span>{nice}{dur}</span>
<span><a href="/archive.html">Archive</a> &middot; <a href="{escape(listen)}">Listen</a></span></div>
<h2 class="ep">{escape(ed.get('title',''))}</h2>
<p class="dek">{escape(ed.get('dek',''))}</p>
<p class="srcline">Source: <a href="{escape(canonical)}">{escape(canonical)}</a></p>
{audio_html}{idea}{contrast_html}{gp_html}{takes_html}{heads_html}
<footer>All editorial content &copy; <a href="{SITE}">The AI Daily Brief</a> (host: Nathaniel
Whittemore). This is a personal, non-commercial reading page assembled by Claude for David Lloyd,
using the podcast&rsquo;s own machine-readable feeds. GP&rsquo;s Corner is Claude&rsquo;s commentary.
Generated {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC.</footer>
</div></body></html>"""


def render_md(ed, notes):
    """Clean Markdown mirror of an edition - the plain-text version the llms.txt
    convention recommends offering agents alongside the HTML page."""
    date = ed["date"]
    nice = datetime.strptime(date, "%Y-%m-%d").strftime("%A %d %B %Y")
    canonical = ed.get("canonicalUrl", f"{SITE}/e/{date}")
    dur = f" · {ed['durationMin']} min listen" if ed.get("durationMin") else ""
    nuggets = ed.get("nuggets", [])

    L = []
    L.append("---")
    L.append(f"title: David's AI Daily Brief — {date}")
    L.append(f"date: {date}")
    L.append(f"source: {canonical}")
    L.append("note: Personal, non-commercial distillation of The AI Daily Brief"
             " podcast. GP's Corner is AI commentary, not from the podcast.")
    L.append("---")
    L.append("")
    L.append("# David's AI Daily Brief")
    L.append("")
    L.append(f"**{nice}{dur}**")
    L.append("")
    if ed.get("title"):
        L.append(f"## {ed['title']}")
        L.append("")
    if ed.get("dek"):
        L.append(f"_{ed['dek']}_")
        L.append("")
    L.append(f"Source: {canonical}")
    L.append("")
    if (ROOT / "audio" / f"{date}.mp3").exists():
        L.append(f"Audio: {SITE_URL}/audio/{date}.mp3")
        L.append("")

    thesis = ed.get("thesis") or {}
    if thesis:
        L.append("## The One Idea")
        L.append("")
        L.append(f"### {thesis.get('headline','')}")
        L.append("")
        L.append(thesis.get("sub", ""))
        L.append("")

    zpath = ROOT / "zitron" / f"{date}.json"
    z = json.loads(zpath.read_text()) if zpath.exists() else None
    if z and z.get("match"):
        nice_src = datetime.strptime(z["source_date"], "%Y-%m-%d").strftime("%-d %B %Y")
        L.append("## The Other Side")
        L.append("")
        L.append(z["other_side"])
        L.append("")
        L.append(f'Source: Ed Zitron, "{z["source_title"]}", {nice_src} — {z["source_url"]}')
        L.append("")
        L.append("## The Truth Beneath")
        L.append("")
        L.append(z["truth_beneath"])
        L.append("")

    if notes and notes.get("items"):
        L.append("## GP's Corner")
        L.append("")
        L.append("_Claude's notes on what today means for UK general practice and the"
                 " NHS - commentary, not from the podcast itself._")
        L.append("")
        for i in notes["items"]:
            L.append(f"### {i['title']}")
            L.append("")
            L.append(i["body"])
            L.append("")

    takes = [n for n in nuggets if n.get("type") == "take"]
    if takes:
        L.append("## NLW's Takes")
        L.append("")
        for t in takes:
            L.append(f"### {t['headline']}")
            L.append("")
            L.append(t["body"])
            L.append("")

    if nuggets:
        L.append("## All Headlines, Briefly")
        L.append("")
        for n in nuggets:
            anchor = f"{canonical}#{n['id']}" if n.get("id") else canonical
            head = n.get("headline", "")
            if n.get("type") == "quote":
                head = f"“{head}”"
            attr = f" — {n['attribution']}" if n.get("attribution") else ""
            ts = f" ({n['ts']})" if n.get("ts") else ""
            L.append(f"- [{head}]({anchor}){attr}{ts}")
        L.append("")

    L.append("---")
    L.append("")
    L.append("All editorial content © The AI Daily Brief (host: Nathaniel Whittemore). "
             "Personal, non-commercial reading page assembled by Claude for David Lloyd, "
             "using the podcast's own machine-readable feeds. GP's Corner is Claude's commentary.")
    L.append("")
    return "\n".join(L)


def render_archive(manifest):
    rows = "".join(
        f"<li><a href='/a/{e['date']}.html'>{datetime.strptime(e['date'],'%Y-%m-%d').strftime('%a %d %b %Y')} — {escape(e['title'])}</a></li>"
        for e in sorted(manifest, key=lambda x: x["date"], reverse=True))
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Archive — David&rsquo;s AI Daily Brief</title><meta name="robots" content="noindex">
<link rel="alternate" type="application/rss+xml"
      title="David's AI Daily Brief" href="/feed.xml">
<style>{CSS}</style></head><body>{BACK_PILL}<div class="wrap">
<header class="mast"><div class="kicker">Distilled from The AI Daily Brief podcast</div>
<h1 class="mast">Archive</h1></header>
<div class="dateline"><span><a href="/">&larr; Latest edition</a></span></div>
<section><ul class="heads">{rows}</ul></section>
<footer>All editorial content &copy; <a href="{SITE}">The AI Daily Brief</a>.</footer>
</div></body></html>"""


def render_feed(manifest):
    """Private podcast RSS of the daily audio briefs (only editions with an mp3)."""
    items = []
    for e in sorted(manifest, key=lambda x: x["date"], reverse=True):
        mp3 = ROOT / "audio" / f"{e['date']}.mp3"
        if not mp3.exists():
            continue
        size = mp3.stat().st_size
        pub = datetime.strptime(e["date"], "%Y-%m-%d").strftime("%a, %d %b %Y 07:00:00 +0000")
        items.append(f"""<item>
<title>{escape(e['title'])} ({e['date']})</title>
<description>Spoken daily brief: the One Idea plus GP's Corner. Distilled from The AI Daily Brief podcast.</description>
<enclosure url="{SITE_URL}/audio/{e['date']}.mp3" length="{size}" type="audio/mpeg"/>
<guid isPermaLink="false">davids-brief-{e['date']}</guid>
<pubDate>{pub}</pubDate>
<link>{SITE_URL}/a/{e['date']}.html</link>
</item>""")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
<channel>
<title>David's AI Daily Brief (audio)</title>
<link>{SITE_URL}</link>
<language>en-gb</language>
<description>A three-minute spoken distillation of The AI Daily Brief podcast, with notes for UK general practice. Personal, non-commercial. All editorial content (c) The AI Daily Brief.</description>
<itunes:author>Claude, for David Lloyd</itunes:author>
<itunes:block>Yes</itunes:block>
{chr(10).join(items)}
</channel>
</rss>"""


def main():
    agent = fetch_json(f"{SITE}/agent.json")
    editions = agent["editions"]
    date = sys.argv[1] if len(sys.argv) > 1 else editions[0]["date"]
    meta = next((e for e in editions if e["date"] == date), None)
    if not meta:
        sys.exit(f"No edition found for {date}")
    ed = fetch_json(meta["json"])

    notes_path = ROOT / "notes" / f"{date}.json"
    notes = json.loads(notes_path.read_text()) if notes_path.exists() else None

    page = render(ed, notes)
    (ROOT / "a").mkdir(exist_ok=True)
    (ROOT / "a" / f"{date}.html").write_text(page)
    (ROOT / "a" / f"{date}.md").write_text(render_md(ed, notes))

    # manifest
    data_dir = ROOT / "data"
    data_dir.mkdir(exist_ok=True)
    mf_path = data_dir / "editions.json"
    manifest = json.loads(mf_path.read_text()) if mf_path.exists() else []
    manifest = [e for e in manifest if e["date"] != date]
    manifest.append({"date": date, "title": ed.get("title", "")})
    manifest.sort(key=lambda x: x["date"])
    mf_path.write_text(json.dumps(manifest, indent=2))

    # index = latest edition in manifest; archive page
    latest = manifest[-1]["date"]
    if latest == date:
        # fix relative links for root copy (archive.html link already root-relative)
        (ROOT / "index.html").write_text(page)
        (ROOT / "index.md").write_text(render_md(ed, notes))
    (ROOT / "archive.html").write_text(render_archive(manifest))
    (ROOT / "feed.xml").write_text(render_feed(manifest))

    # brief.json — today's brief as structured data (only refreshed for the latest edition)
    if latest == date:
        canonical = ed.get("canonicalUrl", f"{SITE}/e/{date}")
        thesis = ed.get("thesis") or {}
        zc_path = ROOT / "zitron" / f"{date}.json"
        zc = json.loads(zc_path.read_text()) if zc_path.exists() else None
        if zc and not zc.get("match"):
            zc = None
        brief = {
            "date": date,
            "title": ed.get("title", ""),
            "dek": ed.get("dek", ""),
            "source": canonical,
            "oneIdea": {"headline": thesis.get("headline", ""), "summary": thesis.get("sub", "")},
            "gpCorner": {
                "note": "AI commentary for UK general practice; not from the podcast",
                "items": (notes or {}).get("items", []),
            },
            "the_other_side": (
                {"source": zc["source_title"], "url": zc["source_url"],
                 "date": zc["source_date"], "same_day": zc["same_day"],
                 "text": zc["other_side"]} if zc else None),
            "the_truth_beneath": {"text": zc["truth_beneath"]} if zc else None,
            "headlines": [
                {
                    "id": n.get("id"),
                    "headline": n.get("headline", ""),
                    "type": n.get("type", "insight"),
                    "segment": n.get("segment", ""),
                    "timestamp": n.get("ts"),
                    "attribution": n.get("attribution"),
                    "summary": n.get("body", ""),
                    "link": f"{canonical}#{n.get('id', '')}",
                }
                for n in ed.get("nuggets", [])
            ],
            "audio": f"{SITE_URL}/audio/{date}.mp3" if (ROOT / "audio" / f"{date}.mp3").exists() else None,
            "generated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        (ROOT / "brief.json").write_text(json.dumps(brief, indent=2))
    print(f"Built edition {date} (latest: {latest}). Pages: a/{date}.html, index.html, archive.html, feed.xml")


if __name__ == "__main__":
    main()
