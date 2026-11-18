import json, os, sys, urllib.request, urllib.parse

MC, NEOFORGE = "1.21.1", 6  # modLoaderType 6 = NeoForge
SHADERS = 6552  # shaderpack classId
API = "https://api.curseforge.com/v1"
KEY = open(os.path.expanduser("~/.config/curseforge.key")).read().strip()


def get(path, **params):
    url = f"{API}{path}" + (f"?{urllib.parse.urlencode(params)}" if params else "")
    req = urllib.request.Request(url, headers={"x-api-key": KEY, "Accept": "application/json", "User-Agent": "modpack-builder"})
    return json.load(urllib.request.urlopen(req))["data"]


resolved, missing = {}, []


def find(slug):
    for cls in (6, SHADERS):
        r = get("/mods/search", gameId=432, classId=cls, slug=slug)
        if r:
            return r[0]
    return None


def add(mod, required_by=None):
    if mod["id"] in resolved:
        return
    if mod["classId"] == SHADERS:  # shader paketleri loader'a bagli degil
        files = get(f"/mods/{mod['id']}/files", pageSize=50)
    else:
        files = get(f"/mods/{mod['id']}/files", gameVersion=MC, modLoaderType=NEOFORGE, pageSize=50)
        files = [f for f in files if MC in f["gameVersions"] and "NeoForge" in f["gameVersions"]]
    rel = [f for f in files if f["releaseType"] == 1] or [f for f in files if f["releaseType"] == 2] or files
    if not rel:
        missing.append(f"{mod['slug']} (uyumlu dosya yok{', gerekli: ' + required_by if required_by else ''})")
        return
    f = max(rel, key=lambda x: x["fileDate"])
    resolved[mod["id"]] = {
        "slug": mod["slug"], "name": mod["name"], "projectID": mod["id"], "fileID": f["id"],
        "file": f["fileName"], "downloadable": f.get("downloadUrl") is not None, "url": f.get("downloadUrl"),
        "sha1": next((h["value"] for h in f["hashes"] if h["algo"] == 1), None),
        "client_only": mod["classId"] == SHADERS or ("Client" in f["gameVersions"] and "Server" not in f["gameVersions"]),
        "shader": mod["classId"] == SHADERS,
        "required_by": required_by,
    }
    for d in f["dependencies"]:
        if d["relationType"] == 3:  # RequiredDependency
            add(get(f"/mods/{d['modId']}"), mod["slug"])


for slug in sys.argv[1:]:
    m = find(slug)
    if m:
        add(m)
    else:
        missing.append(f"{slug} (slug bulunamadi)")

json.dump({"mods": sorted(resolved.values(), key=lambda x: x["slug"]), "missing": missing}, sys.stdout, indent=1)
