# titan.xithrius.cloud

Using RAID mirroring across 2x2tb hard drives, this home server has/will have the following stack of docker containers running as services:
- [x] Dashboard: [flame](https://github.com/pawelmalak/flame)
- [ ] HDD monitoring: [scrutiny](https://github.com/AnalogJ/scrutiny)
- [x] General storage: [nextcloud](https://github.com/nextcloud/server)
- [x] Media storage: [jellyfin](https://github.com/jellyfin/jellyfin)
- [x] Minecraft: [minecraft-server](https://hub.docker.com/r/itzg/minecraft-server/)
    - Use the following to not expose IP: [tcpshield](https://tcpshield.com/), with the [realip](https://github.com/TCPShield/RealIP/releases) plugin
