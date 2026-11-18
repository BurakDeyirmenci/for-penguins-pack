"""Sunucu docker-compose.yml'ini uretir: sunucu modlari (cf_mods.json) + FTB Quests gorevleri.
Gorevler GitHub reposundan (quests/ klasoru) her acilista indirilip /data/config/ftbquests/quests'e yazilir.
Kullanim: python3 mk_compose.py <cf_mods.json> <cikti.yml>"""
import json, sys, urllib.parse

REPO = "BurakDeyirmenci/for-penguins-pack"
mods_json, out = sys.argv[1:3]
mods = [m for m in json.load(open(mods_json))["mods"] if not m["client_only"]]
urls = []
for m in mods:
    u = urllib.parse.urlsplit(m["url"])
    urls.append(urllib.parse.urlunsplit(u._replace(path=urllib.parse.quote(urllib.parse.unquote(u.path)))))

mods_block = ",\n".join(" " * 8 + u for u in urls)
open(out, "w").write(f"""services:
  minecraft:
    image: itzg/minecraft-server:java21
    restart: unless-stopped
    tty: true
    stdin_open: true
    ports:
      - "25565:25565"       # Minecraft
      - "24454:24454/udp"   # Simple Voice Chat
    entrypoint:
      - /bin/sh
      - -c
      - >-
        if curl -fsSL https://github.com/{REPO}/archive/refs/heads/main.tar.gz -o /tmp/pack.tgz; then
        rm -rf /data/config/ftbquests/quests && mkdir -p /data/config/ftbquests &&
        tar xzf /tmp/pack.tgz -C /data/config/ftbquests --strip-components=1 for-penguins-pack-main/quests &&
        chown -R 1000:1000 /data/config/ftbquests; else echo "gorevler indirilemedi, eskiler kullaniliyor"; fi;
        exec /start
    environment:
      EULA: "TRUE"
      TYPE: NEOFORGE
      VERSION: "1.21.1"
      NEOFORGE_VERSION: "21.1.267"
      MEMORY: "4G"
      USE_AIKAR_FLAGS: "true"
      MOTD: "Dostlar SMP"
      DIFFICULTY: normal
      MAX_PLAYERS: "10"
      VIEW_DISTANCE: "8"
      SIMULATION_DISTANCE: "6"
      ONLINE_MODE: "true"
      ENABLE_WHITELIST: "true"
      WHITELIST: ${{WHITELIST}}
      OPS: ${{OPS}}
      ALLOW_FLIGHT: "true"   # Mekanism jetpack / Ars vb. icin kick yememek
      REMOVE_OLD_MODS: "true"
      MODS: >-
{mods_block}
    volumes:
      - minecraft-data:/data
    deploy:
      resources:
        limits:
          memory: 6G

volumes:
  minecraft-data:
""")
print(out, len(urls), "mod")
