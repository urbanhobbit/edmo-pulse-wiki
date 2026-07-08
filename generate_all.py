#!/usr/bin/env python3
"""Generate full EDMO Pulse Wiki — pages, bundle, and viz."""
import json, os, shutil

HOME = os.path.expanduser("~")
WIKI = f"{HOME}/edmo-pulse-wiki"
OLD_WIKI = f"{HOME}/bilgi-llm-wiki/raw/articles"

ARTICLES = [
    {
        "slug": "2026-03-26-edmo-pulse",
        "date": "March 26, 2026",
        "title": "AI-Generated Content Shaping European Perceptions of Gulf Conflicts",
        "url": "https://edmo.eu/publications/?s=weekly+pulse+26+march",
        "sections": ["GLOBAL PULSE"],
        "summary": "AI-generated content shaping European perceptions of Gulf conflicts. Foreign influence operations in the Baltics. Disinformation surrounding the Artemis II mission."
    },
    {
        "slug": "2026-04-01-edmo-pulse",
        "date": "April 1, 2026",
        "title": "Hungarian Electoral Campaign Disinformation",
        "url": "https://edmo.eu/publications/?s=weekly+pulse+1+april",
        "sections": ["ELECTION BEAT"],
        "summary": "Hungarian electoral campaign disinformation. Lasting damage of disinformation campaigns. Prebunking false flag operations before the Hungarian elections."
    },
    {
        "slug": "2026-04-16-edmo-pulse",
        "date": "April 16, 2026",
        "title": "Orbán Has Been Defeated, But What Comes Next?",
        "url": "https://edmo.eu/publications/orban-has-been-defeated-but-what-comes-next/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Post-Orbán Hungary disinformation landscape. Political ads evade moderation. Gen-AI content and election integrity. Bulgarian electoral disinformation. Drones in the Baltics and Russian propaganda. Chat Control 2.0 and European public opinion."
    },
    {
        "slug": "2026-04-23-edmo-pulse",
        "date": "April 23, 2026",
        "title": "AI Slop: How Greed Is Affecting Democracies",
        "url": "https://edmo.eu/publications/ai-slop-how-greed-is-affecting-democracies/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "AI slop content flooding platforms. Fake AI feel-good stories in Malta. Telegram as Bulgarian elections blindspot. Pope Leo XIV vs Trump false claims. The importance of united and socially aware research."
    },
    {
        "slug": "2026-04-30-edmo-pulse",
        "date": "April 30, 2026",
        "title": "Trump's Assassination Attempts and Related Disinformation Are Two Sides of the Same Coin",
        "url": "https://edmo.eu/publications/trumps-assassination-attempts-and-related-disinformation-are-two-sides-of-the-same-coin/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Disinformation narratives surrounding Trump assassination attempts. Vaccine misinformation in Italy. French election disinformation ecosystem. AI-generated content and electoral integrity. Deepfakes in Turkish politics."
    },
    {
        "slug": "2026-05-07-edmo-pulse",
        "date": "May 7, 2026",
        "title": "From Zelensky to Magyar: Old and New Attempts at Disinformation-Driven Character Assassination",
        "url": "https://edmo.eu/publications/from-zelensky-to-magyar-old-and-new-attempts-at-disinformation-driven-character-assassination/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Disinformation-driven character assassination targeting Zelensky and Magyar. Romanian elections disinformation. UK local elections and AI-generated content. Climate disinformation narratives."
    },
    {
        "slug": "2026-05-14-edmo-pulse",
        "date": "May 14, 2026",
        "title": "Hantavirus-Related Disinformation, a New Menace for Bodies and Minds?",
        "url": "https://edmo.eu/publications/hantavirus-related-disinformation-a-new-menace-for-bodies-and-minds/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Hantavirus disinformation and health misinformation. AI-generated political content in Baltic states. Russian disinformation campaigns. Disinformation narratives around migration and crime."
    },
    {
        "slug": "2026-05-21-edmo-pulse",
        "date": "May 21, 2026",
        "title": "Crime, Migrants and Disinformation: An Online Banquet for Extremists, a Real-World Danger for Societies",
        "url": "https://edmo.eu/publications/crime-migrants-and-disinformation-an-online-banquet-for-extremists-a-real-world-danger-for-societies/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Crime and migration disinformation fueling extremism. Romanian presidential election interference. German AfD AI-generated content. Disinformation about Ukraine war narratives. Platform accountability."
    },
    {
        "slug": "2026-05-29-edmo-pulse",
        "date": "May 29, 2026",
        "title": "AI-Political Influencers: The New Gods of Propaganda and Disinformation?",
        "url": "https://edmo.eu/publications/ai-political-influencers-the-new-gods-of-propaganda-and-disinformation/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "AI-powered political influencers as new propaganda vectors. Spanish local elections disinformation. Deepfake detection advances. Russian information operations in Eastern Europe. Media literacy responses."
    },
    {
        "slug": "2026-06-04-edmo-pulse",
        "date": "June 4, 2026",
        "title": "The Same Old Story – A Heat Wave of Climate Disinformation",
        "url": "https://edmo.eu/publications/the-same-old-story-a-heat-wave-of-climate-disinformation/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Climate disinformation during European heatwave. Chromatic change conspiracy theory. Solar energy misinformation. AI-generated climate content. Election disinformation in multiple EU countries. Fact-checking coordination."
    },
    {
        "slug": "2026-06-11-edmo-pulse",
        "date": "June 11, 2026",
        "title": "Incident or Deliberate Action? Drone Crashes Are Always Good for Spreading Conspiracy Theories and Fearmongering",
        "url": "https://edmo.eu/publications/incident-or-deliberate-action-it-doesnt-matter-drone-crashes-are-always-good-for-spreading-conspiracy-theories-and-fearmongering/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Drone crash conspiracy theories. Disinformation about European defense. Romanian election interference update. Russian narratives about Baltic security. Platform content moderation challenges."
    },
    {
        "slug": "2026-06-18-edmo-pulse",
        "date": "June 18, 2026",
        "title": "Dublin, Southport, Belfast: Who Is Fanning the Flames?",
        "url": "https://edmo.eu/publications/dublin-southport-belfast-who-is-fanning-the-flames/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Disinformation following violent incidents in Ireland and UK. Far-right exploitation of tragedies. French legislative elections disinformation. Anti-immigration narratives. Social media platform accountability."
    },
    {
        "slug": "2026-06-25-edmo-pulse",
        "date": "June 25, 2026",
        "title": "The World Cup of Hypersexualized Fakes?",
        "url": "https://edmo.eu/publications/the-world-cup-of-hypersexualized-fakes/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "AI-generated non-consensual intimate content during World Cup. Deepfake pornography and platform responsibility. Electoral disinformation in multiple EU countries. Russian information operations. Digital services act implementation."
    },
    {
        "slug": "2026-07-03-edmo-pulse",
        "date": "July 3, 2026",
        "title": "Climate Change Denialism, and How to Shoot the Messenger to Ignore the Message",
        "url": "https://edmo.eu/publications/climate-change-denialism-and-how-to-shoot-the-messenger-to-ignore-the-message/",
        "sections": ["ON THE RISE", "ZOOM-IN", "ELECTION BEAT", "GLOBAL PULSE", "ON A DIFFERENT NOTE"],
        "summary": "Climate change denialism during European heatwave. Chromatic change conspiracy theory. Solar energy misinformation. Moldovan crypto election interference. Crimea sovereignty disinformation. Grooming gang disinformation in Britain. Google Gemini AI video generator risks."
    },
]

