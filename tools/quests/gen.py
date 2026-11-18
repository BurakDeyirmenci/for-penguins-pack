"""Gorev dosyalarini uretir ve esya/yaratik ID'lerini paketteki jar'lara karsi dogrular.
Kullanim: python3 gen.py <cikti_klasoru> [item_ids.json entity_ids.json]"""
import json, sys
from engine import build
from ch_basics import basics
from ch_tech import TECH
from ch_storage import STORAGE
from ch_magic import MAGIC
from ch_adventure import ADVENTURE

chapters = [basics] + TECH + STORAGE + MAGIC + ADVENTURE
used = build(chapters, sys.argv[1], "For Penguins")
n = sum(len(c.quests) for c in chapters)
print(f"{len(chapters)} bolum, {n} gorev")
if len(sys.argv) > 3:
    items, ents = json.load(open(sys.argv[2])), json.load(open(sys.argv[3]))
    bad = sorted(i for i in used["items"] if i not in items) + sorted("E:" + e for e in used["entities"] if e not in ents)
    print("BILINMEYEN ID:", bad if bad else "yok")
    sys.exit(1 if bad else 0)
