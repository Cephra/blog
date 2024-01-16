+++
title = 'Warfork Systemd Service'
date = 2024-01-16T22:13:02+01:00
+++

```ini
[Unit]
Description=Warfork Server

[Service]
Type=forking
User=steam
Group=steam
Restart=always
ExecStart=/home/steam/start_server.sh
ExecStop=/usr/bin/tmux kill-server

[Install]
WantedBy=multi-user.target
```