def make_page(a):
    tags_list = ["edmo", "weekly-pulse", "disinformation", "europe"]
    if "climate" in a["title"].lower() or "climate" in a["summary"].lower():
        tags_list.append("climate-change")
    if "ai" in a["title"].lower() or "ai" in a["summary"].lower() or "artificial" in a["title"].lower():
        tags_list.append("artificial-intelligence")
    if "elect" in a["title"].lower() or "elect" in a["summary"].lower():
        tags_list.append("elections")
    if "migrat" in a["summary"].lower() or "crime" in a["summary"].lower():
        tags_list.append("migration")
    
    tags_str = "\n".join(f"  - {t}" for t in sorted(set(tags_list)))
    sections_str = "\n".join(f"  - \"{s.upper()}\"" for s in a["sections"])
    
    return f"""---
title: "EDMO Weekly Pulse — {a['date']}"
source: "EDMO"
url: "{a['url']}"
date: "{a['date']}"
type: "weekly-pulse-issue"
sections:
{sections_str}
tags:
{tags_str}
---

## {a['title']}

**{a['date']}** — EDMO Weekly Pulse

{fix_content(a['summary'])}

## Sections

{chr(10).join(f"### {s}" for s in a['sections'])}

### Full Edition

➡️ [Read the full edition on EDMO]({a['url']})

---

*Source: [EDMO Weekly Pulse Archive](https://edmo.eu/pulse/)*

---

## 🔗 Related
- [[entities/edmo.md|European Digital Media Observatory (EDMO)]]
"""

