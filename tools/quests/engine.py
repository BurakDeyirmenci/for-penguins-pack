"""FTB Quests (2101.x, NeoForge 1.21.1) dosyalarini Python tanimlarindan uretir.

Gorev tanimi:
    Q(key, tasks, title=None, sub=None, desc=[...], deps=[...], rew=[...], x=, y=, shape=, size=)
tasks: "mod:item" | "mod:item*16" | "check" | "kill:mod:entity*3" | "adv:minecraft:story/x"
rew:   "xp:100" | "lv:10" | "mod:item*4"
title None ve tek esya gorevi ise FTB Quests esyanin oyundaki adini gosterir.
"""
import hashlib, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))


def hid(*parts):
    h = hashlib.sha1("/".join(parts).encode()).hexdigest()[:16].upper()
    return ("%X" % (int(h[0], 16) & 7)) + h[1:]  # isaretli long'a sigsin


def s(v):
    return json.dumps(v, ensure_ascii=False)


class Q:
    def __init__(self, key, tasks, title=None, sub=None, desc=(), deps=(), rew=("xp:50",),
                 x=None, y=None, shape=None, size=None, optional=False):
        self.key, self.title, self.sub, self.desc = key, title, sub, list(desc)
        self.tasks = [tasks] if isinstance(tasks, str) else list(tasks)
        self.deps, self.rew = list(deps), list(rew)
        self.x, self.y, self.shape, self.size, self.optional = x, y, shape, size, optional


class Chapter:
    def __init__(self, key, title, icon, group, quests, sub=None, shape="circle"):
        self.key, self.title, self.icon, self.group = key, title, icon, group
        self.quests, self.sub, self.shape = quests, sub, shape
        self.id = hid("chapter", key)


GROUPS = [("tech", "Teknoloji"), ("storage", "Depolama"), ("magic", "Büyü"), ("adventure", "Macera")]


def item(spec):
    m = re.fullmatch(r"([a-z0-9_.-]+:[a-z0-9_/.-]+)(?:\*(\d+))?", spec)
    if not m:
        raise ValueError(spec)
    return m.group(1), int(m.group(2) or 1)


def task_snbt(q, i, spec, used):
    tid = hid("task", q.key, str(i))
    if spec == "check":
        return [f'id: "{tid}"', 'type: "checkmark"']
    if spec.startswith("kill:"):
        ent, n = item(spec[5:])
        used["entities"].add(ent)
        return [f'entity: "{ent}"', f'id: "{tid}"', 'type: "kill"', f"value: {n}L"]
    if spec.startswith("adv:"):
        return [f'advancement: "{spec[4:]}"', 'criterion: ""', f'id: "{tid}"', 'type: "advancement"']
    iid, n = item(spec)
    used["items"].add(iid)
    out = [] if n == 1 else [f"count: {n}L"]
    return out + [f'id: "{tid}"', f'item: {{ count: 1, id: "{iid}" }}', 'type: "item"']


def reward_snbt(q, i, spec, used):
    rid = hid("reward", q.key, str(i))
    if spec.startswith("xp:"):
        return [f'id: "{rid}"', 'type: "xp"', f"xp: {int(spec[3:])}"]
    if spec.startswith("lv:"):
        return [f'id: "{rid}"', 'type: "xp_levels"', f"xp_levels: {int(spec[3:])}"]
    iid, n = item(spec)
    used["items"].add(iid)
    return [f'id: "{rid}"', f'item: {{ count: {n}, id: "{iid}" }}', 'type: "item"']


def block(lines, ind):
    pad = "\t" * ind
    return "{\n" + "".join(f"{pad}\t{l}\n" for l in lines) + pad + "}"


def obj_list(objs, ind):
    if len(objs) == 1:
        return "[" + block(objs[0], ind) + "]"
    pad = "\t" * ind
    return "[\n" + "".join(f"{pad}\t{block(o, ind + 1)}\n" for o in objs) + pad + "]"


def layout(quests):
    """x/y verilmeyen gorevleri bagimlilik derinligine gore sutunlara dizer."""
    by = {q.key: q for q in quests}
    depth = {}

    def d(q):
        if q.key not in depth:
            depth[q.key] = 0 if not q.deps else 1 + max(d(by[k]) for k in q.deps if k in by)
        return depth[q.key]

    cols = {}
    for q in quests:
        cols.setdefault(d(q), []).append(q)
    for c, qs in cols.items():
        free = [q for q in qs if q.x is None]
        for i, q in enumerate(free):
            q.x = c * 2.0
            q.y = (i - (len(free) - 1) / 2) * 1.5


