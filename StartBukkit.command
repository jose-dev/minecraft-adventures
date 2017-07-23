#!/bin/bash
echo "Adventures In Minecraft"
echo "Bukkit Minecraft Server Version is 1.6.4"
echo "  Note - make sure Minecraft is using 1.6.4"
echo "Press any key to continue"
read -n 1 -s
cd "$( dirname "$0" )"
cd Bukkit
./start_server.command