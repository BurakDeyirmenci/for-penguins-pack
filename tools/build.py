"""Builds a Prism instance and a CurseForge modpack zip from cf_mods.json."""
import hashlib, json, os, re, shutil, sys, urllib.request, zipfile

NAME, VERSION, MC, NEOFORGE = "For Penguins", "1.4.0", "1.21.1", "21.1.267"
SCRATCH = os.path.dirname(os.path.abspath(__file__))
INSTANCE = os.path.expanduser("~/.local/share/PrismLauncher/instances/Dostlar SMP")  # klasor adi sabit, gorunen ad instance.cfg icinde

mods = json.load(open(os.path.join(SCRATCH, "cf_mods.json")))["mods"]
OVERRIDES = os.path.join(SCRATCH, "overrides")  # make_menu.py ciktisi (config/fancymenu/...)
ICON = os.path.join(SCRATCH, "images", "icon_c_511.png")

# CurseForge modpack zip (arkadaslar Prism/CurseForge app'e import eder)
manifest = {
    "minecraft": {"version": MC, "modLoaders": [{"id": f"neoforge-{NEOFORGE}", "primary": True}]},
    "manifestType": "minecraftModpack", "manifestVersion": 1,
    "name": NAME, "version": VERSION, "author": "burak", "overrides": "overrides",
    "files": [{"projectID": m["projectID"], "fileID": m["fileID"], "required": True} for m in mods],
}
zip_path = os.path.join(SCRATCH, f"{NAME.replace(' ', '-')}-{VERSION}.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("manifest.json", json.dumps(manifest, indent=2))
    z.writestr("modlist.html", "<ul>\n" + "\n".join(
        f'<li><a href="https://www.curseforge.com/minecraft/mc-mods/{m["slug"]}">{m["name"]}</a></li>' for m in mods) + "\n</ul>\n")
    for root, _, files in os.walk(OVERRIDES):
        for fn in files:
            full = os.path.join(root, fn)
            z.write(full, os.path.join("overrides", os.path.relpath(full, OVERRIDES)))
print("zip:", zip_path)

# Prism instance (varsa sadece mod jar'lari ve shader'lar yenilenir, config'ler korunur)
mods_dir = os.path.join(INSTANCE, "minecraft", "mods")
shader_dir = os.path.join(INSTANCE, "minecraft", "shaderpacks")
if not os.path.exists(INSTANCE):
    os.makedirs(mods_dir)
    with open(os.path.join(INSTANCE, "instance.cfg"), "w") as f:
        f.write(f"[General]\nConfigVersion=1.2\nInstanceType=OneSix\nname={NAME}\niconKey=default\n"
                "OverrideMemory=true\nMinMemAlloc=2048\nMaxMemAlloc=6144\n")
    json.dump({"formatVersion": 1, "components": [
        {"uid": "net.minecraft", "version": MC, "important": True},
        {"uid": "net.neoforged", "version": NEOFORGE},
    ]}, open(os.path.join(INSTANCE, "mmc-pack.json"), "w"), indent=1)
os.makedirs(shader_dir, exist_ok=True)
shutil.copytree(OVERRIDES, os.path.join(INSTANCE, "minecraft"), dirs_exist_ok=True)

# gorunen ad + simge
icons_dir = os.path.expanduser("~/.local/share/PrismLauncher/icons")
os.makedirs(icons_dir, exist_ok=True)
shutil.copy(ICON, os.path.join(icons_dir, "forpenguins.png"))
cfg_path = os.path.join(INSTANCE, "instance.cfg")
cfg = open(cfg_path).read()
cfg = re.sub(r"(?m)^name=.*$", f"name={NAME}", cfg)
cfg = re.sub(r"(?m)^iconKey=.*$", "iconKey=forpenguins", cfg)
open(cfg_path, "w").write(cfg)
for old in os.listdir(mods_dir):
    if old.endswith(".jar"):
        os.remove(os.path.join(mods_dir, old))

for m in mods:
    target = os.path.join(shader_dir if m.get("shader") else mods_dir, m["file"])
    if os.path.exists(target):
        continue
    data = urllib.request.urlopen(urllib.request.Request(m["url"], headers={"User-Agent": "modpack-builder"})).read()
    if m["sha1"] and hashlib.sha1(data).hexdigest() != m["sha1"]:
        sys.exit(f"hash uyusmuyor: {m['file']}")
    open(target, "wb").write(data)
print(f"instance: {INSTANCE} ({len(mods)} dosya)")
