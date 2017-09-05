#!/bin/bash
echo "Adventures In Minecraft"
echo "Bukkit Minecraft Server Version is 1.6.4"
echo "  Note - make sure Minecraft is using 1.6.4"


SERVERFILE="server.properties"
WORLDS=("world" "WoodieWooRocks" "flat_world")
cd "$( dirname "$0" )"


# read world to save
echo "Enter name of world to be saved: "
read worldtosave


# check that world exists
case "${WORLDS[@]}" in
    *"${worldtosave}"*)
        echo "Saving the ${worldtosave} world"
        ;;
    *)
     echo "World does not exist: ${worldtosave}"
     exit 1
esac


# read name of new world
echo "Enter name of new world: "
read newworld
# check that world exists
case "${WORLDS[@]}" in
    *"${newworld}"*)
        echo "There is already a ${newworld} world"
        echo "would you like to overwrite? (y/n) "
        read overwrite
        case ${overwrite} in
            y)
                echo "Existing world will be overwritten"
                ;;
            *)
                echo "Nothing done"
                exit 0
         esac
        ;;
    *)
        echo "Saving as: ${newworld}"
esac


echo "Saving world..."
cd Bukkit
targetdir="worlds/${newworld}"
if [ ! -d "$targetdir" ]; then
    mkdir $targetdir
fi
# first directories
for i in "" "_nether" "_the_end"; do
    src="${worldtosave}${i}"
    new="${targetdir}/${newworld}${i}"
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
worldproperties="${targetdir}/${newworld}-${SERVERFILE}"
cp -r ${SERVERFILE} ${worldproperties}
if [ ! "${worldtosave}" = "${newworld}" ]; then
    echo "Updating level-name in server.properties file..."
    sed -i -- "s/level-name=${worldtosave}/level-name=${newworld}/g" ${worldproperties}
fi
cd -

