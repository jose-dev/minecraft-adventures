import mcpi.minecraft as minecraft
import mcpi.block as block
import time


HOUSE_SIZE = 20
HOUSE_HEIGHT = 10


mc = minecraft.Minecraft.create()

time.sleep(5)
pos = mc.player.getTilePos()
mc.postToChat("x: {0} y: {1} z: {2}".format(str(pos.x),
                                            str(pos.y),
                                            str(pos.z)))


LENGTH_TO_CLEAR = 40 * 2
WIDTH_TO_CLEAR  = 40 * 2
HEIGHT_TO_CLEAR = 40

time.sleep(2)
mc.postToChat("clearing area first")
mc.setBlocks(pos.x - int(LENGTH_TO_CLEAR / 2),
             pos.y,
             pos.z - int(WIDTH_TO_CLEAR / 2),
             pos.x + int(LENGTH_TO_CLEAR / 2),
             pos.y + HEIGHT_TO_CLEAR,
             pos.z + int(WIDTH_TO_CLEAR / 2),
             block.AIR.id)



time.sleep(2)
mc.postToChat("building the house")

x = pos.x + 2
y = pos.y
z = pos.z

midx = x + HOUSE_SIZE / 2
midy = y + HOUSE_HEIGHT / 2

time.sleep(1)
mc.postToChat("First the solid house")
mc.setBlocks(x, y, z, x + HOUSE_SIZE, y + HOUSE_HEIGHT, z + HOUSE_SIZE, block.DIAMOND_BLOCK.id)

time.sleep(1)
mc.postToChat("Second we empty the house")
mc.setBlocks(x + 1, y, z + 1, x + HOUSE_SIZE - 1, y + HOUSE_HEIGHT, z + HOUSE_SIZE - 1, block.AIR.id)


time.sleep(1)
mc.postToChat("`third we make whole for a door")
mc.setBlocks(midx - 1, y, z, midx, y + 1, z, block.AIR.id)


time.sleep(10)
mc.postToChat("`then we make put a door :)")
mc.setBlock(midx - 1, y, z, block.DOOR_WOOD.id, 0)
mc.setBlock(midx - 1, y + 1, z, block.DOOR_WOOD.id, 8)
mc.setBlock(midx, y, z, block.DOOR_WOOD.id, 1)
mc.setBlock(midx, y + 1, z, block.DOOR_WOOD.id,8)


