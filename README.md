# For Penguins

NeoForge 1.21.1 modpack (CurseForge) and its server setup.

- `quests/`: FTB Quests files. The server downloads this folder on every start.
- `tools/quests/`: quest sources (Python). `python3 tools/quests/gen.py <out>` writes them to `<out>/config/ftbquests/quests`.
- `tools/`: mod resolver, pack builder, menu and compose generators.
- `docker-compose.yml`: the server compose deployed on Coolify (itzg/minecraft-server).
