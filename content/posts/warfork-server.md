+++
title = 'Warfork Server'
date = 2024-01-16T22:13:02+01:00
+++
So recently I've set up a [warfork](https://warfork.com/) server. Warfork is FOSS and a fast-paced quake-like arena shooter.

Playing it with my friends really gave me that nostalgic feeling of LAN parties back in the day.

Only problem we had was that we didn't have our own server so we could play together in our own place. Which is when I realized I could just host my own server.

The process was quite simple. All I had to do was install steamcmd, login and download the Warfork Server Executable which is bundled with the game itself.

Only thing left to do was making sure that the server would start even when the host server has to reboot.

So this is what I came up with:

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

To quickly connect to it using the in-game console:
```
connect 0x29a.me
```
Who knows, maybe we'll see each other!