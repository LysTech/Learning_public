#!/usr/bin/env python3
"""
Sync papers, videos, and books from a knowledge-index JSON into the vault.

Usage:
    python3 tools/sync_library.py [DATA_DIR]

DATA_DIR defaults to ~/Downloads/data and must contain index/knowledge_index.json.

Routing (one note per item, by type):
    paper -> Literature/<channel>/
    video -> Videos/<channel>/
    book  -> Books/<channel>/

Safe to re-run. Items are matched by a stable `uid`. On update it refreshes the
auto-generated parts (frontmatter + Summary / Key points / Links) but PRESERVES:
    * the `status` and `rating` you set,
    * everything from the `## My notes` heading onward.
Notes without a `uid` (hand-made) are never touched.
"""
import json, re, sys
from pathlib import Path

DATA = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else Path.home() / "Downloads" / "data"
INDEX = DATA / "index" / "knowledge_index.json"
VAULT = Path(__file__).resolve().parent.parent

# type -> output folder. Order = classification priority (first match wins).
TYPES = [("paper", "Literature"), ("video", "Videos"), ("book", "Books")]
ROOTS = {t: VAULT / folder for t, folder in TYPES}

INVALID = re.compile(r'[\\/:*?"<>|#^\[\]]+')
STATUS_MAP = {"unread": "to-read", "read": "read", "reading": "reading"}

def kind(item):
    tags = item.get("tags") or []
    ct = item.get("content_type")
    for t, _ in TYPES:
        if ct == t or t in tags:
            return t
    return None

def safe_name(title, fallback):
    t = INVALID.sub(" ", (title or "").strip() or fallback)
    return (re.sub(r"\s+", " ", t).strip(" .")[:110].strip() or fallback)

def q(s):
    s = "" if s is None else str(s)
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

def qlist(xs):
    xs = [x for x in (xs or []) if str(x).strip()]
    return "[" + ", ".join(q(x) for x in xs) + "]"

def parse_existing(text):
    uid = status = rating = None
    my = None
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            if line.startswith("uid:"):     uid = line[4:].strip().strip('"')
            elif line.startswith("status:"): status = line[7:].strip()
            elif line.startswith("rating:"): rating = line[7:].strip()
    mn = re.search(r"\n(## My notes\n.*)$", text, re.DOTALL)
    if mn: my = mn.group(1)
    return uid, status, rating, my

# --- index existing notes across all managed roots -------------------------
existing, by_loc = {}, {}
for root in ROOTS.values():
    if root.exists():
        for p in root.rglob("*.md"):
            uid, *_ = parse_existing(p.read_text(encoding="utf-8"))
            if uid:
                existing[uid] = p
            by_loc[(p.parent.name, p.stem.lower())] = p

items = json.load(open(INDEX))["items"]

claimed = set()
def resolve_path(folder, base, keep):
    folder.mkdir(parents=True, exist_ok=True)
    n = 0
    while True:
        name = base if n == 0 else f"{base} ({n+1})"
        path = folder / f"{name}.md"
        if path == keep or (path not in claimed and not path.exists()):
            return path
        n += 1

stats = {t: {"added": 0, "updated": 0} for t, _ in TYPES}
for it in items:
    t = kind(it)
    if not t:
        continue
    uid = it.get("id")
    chan = it.get("discord_channel") or "uncategorized"
    folder = ROOTS[t] / chan
    base = safe_name(it.get("title"), uid or "untitled")

    old = existing.get(uid) or by_loc.get((chan, base.lower()))
    is_new = old is None

    if old and old.exists():
        _, e_status, e_rating, e_my = parse_existing(old.read_text(encoding="utf-8"))
        status = e_status or STATUS_MAP.get(it.get("status"), "to-read")
        rating = e_rating if e_rating is not None else ""
        my_block = e_my or "## My notes\n- \n"
    else:
        status = STATUS_MAP.get(it.get("status"), "to-read")
        rating = ""
        my_block = "## My notes\n- \n"

    path = resolve_path(folder, base, keep=old)
    claimed.add(path)

    authors = it.get("authors") or []
    if isinstance(authors, str):
        authors = [a.strip() for a in re.split(r",|;", authors) if a.strip()]
    added_date = (it.get("ingested_at") or it.get("shared_at") or "")[:10]
    url = it.get("source_url") or ""
    note_text = (it.get("note_text") or "").strip()
    summary = (it.get("normalized_summary") or "").strip()
    kps = it.get("key_points") or []

    fm = ["---", f"type: {t}", f"uid: {q(uid)}",
          f"title: {q(it.get('title'))}",
          f"authors: {qlist(authors)}",
          f"year: {it.get('year') or ''}",
          f"venue: {q(it.get('venue') or '')}",
          f"doi: {q(it.get('doi') or '')}",
          f"url: {q(url)}",
          f"status: {status}",
          f"rating: {rating}",
          f"shared_by: {q(it.get('shared_by') or '')}",
          f"channel: {q(chan)}",
          f"tags: {qlist(it.get('tags'))}",
          f"source: {q(it.get('source_type') or '')}",
          f"added: {added_date}",
          "---", ""]

    body = ["## Summary", summary or "<!-- TODO -->", ""]
    if kps:
        body += ["## Key points"] + [f"- {k}" for k in kps] + [""]
    if note_text and note_text != url:
        body += ["## Notes", note_text, ""]
    body += ["## Links"]
    if url: body.append(f"- Source: {url}")
    if it.get("discord_message_url"): body.append(f"- Discord: {it['discord_message_url']}")
    body += ["", my_block.rstrip() + "\n"]

    path.write_text("\n".join(fm) + "\n".join(body), encoding="utf-8")
    if old and old.exists() and old != path:
        old.unlink()

    stats[t]["added" if is_new else "updated"] += 1

print("Sync complete:")
for t, _ in TYPES:
    s = stats[t]
    print(f"  {t:6} {s['added']:>4} added, {s['updated']:>4} updated  -> {ROOTS[t].name}/")
