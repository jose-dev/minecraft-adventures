Apple Mac Starter Kit
Martin O'Hanlon

From the book: "Adventures in Minecraft"
 written by David Whale and Martin O'Hanlon, Wiley, 2014
 http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html

-------------------------------

Description
------------------------------- 
This starter kit contains a pre-configured Bukkit (v. 1.6.4) server and a folder called "MyAdventures" which contains all the Python libraries required to complete all the chapters in "Adventure in Minecraft".

It is highly recommended that you use the Starter Kit as is and follow the instructions in Adventure 1 - "Hello Minecraft World" to setup your computer.  

The structure of the StarterKit zip file is as follows:
AdventuresInMinecraft
 - Bukkit : contains the pre-configured bukkit server and raspberry juice plugin
 - MyAdventures : folders to save the minecraft programs too
   - mcpi : python api library distributed with Minecraft: Pi Edition
   - anyio : python library for controlling hardware
 - StartBukkit.command : a command file used to start the bukkit server
 - findPort.py : a python program used in adventure 5 to find the com port a connected arduino uses
-------------------------------


StarterKit Creation Guide
-------------------------------
If required the information below can be used as a guide to create your own StarterKit from scratch.  It is written as guide, not as a precise series of instructions.  There is no guarantee that they are accurate and are provided as is.

You can use either Bukkit or Canarymod for the minecraft server.  Follow the instructions to Download and run either Bukkit or Canarymod not both!

Create folders
----------------------
Create a folder "AdventuresInMinecraft"

Create a folder "AdventuresInMinecraft\Bukkit"
             or "AdventuresInMinecraft\Canarymod"
(depending on whether you want to use Bukkit or Canarymod)

Create a folder "AdventuresInMinecraft\MyAdventures"

Download and run Bukkit
---------------------
Download Bukkit from dl.bukkit.com and put it in "AdventuresInMinecraft\Bukkit", the file will be named craftbukkit-#.#.#-R#.0.jar where the #'s are the current version number; make a note of the version number, you will need this later.

Rename the downloaded .jar file from craftbukkit-#.#.#-R#.#.jar to craftbukkit.jar.

Open TextEdit and insert the following text:

#!/bin/bash
cd "$( dirname "$0" )"
java -Xmx1024M -jar craftbukkit.jar

Save the file in TextEdit to the Bukkit folder as start_server.command.

The start_server.command file is a command program which will startup the Bukkit server when it is run, it needs to be made executable.

Open Terminal, and type the following command, BUT do not press enter:

chmod a+x

Drag the start_server.command into Terminal and hit enter

Double-click the start_server.command file to run it and startup Bukkit.

When you first start Bukkit it will take a little time to run as it sets up the server and creates a new Minecraft world, when it’s finished you will see the message Done in Bukkit's command window.

When you want to start your Minecraft Bukkit server in the future you can double click on the start_server.command file.

To stop Bukkit, enter the command stop into the command window and press Enter.

 - Configure Bukkit
 ----------------------
Open TextEdit, click File, Open and goto the Bukkit folder and open the file server.properties.

By changing the server.properties files you can change how Bukkit is setup.
Change:
 - gamemode=0 to gamemode=1 to change the server from survival mode to creative.
 - force-gamemode=false to force-gamemode=true to make all players play in creative mode.
 - spawn-monsters=true to spawn-monsters=false so monsters mobs won’t appear in the game.
 - allow-flight=false to allow-flight=true so you can fly in Minecraft.
 - online-mode=true to online-mode=false so you dont need to be connected to the internet to use Bukkit

 - Create StartBukkit.command
 ----------------------
Open TextEdit and add the following text:

#!/bin/bash
echo "Adventures In Minecraft"
echo "Bukkit Minecraft Server Version is #.#.#"
echo "  Note - make sure Minecraft is using #.#.#"
echo "Press any key to continue"
read -n 1 -s
cd "$( dirname "$0" )"
cd Bukkit
./start_server.command

Replace #.#.# with the version number of Bukkit you downloaded.

Save the folder as StartBukkit.command to the MyAdventures folder

Open Terminal, and type the following command, BUT do not press enter:

chmod a+x

Drag the StartBukkit.command into Terminal and hit enter

 - Install RaspberryJuice
 ----------------------