def fix_content(t):
    return t

print("📝 Generating wiki pages...")
os.makedirs(f"{WIKI}/raw", exist_ok=True)
os.makedirs(f"{WIKI}/entities", exist_ok=True)

for a in ARTICLES:
    path = f"{WIKI}/raw/{a['slug']}.md"
    with open(path, 'w') as f:
        f.write(make_page(a))
    print(f"  ✅ {a['slug']}.md")

# Entity page
print("\n📝 Generating entity pages...")
entity_md = f"""---
title: "European Digital Media Observatory (EDMO)"
created: 2026-04-16
updated: 2026-07-08
type: entity
tags:
  - institution
  - eu
  - disinformation
  - fact-checking
  - media-literacy
sources:
{chr(10).join(f'  - raw/{a["slug"]}.md' for a in ARTICLES)}
---

# European Digital Media Observatory (EDMO)

AB'nin en büyük disiplinlerarası dezenformasyonla mücadele ağı. **European University Institute** (EUI) Florence School of Transnational Governance bünyesinde faaliyet gösteriyor.

**Kapsam:** 28 AB/AEA ülkesinde 15 ulusal/çokuluslu EDMO hub'ını koordine ediyor.

**Faaliyet Alanları:**
- **Fact-checking:** Dezenformasyon tespiti ve ifşası
- **Media Literacy:** Medya okuryazarlığı eğitimleri ve kaynakları
- **Research:** Dezenformasyon ekosistemi analizi
- **Policy Analysis:** AB dezenformasyon politikalarına katkı

**Hub'lar:** ADMO, BECID, BENEDMO, BROD, CEDMO, DE FACTO, EDMO BELUX, EDMO IRELAND, FACT, GADMO, HDMO, IBERIFIER, IDMO, MEDDMO, NORDIS

**Yayınlar:**
- **Weekly Pulse** — Haftalık dezenformasyon trendleri ve analiz bülteni
- Signals & Noise — Aylık dezenformasyon bülteni
- Best of Fact-checking Map
- EDMO Taskforce Reports

## Weekly Pulse Editions

{chr(10).join(f'- [[raw/{a["slug"]}.md|{a["date"]} — {a["title"]}]]' for a in ARTICLES)}
"""

with open(f"{WIKI}/entities/edmo.md", 'w') as f:
    f.write(entity_md)
print("  ✅ entities/edmo.md")

# Index page
print("\n📝 Generating index page...")
index_md = f"""---
title: "EDMO Weekly Pulse Wiki"
created: 2026-07-08
updated: 2026-07-08
type: index
---

# 📡 EDMO Weekly Pulse Wiki

EDMO (European Digital Media Observatory) tarafından her Perşembe yayınlanan **Weekly Pulse** bülteninin arşiv ve görselleştirme wiki'si.

## Nedir?

Weekly Pulse, Avrupa dezenformasyon ortamındaki güncel trendleri, vakaları ve analizleri derleyen haftalık bir bültendir. EDMO'nun 30 Avrupa ülkesindeki 15 hub'ının çalışmalarını sentezler.

## Bölümler

- **ON THE RISE** — Haftalık yükselen dezenformasyon riskleri
- **ZOOM-IN** — EDMO ağı tarafından tespit edilen vakalar
- **ELECTION BEAT** — Seçim dezenformasyonu takibi
- **GLOBAL PULSE** — Küresel dezenformasyon anlatıları
- **ON A DIFFERENT NOTE** — İlgili konularda kısa analizler

## Tüm Sayılar ({len(ARTICLES)})

| Tarih | Başlık |
|---|---|
{chr(10).join(f'| {a["date"]} | [[raw/{a["slug"]}.md|{a["title"]}]] |' for a in ARTICLES)}

## Künye

- **Yayıncı:** [[entities/edmo.md|European Digital Media Observatory (EDMO)]]
- **Sıklık:** Haftalık (her Perşembe)
- **Arşiv:** [EDMO Pulse](https://edmo.eu/pulse/)
- **Wiki güncelleme:** Otomatik (cronjob ile haftalık)
"""

