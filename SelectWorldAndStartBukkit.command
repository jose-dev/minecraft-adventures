#!/bin/bash
echo "Adventures In Minecraft"
echo "Bukkit Minecraft Server Version is 1.6.4"
echo "  Note - make sure Minecraft is using 1.6.4"


SERVERFILE="server.properties"
WORLDS=("test_world" "flat_world")
cd "$( dirname "$0" )"


# read chosen world
echo "Enter name of world: "
read worldname


# check that world exists
case "${WORLDS[@]}" in
    *"${worldname}"*)
        echo "World chosen: ${worldname}"
        ;;
    *)
     echo "${worldname} is an Invalid world"
     exit 1
esac



echo "Preparing world..."
cd Bukkit
# first directories
for i in "" "_nether" "_the_end"; do
    new="${worldname}${i}"
    src="worlds/${worldname}/${new}"
    if [ ! -d "$src" ]; then
      echo "[ERROR] Directory $src does not exist..."
      exit 1
    fi
    if [ -d "$new" ]; then
      rm -rf  ${new}
    fi
    cp -r ${src} ${new}
done
# then server.properties
worldproperties="worlds/${worldname}/${worldname}-${SERVERFILE}"
if [ -e "$worldproperties" ]; then
    cp -r ${worldproperties} ${SERVERFILE}
else
    echo "[ERROR] File $worldproperties does not exist..."
    exit 1
fi
cd -


# launching server
./StartBukkit.command