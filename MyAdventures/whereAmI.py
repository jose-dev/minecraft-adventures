import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    mc.postToChat("x: {0} y: {1} z: {2}".format(str(pos.x),
                                       str(pos.y),
                                       str(pos.z)))