with open(f"{WIKI}/index.md", 'w') as f:
    f.write(index_md)
print("  ✅ index.md")

# Bundle generation
print("\n📊 Generating bundle.json...")
nodes = []
edges = []
seen_ids = set()

# EDMO entity node
nodes.append({
    "data": {
        "id": "edmo",
        "label": "EDMO",
        "type": "entity",
        "color": "#3b82f6",
        "description": "European Digital Media Observatory",
        "degree": len(ARTICLES) + 5
    }
})
seen_ids.add("edmo")

# Concepts
concepts = [
    ("disinformation", "Dezenformasyon", "#ef4444"),
    ("elections", "Seçim Dezenformasyonu", "#f59e0b"),
    ("ai-content", "AI Üretimi İçerik", "#8b5cf6"),
    ("climate-disinfo", "İklim Dezenformasyonu", "#10b981"),
    ("migration", "Göç ve Suç Anlatıları", "#f97316"),
    ("platform-governance", "Platform Yönetişimi", "#06b6d4"),
    ("deepfakes", "Deepfake", "#ec4899"),
    ("media-literacy", "Medya Okuryazarlığı", "#14b8a6"),
]

for cid, clabel, ccolor in concepts:
    nodes.append({
        "data": {
            "id": cid,
            "label": clabel,
            "type": "concept",
            "color": ccolor,
            "degree": 0,
            "description": f"Kavram: {clabel}"
        }
    })
    seen_ids.add(cid)
    edges.append({
        "data": {
            "id": f"edmo-{cid}",
            "source": "edmo",
            "target": cid,
            "label": "covers"
        }
    })

# Month groups as concept nodes
months_order = [
    ("mar-2026", "March 2026", "#64748b"),
    ("apr-2026", "April 2026", "#64748b"),
    ("may-2026", "May 2026", "#64748b"),
    ("jun-2026", "June 2026", "#64748b"),
    ("jul-2026", "July 2026", "#64748b"),
]
for mid, mlabel, mcolor in months_order:
    nodes.append({
        "data": {
            "id": mid,
            "label": mlabel,
            "type": "concept",
            "color": mcolor,
            "degree": 0,
        }
    })
    seen_ids.add(mid)

# Article nodes
article_tags_map = {
    "2026-03-26-edmo-pulse": ["disinformation", "ai-content"],
    "2026-04-01-edmo-pulse": ["elections", "disinformation"],
    "2026-04-16-edmo-pulse": ["elections", "disinformation"],
    "2026-04-23-edmo-pulse": ["ai-content", "disinformation", "platform-governance"],
    "2026-04-30-edmo-pulse": ["disinformation", "elections", "deepfakes"],
    "2026-05-07-edmo-pulse": ["disinformation", "elections", "ai-content"],
    "2026-05-14-edmo-pulse": ["disinformation", "climate-disinfo"],
    "2026-05-21-edmo-pulse": ["migration", "disinformation", "elections"],
    "2026-05-29-edmo-pulse": ["ai-content", "disinformation", "media-literacy"],
    "2026-06-04-edmo-pulse": ["climate-disinfo", "disinformation", "elections"],
    "2026-06-11-edmo-pulse": ["disinformation", "platform-governance"],
    "2026-06-18-edmo-pulse": ["migration", "disinformation", "platform-governance"],
    "2026-06-25-edmo-pulse": ["deepfakes", "ai-content", "platform-governance"],
    "2026-07-03-edmo-pulse": ["climate-disinfo", "disinformation", "elections", "ai-content"],
}

month_of = {
    "2026-03": "mar-2026", "2026-04": "apr-2026", "2026-05": "may-2026",
    "2026-06": "jun-2026", "2026-07": "jul-2026",
}

