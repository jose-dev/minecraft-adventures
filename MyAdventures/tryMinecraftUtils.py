import time
import csv

import mcpi.minecraft as minecraft
import mcpi.minecraftutils as minecraftutils
import mcpi.block as block

mc = minecraft.Minecraft.create()
mcutils = minecraftutils.MinecraftUtils(mc)

carpet = mcutils.read_csv_drawing('../carpets/rainbow.csv')

print(carpet)
print("number of rows: " + str(len(carpet)))
print("number of columns: " + str(len(carpet[0])))

for i in range(0, 10):
    time.sleep(1)
    pos = mc.player.getTilePos()
    mcutils.log_to_console("x: {0} y: {1} z: {2}".format(str(pos.x),
                                                str(pos.y),
                                                str(pos.z)))



#mcutils.log_to_console("doing sculpture...")
#mcutils.make_sculpture(pos, carpet)

mcutils.log_to_console("doing picture...")
mcutils.make_picture(pos, carpet)

#mcutils.log_to_console("doing carpet...")
#mcutils.make_carpet(pos, carpet)





