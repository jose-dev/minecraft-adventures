import mcpi.minecraft as minecraft
import mcpi.block as block
import time


mc = minecraft.Minecraft.create()


# this is to make room for the house
#
LENGTH_TO_CLEAR = 40 * 1
WIDTH_TO_CLEAR  = 40 * 1
HEIGHT_TO_CLEAR = 24

time.sleep(10)
pos = mc.player.getTilePos()
mc.postToChat("this is the center of the area to be cleared")
mc.postToChat("x: {0} y: {1} z: {2}".format(str(pos.x),
                                            str(pos.y),
                                            str(pos.z)))
time.sleep(10)
mc.postToChat("clearing the area")
mc.setBlocks(pos.x,
             pos.y,
             pos.z,
             pos.x + LENGTH_TO_CLEAR,
             pos.y + HEIGHT_TO_CLEAR,
             pos.z + WIDTH_TO_CLEAR,
             block.AIR.id)


# let's build the first floor
HOUSE = 0
OFFSET = int(LENGTH_TO_CLEAR / 4)
X1 = pos