for a in ARTICLES:
    month_key = "-".join(a["slug"].split("-")[:2])
    month_node = month_of.get(month_key, "mar-2026")
    
    # Get tag count for sizing
    tags = article_tags_map.get(a["slug"], ["disinformation"])
    degree = len(tags) + 2  # +1 for edmo, +1 for month
    
    nid = a["slug"]
    nodes.append({
        "data": {
            "id": nid,
            "label": a["date"].replace(",", ""),
            "type": "raw_article",
            "color": "#10b981",
            "full_title": a["title"][:60],
            "description": a["summary"][:200],
            "url": a["url"],
            "degree": degree
        }
    })
    seen_ids.add(nid)
    
    # Edge to entity
    edges.append({
        "data": {
            "id": f"edmo-{nid}",
            "source": "edmo",
            "target": nid,
            "label": "published"
        }
    })
    
    # Edge to month
    edges.append({
        "data": {
            "id": f"{nid}-{month_node}",
            "source": nid,
            "target": month_node,
            "label": "in"
        }
    })
    
    # Edges to concepts
    for tag in tags:
        if tag in [c[0] for c in concepts]:
            eid = f"{nid}-{tag}"
            edges.append({
                "data": {
                    "id": eid,
                    "source": nid,
                    "target": tag,
                    "label": "about"
                }
            })

# Sequence edges between consecutive issues
for i in range(len(ARTICLES) - 1):
    edges.append({
        "data": {
            "id": f"{ARTICLES[i]['slug']}-next-{ARTICLES[i+1]['slug']}",
            "source": ARTICLES[i]["slug"],
            "target": ARTICLES[i+1]["slug"],
            "label": "next",
            "color": "#fbbf24"
        }
    })

# Update degrees
degree_map = {}
for e in edges:
    src = e["data"]["source"]
    tgt = e["data"]["target"]
    degree_map[src] = degree_map.get(src, 0) + 1
    degree_map[tgt] = degree_map.get(tgt, 0) + 1

for n in nodes:
    nid = n["data"]["id"]
    if nid in degree_map:
        n["data"]["degree"] = degree_map[nid]

bundle = {"nodes": nodes, "edges": edges}
with open(f"{WIKI}/bundle.json", 'w') as f:
    json.dump(bundle, f, indent=2)
print(f"  ✅ bundle.json ({len(nodes)} nodes, {len(edges)} edges)")

