import mcpi.minecraft as minecraft
import mcpi.block as block
import time


LENGTH = 10 * 1
WIDTH  = 10 * 1
HEIGHT = -8


mc = minecraft.Minecraft.create()


time.sleep(10)
pos = mc.player.getTilePos()
mc.postToChat("this is the center of the area to be cleared")
mc.postToChat("x: {0} y: {1} z: {2}".format(str(pos.x),
                                            str(pos.y),
                                            str(pos.z)))
time.sleep(10)
mc.postToChat("clearing the area")
mc.setBlocks(pos.x - int(LENGTH / 2),
             pos.y,
             pos.z - int(WIDTH / 2),
             pos.x + int(LENGTH / 2),
             pos.y + HEIGHT,
             pos.z + int(WIDTH / 2),
             block.AIR.id)