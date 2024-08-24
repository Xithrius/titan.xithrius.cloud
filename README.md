# titan.xithrius.cloud

## Services

- `db.docker-compose.yml`
  - [`PostgreSQL`](https://www.postgresql.org/)
- `git.docker-compose.yml`
  - [`gitea`](https://about.gitea.com/)
- `mc.docker-compose.yml`
  - [`vanilla-mc`](https://github.com/itzg/docker-minecraft-server)
  - [`modded-mc`](https://github.com/itzg/docker-minecraft-server) running [ATM9](https://www.curseforge.com/minecraft/modpacks/all-the-mods-9)
  - [`mc-router`](https://github.com/itzg/mc-router)
- `monitor.docker-compose.yml`
  - [`netdata`](https://github.com/netdata/netdata)

## Setup

### `modded-mc`

1. `cp .env.sample .env`
2. Get a CurseForge token from [the API page](https://console.curseforge.com/#/api-keys), and copy it to the `CF_API_KEY` variable in the `.env` file
3. Download the following mods, make a new folder called `downloads` in the same directory level as `scripts` in this repository:
   - [Towers of the Wild Modded](https://www.curseforge.com/minecraft/mc-mods/towers-of-the-wild-modded/files/4802113)
   - [Structory](https://www.curseforge.com/minecraft/mc-mods/structory/files/4767394)
   - [All the Wizard Gear](https://www.curseforge.com/minecraft/mc-mods/all-the-wizard-gear/files/4821791)
4. `docker-compose -f <category>.docker-compose.yml up -d`

### `netdata`

Additional configuration options for the `netdata` container can be found on [this page](https://learn.netdata.cloud/docs/installing/docker#recommended-way).