# viz.html
print("📊 Generating viz.html...")
viz_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>EDMO Weekly Pulse — Wiki Viewer</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<script src="https://cdn.jsdelivr.net/npm/cytoscape@3.28.1/dist/cytoscape.min.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;overflow:hidden;background:#0f172a;color:#e2e8f0;height:100vh;display:flex;flex-direction:column}
.hdr{background:linear-gradient(135deg,#1a1a2e,#16213e);padding:10px 20px;display:flex;align-items:center;gap:12px;border-bottom:1px solid #1e293b;flex-shrink:0;flex-wrap:wrap}
.hdr h1{font-size:16px;font-weight:600}
.hdr .sub{font-size:12px;color:#64748b}
.ctrls{display:flex;gap:6px;flex-wrap:wrap;margin-left:auto}
.ctrls button{padding:3px 10px;border-radius:4px;border:1px solid #334155;background:#1e293b;color:#94a3b8;font-size:11px;cursor:pointer}
.ctrls button:hover{background:#334155;color:#e2e8f0}
.ctrls button.on{background:#3b82f6;color:#fff;border-color:#3b82f6}
#cy{flex:1;width:100%;min-height:0}
#info{position:fixed;right:20px;top:60px;width:380px;max-height:80vh;background:#1e293b;border:1px solid #334155;border-radius:8px;padding:16px;overflow-y:auto;display:none;z-index:100;font-size:13px;box-shadow:0 4px 20px rgba(0,0,0,.4)}
#info h2{font-size:14px;margin-bottom:8px;color:#e2e8f0;word-break:break-word}
#info .tp{font-size:11px;color:#64748b;margin-bottom:4px;text-transform:uppercase;letter-spacing:.5px}
#info .desc{color:#94a3b8;margin:8px 0;line-height:1.5;font-size:12px}
#info a{color:#60a5fa}
#info .tags span{display:inline-block;padding:1px 6px;border-radius:3px;background:#334155;color:#94a3b8;font-size:10px;margin:2px}
#info .close{float:right;cursor:pointer;color:#64748b;font-size:18px;line-height:1}
.legend{position:fixed;left:20px;bottom:20px;background:#1e293b;border:1px solid #334155;border-radius:6px;padding:8px 12px;font-size:11px;z-index:50}
.legend .r{display:flex;align-items:center;gap:6px;padding:2px 0}
.legend .d{width:10px;height:10px;border-radius:50%;flex-shrink:0}
#hint{position:fixed;left:50%;top:50%;transform:translate(-50%,-50%);color:#334155;font-size:14px;pointer-events:none;z-index:1;text-align:center;transition:opacity 1s}
@media(max-width:600px){.hdr h1{font-size:14px}.ctrls button{font-size:10px;padding:2px 6px}#info{width:calc(100vw-20px);right:10px;top:50px}}
</style>
</head>
<body>
<div class="hdr">
  <h1>📡 EDMO Weekly Pulse</h1>
  <span class="sub" id="stats">""" + f"{len(nodes)} nodes · {len(edges)} edges" + """</span>
  <div class="ctrls">
    <button onclick="filter('all')" class="on">All</button>
    <button onclick="filter('concept')">🧠 Concept</button>
    <button onclick="filter('entity')">🏛 Entity</button>
    <button onclick="filter('raw_article')">📄 Issues</button>
    <button onclick="layout('cose')">Auto</button>
    <button onclick="layout('grid')">Grid</button>
    <button onclick="layout('breadthfirst')">Timeline</button>
  </div>
</div>
<div id="cy"></div>
<div id="hint">🔍 Zoom &amp; drag to explore…</div>
<div id="info"><span class="close" onclick="closeInfo()">✕</span><div id="info-content"></div></div>
<div class="legend" id="legend"></div>
<script>
var DATA = null;
var cy = null;

function init() {
  fetch('bundle.json')
    .then(function(r) { return r.json(); })
    .then(function(data) {
      DATA = data;
      buildGraph();
      buildLegend();
    })
    .catch(function(err) {
      document.getElementById('stats').textContent = 'Error: ' + err.message;
    });
}

function buildGraph() {
  cy = cytoscape({
    container: document.getElementById('cy'),
    elements: [].concat(DATA.nodes, DATA.edges),
    style: [
      { selector: 'node', style: { 'background-color': 'data(color)', 'label': 'data(label)', 'color': '#f1f5f9', 'font-size': '8px', 'text-valign': 'center', 'text-halign': 'center', 'text-outline-width': 2, 'text-outline-color': '#0f172a', 'width': 'mapData(degree,0,30,20,60)', 'height': 'mapData(degree,0,30,20,60)', 'border-width': 1.5, 'border-color': 'data(color)', 'border-opacity': 0.6, 'background-opacity': 0.85 } },
      { selector: 'node[type="concept"]', style: { 'shape': 'diamond', 'font-weight': 'bold', 'font-size': '9px' } },
      { selector: 'node[type="entity"]', style: { 'shape': 'hexagon', 'font-size': '11px', 'width': 70, 'height': 70 } },
      { selector: 'node[type="raw_article"]', style: { 'shape': 'ellipse', 'font-size': '7px' } },
      { selector: 'edge', style: { 'width': 1, 'line-color': '#334155', 'target-arrow-color': '#334155', 'target-arrow-shape': 'triangle', 'curve-style': 'haystack', 'arrow-scale': 0.5, 'opacity': 0.3 } },
      { selector: 'edge[label="next"]', style: { 'width': 2, 'line-color': '#fbbf24', 'opacity': 0.6, 'curve-style': 'unbundled-bezier', 'target-arrow-shape': 'none' } },
      { selector: ':selected', style: { 'border-width': 3, 'border-color': '#fbbf24', 'border-opacity': 1 } }
    ],
    layout: { name: 'cose', fit: true, padding: 50, nodeRepulsion: 8000, idealEdgeLength: 100, gravity: 0.5 },
    wheelSensitivity: 0.4
  });

  cy.nodes().on('tap', function(e) {
    var node = e.target;
    if (!node.isNode || !node.isNode()) return;
    showInfo(node.data());
  });

  document.getElementById('hint').style.opacity = '0';
  setTimeout(function() { document.getElementById('hint').style.display = 'none'; }, 2000);
  updateStats();
}

function showInfo(d) {
  var el = document.getElementById('info-content');
  var tags = (d.type === 'raw_article') ? '<div class="tags"><span>#' + d.type + '</span></div>' : '';
  var desc = d.description ? '<div class="desc">' + d.description + '</div>' : '';
  var link = d.url ? '<a href="' + d.url + '" target="_blank">🔗 Read full edition →</a>' : '';
  el.innerHTML = '<span class="tp">' + (d.type || 'node') + '</span><h2>' + (d.full_title || d.label || '') + '</h2>' + desc + tags + link;
  document.getElementById('info').style.display = 'block';
}

function closeInfo() { document.getElementById('info').style.display = 'none'; }

function filter(type) {
  var btns = document.querySelectorAll('.ctrls button');
  btns.forEach(function(b) { b.classList.remove('on'); });
  event.target.classList.add('on');
  if (!cy) return;
  if (type === 'all') {
    cy.nodes().show();
    cy.edges().show();
  } else {
    cy.nodes().forEach(function(n) {
      if (n.data('type') === type) n.show();
      else n.hide();
    });
    cy.edges().forEach(function(e) {
      var src = e.source();
      var tgt = e.target();
      if (src.visible() && tgt.visible()) e.show();
      else e.hide();
    });
  }
  updateStats();
}

function layout(name) {
  if (!cy) return;
  var opts = { fit: true, padding: 50, animate: true, duration: 500 };
  if (name === 'grid') opts.name = 'grid';
  else if (name === 'breadthfirst') { opts.name = 'breadthfirst'; opts.roots = '#edmo'; }
  else { opts.name = 'cose'; opts.nodeRepulsion = 8000; opts.idealEdgeLength = 100; opts.gravity = 0.5; }
  cy.layout(opts);
}

function buildLegend() {
  var items = [
    { color: '#3b82f6', label: 'Entity (EDMO)' },
    { color: '#10b981', label: 'Issue (Weekly Pulse)' },
    { color: '#8b5cf6', label: 'Concept: AI Content' },
    { color: '#ef4444', label: 'Concept: Disinformation' },
    { color: '#f59e0b', label: 'Concept: Elections' },
    { color: '#10b981', label: 'Concept: Climate' },
    { color: '#f97316', label: 'Concept: Migration' },
    { color: '#fbbf24', label: 'Sequence (next issue)' },
  ];
  var h = items.map(function(i) {
    return '<div class="r"><div class="d" style="background:' + i.color + '"></div>' + i.label + '</div>';
  }).join('');
  document.getElementById('legend').innerHTML = h;
}

function updateStats() {
  if (!cy) return;
  var vn = cy.nodes(':visible').length;
  var ve = cy.edges(':visible').length;
  document.getElementById('stats').textContent = vn + '/' + DATA.nodes.length + ' nodes · ' + ve + ' edges';
}

init();
</script>
</body>
</html>"""

with open(f"{WIKI}/viz.html", 'w') as f:
    f.write(viz_html)
print("  ✅ viz.html")

# Log file
print("📝 Generating log...")
from datetime import date

log_md = f"""# EDMO Pulse Wiki — Change Log

## [{date.today().isoformat()}] Initial Ingest
- Created wiki from EDMO Weekly Pulse archive
- {len(ARTICLES)} issues ingested
- Generated bundle.json ({len(nodes)} nodes, {len(edges)} edges)
- Generated viz.html
- Source: https://edmo.eu/pulse/
"""

with open(f"{WIKI}/log.md", 'w') as f:
    f.write(log_md)
print("  ✅ log.md")

# README
readme = f"""# EDMO Weekly Pulse Wiki

EDMO Weekly Pulse bültenlerinin wiki arşivi ve görselleştirmesi.

- **{len(ARTICLES)} sayı** (Mart - Temmuz 2026)
- **Kaynak:** [EDMO Pulse](https://edmo.eu/pulse/)
- **Görselleştirme:** `viz.html` (Cytoscape.js)
- **Güncelleme:** Haftalık cronjob ile otomatik

## Yapı

```
raw/           — Her sayı için wiki sayfaları
entities/      — EDMO kurum sayfası
bundle.json    — Görselleştirme verisi
viz.html       — Etkileşimli grafik
index.md       — Ana sayfa
log.md         — Değişiklik kaydı
```
"""

with open(f"{WIKI}/README.md", 'w') as f:
    f.write(readme)
print("  ✅ README.md")

print(f"\n🎉 Done! Generated {len(ARTICLES)} articles + index + entity + bundle + viz")