def build(chapters, out, file_title):
    qdir = os.path.join(out, "config", "ftbquests", "quests")
    for sub in ("chapters", "lang/en_us/chapters", "lang/tr_tr/chapters"):
        os.makedirs(os.path.join(qdir, sub), exist_ok=True)
    used = {"items": set(), "entities": set()}
    lang_chapters = {}
    keys = {}
    for ch in chapters:
        for q in ch.quests:
            if q.key in keys:
                raise ValueError("ayni gorev anahtari: " + q.key)
            keys[q.key] = ch.key

    order = {"": 0}
    for ci, ch in enumerate(chapters):
        layout(ch.quests)
        qs, lang = [], {}
        lang[f"chapter.{ch.id}.title"] = ch.title
        if ch.sub:
            lang[f"chapter.{ch.id}.chapter_subtitle"] = [ch.sub]
        for q in ch.quests:
            qid = hid("quest", q.key)
            lines = []
            deps = [hid("quest", k) for k in q.deps]
            for k in q.deps:
                if k not in keys:
                    raise ValueError(f"{q.key}: bilinmeyen bagimlilik {k}")
            if deps:
                lines.append("dependencies: [" + ", ".join(s(x) for x in deps) + "]")
            lines.append(f'id: "{qid}"')
            if q.optional:
                lines.append("optional: true")
            lines.append("rewards: " + obj_list([reward_snbt(q, i, r, used) for i, r in enumerate(q.rew)], 3))
            if q.shape:
                lines.append(f'shape: "{q.shape}"')
            if q.size:
                lines.append(f"size: {q.size:.1f}d")
            lines.append("tasks: " + obj_list([task_snbt(q, i, t, used) for i, t in enumerate(q.tasks)], 3))
            lines += [f"x: {q.x:.1f}d", f"y: {q.y:.1f}d"]
            qs.append(lines)
            if q.title:
                lang[f"quest.{qid}.title"] = q.title
            if q.sub:
                lang[f"quest.{qid}.quest_subtitle"] = q.sub
            if q.desc:
                lang[f"quest.{qid}.quest_desc"] = q.desc
        grp = "" if ch.group is None else hid("group", ch.group)
        order.setdefault(grp, 0)
        icon_id, _ = item(ch.icon)
        used["items"].add(icon_id)
        head = [
            "default_hide_dependency_lines: false",
            f'default_quest_shape: "{ch.shape}"',
            f'filename: "{ch.key}"',
            f'group: "{grp}"',
            f'icon: {{ id: "{icon_id}" }}',
            f'id: "{ch.id}"',
            f"order_index: {order[grp]}",
            "quest_links: [ ]",
            "quests: [\n" + "".join(f"\t\t{block(l, 2)}\n" for l in qs) + "\t]",
        ]
        order[grp] += 1
        open(os.path.join(qdir, "chapters", ch.key + ".snbt"), "w").write(block(head, 0) + "\n")
        lang_chapters[ch.key] = lang

    open(os.path.join(qdir, "chapter_groups.snbt"), "w").write(
        "{\n\tchapter_groups: [\n" + "".join(f'\t\t{{ id: "{hid("group", g)}" }}\n' for g, _ in GROUPS) + "\t]\n}\n")
    open(os.path.join(qdir, "data.snbt"), "w").write(block([
        'default_autoclaim_rewards: "disabled"', "default_consume_items: false",
        'default_quest_shape: "circle"', "detection_delay: 20", "disable_gui: false",
        "drop_loot_crates: false", 'icon: { id: "minecraft:blue_ice" }', 'lock_message: ""',
        "pause_game: false", 'progression_mode: "flexible"', "show_lock_icons: true", "version: 13",
    ], 0) + "\n")

    def lang_file(d):
        return "{\n" + "".join(f"\t{k}: {s(v)}\n" for k, v in sorted(d.items())) + "}\n"

    # Herkes Turkce gorsun diye en_us ve tr_tr ayni icerik
    for loc in ("en_us", "tr_tr"):
        base = os.path.join(qdir, "lang", loc)
        open(os.path.join(base, "file.snbt"), "w").write(lang_file({"file.0000000000000001.title": file_title}))
        open(os.path.join(base, "chapter_group.snbt"), "w").write(
            lang_file({f"chapter_group.{hid('group', g)}.title": t for g, t in GROUPS}))
        open(os.path.join(base, "chapter.snbt"), "w").write(lang_file(
            {k: v for l in lang_chapters.values() for k, v in l.items() if k.startswith("chapter.")}))
        for ck, l in lang_chapters.items():
            open(os.path.join(base, "chapters", ck + ".snbt"), "w").write(
                lang_file({k: v for k, v in l.items() if k.startswith("quest.")}))
    return used
