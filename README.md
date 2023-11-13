# titan.xithrius.cloud

`dev.docker-compose.yml`:

- [x] [PostgreSQL](https://www.postgresql.org/)
- [x] [home-assistant](https://github.com/home-assistant/core)

`prod.docker-compose.yml`:

- [x] [vanilla-mc](https://github.com/itzg/docker-minecraft-server)
- [x] [modded-mc](https://github.com/itzg/docker-minecraft-server)
- [x] [jellyfin](https://github.com/jellyfin/jellyfin)
- [ ] [docker-mc-backup](https://github.com/itzg/docker-mc-backup)


## Setup for production

1. `cp .env.sample .env`
2. Get a CurseForge token from [the API page](https://console.curseforge.com/#/api-keys), and copy it to the `CF_API_KEY` variable in the `.env` file
3. Download the following mods, make a new folder called `downloads` in the same directory level as `scripts` in this repository:
    - [Towers of the Wild Modded](https://www.curseforge.com/minecraft/mc-mods/towers-of-the-wild-modded/files/4802113)
    - [Structory](https://www.curseforge.com/minecraft/mc-mods/structory/files/4767394)
    - [All the Wizard Gear](https://www.curseforge.com/minecraft/mc-mods/all-the-wizard-gear/files/4821791)
3. `docker-compose -f prod.docker-compose.yml up -d`
