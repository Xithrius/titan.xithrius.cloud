# titan.xithrius.cloud

# `prod.docker-compose.yml`:

- [gitlab](https://hub.docker.com/r/gitlab/gitlab-ce)

## Setup

`docker compose up gitlab -d`

# `old.docker-compose.yml`:

- [vanilla-mc](https://github.com/itzg/docker-minecraft-server)
- [modded-mc](https://github.com/itzg/docker-minecraft-server)
- [jellyfin](https://github.com/jellyfin/jellyfin)
- [netdata](https://github.com/netdata/netdata)
- [PostgreSQL](https://www.postgresql.org/)
- [home-assistant](https://github.com/home-assistant/core)

## Old setup

### Setup for production

1. `cp .env.sample .env`
2. Get a CurseForge token from [the API page](https://console.curseforge.com/#/api-keys), and copy it to the `CF_API_KEY` variable in the `.env` file
3. Download the following mods, make a new folder called `downloads` in the same directory level as `scripts` in this repository:
    - [Towers of the Wild Modded](https://www.curseforge.com/minecraft/mc-mods/towers-of-the-wild-modded/files/4802113)
    - [Structory](https://www.curseforge.com/minecraft/mc-mods/structory/files/4767394)
    - [All the Wizard Gear](https://www.curseforge.com/minecraft/mc-mods/all-the-wizard-gear/files/4821791)
3. `docker-compose -f prod.docker-compose.yml up -d`

### More info

#### Netdata

More configuration options for the container can be found on [this page](https://learn.netdata.cloud/docs/installing/docker#recommended-way).