RaspberryJuice is a plugin for Bukkit which will allow you to write programs which will change the Minecraft world as you are playing, just like the API which comes with Minecraft: Pi Edition on the Raspberry Pi.

Goto dev.bukkit.org/bukkit-plugins/raspberryjuice/ and download the latest version of the raspberry juice plugin, download the raspberryjuice-#.#.jar file.  

Copy the raspberryjuice-#-#.jar plugin to the plugins folder in the Bukkit folder.


Download and run Canarymod
---------------------
Download Canarymod from http://canarymod.net/releases and put it in "AdventuresInMinecraft\Canarymod", the file will be named CanaryMod-#.#.#-#.#.#.jar   where the # s are the current version number; make a note of the version number, you will need this later.

Rename the downloaded .jar file from CanaryMod-#.#.#-#.#.#.jar  to  CanaryMod.jar .

Open TextEdit and insert the following text:

#!/bin/bash
cd "$( dirname "$0" )"
java -Xmx1024M -jar Canarymod.jar

Save the file in TextEdit to the Canarymod folder as start_server.command.

The start_server.command file is a command program which will startup the Bukkit server when it is run, it needs to be made executable.

Open Terminal, and type the following command, BUT do not press enter:

chmod a+x

Drag the start_server.command into Terminal and hit enter

Double-click the start_server.command file to run it and startup Canarymod.

The first time you start you will be asked to agree to the EULA.

Open the eula.txt file in the Canarymod folder:
Change  eula=false  to  eula=true
Save the file and run the start_server.command file again.

When you want to start your Minecraft Canarymod server in the future you can double click on the start_server.command file.

To stop Canarymod, enter the word  stop  into the command window and press Enter.

 - Configure Canarymod
 ----------------------
Open TextEdit, click File, Open and goto the Canarymod folder open the following files and make the changes below:

Open config\server.cfg
Change:
 -  online-mode=true  to  online-mode=false  so you dont need to be connected to the internet to use Canarymod

Open config\worlds\default\default_NORMAL.cfg
Change:
 -  gamemode=0  to  gamemode=1  to change the server from survival to creative
 -  spawn-protection=16  to  spawn-protection=0  so the spawn area can be built on
 -  spawn-villagers=true  to  spawn-villagers=false  to turn off mobs
 -  spawn-golems=true  to  spawn-golems=false
 -  spawn-animals=true  to  spawn-animals=false
 -  spawn-monsters=true  to  spawn-monsters=false

 - Give players permissions
 ----------------------
By default no players have permissions in Canarymod.  To give yourself admin permissions on the server type:

playermod group add playersname admins

e.g.  playermod group add martinohanlon admins

in the Canarymod command window.

 - Create StartCanarymod.command
 ----------------------
Open TextEdit and add the following text:

#!/bin/bash
echo "Adventures In Minecraft"
echo "Canarymod Minecraft Server Version is #.#.#"
echo "  Note - make sure Minecraft is using #.#.#"
echo "Press any key to continue"
read -n 1 -s
cd "$( dirname "$0" )"
cd Canarymod
./start_server.command

Replace #.#.# with the version number of Canarymod you downloaded.

Save the folder as StartCanarymod.command to the MyAdventures folder

Open Terminal, and type the following command, BUT do not press enter:

chmod a+x

Drag the StartCanarymod.command into Terminal and hit enter

 - Install RaspberryJuice
 ----------------------
RaspberryJuice is a plugin for Canarymod which will allow you to write programs which will change the Minecraft world as you are playing, just like the API which comes with Minecraft: Pi Edition on the Raspberry Pi.

Goto https://github.com/martinohanlon/canaryraspberryjuice and download the raspberry juice plugin and source code.

From the jars folder copy the raspberryjuice-#-#.jar plugin to the plugins folder in the Canarymod folder.


Setup MyAdventures folder
----------------------
Download mcpi(*) from github https://github.com/martinohanlon/mcpi
   * - the mcpi folder contains the python library supplied by mojang with Minecraft: Pi Edition and the minecraftstuff library (github.com/martinohanlon/minecraft-stuff) by Martin O'Hanlon 

Copy the mcpi folder to AdventuresInMinecraft/MyAdventures

Download anyio from github https://github.com/whaleygeek/anyio

Copy the anyio folder to AdventuresInMinecraft/MyAdventures

Copy the findPort.py file to AdventuresInMinecraft/MyAdventures
-------------------------------