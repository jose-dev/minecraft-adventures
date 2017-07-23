import mcpi.minecraft as minecraft
import mcpi.block as block
import time


LENGTH = 20
WIDTH  = 20
HEIGHT = 4


mc = minecraft.Minecraft.create()


time.sleep(10)
pos = mc.player.getTilePos()
mc.postToChat("this is the center of the area...")
mc.postToChat("x: {0} y: {1} z: {2}".format(str(pos.x),
                                            str(pos.y),
                                            str(pos.z)))
time.sleep(10)
mc.postToChat("building solid dome")
mc.setBlocks(pos.x - int(LENGTH / 2) - 1,
             pos.y - 1,
             pos.z - int(WIDTH / 2),
             pos.x + int(LENGTH / 2) + 1,
             pos.y + HEIGHT + 1,
             pos.z + int(WIDTH / 2),
             block.WATER.id)

for i in range(11):
    time.sleep(1)
    posa = mc.player.getTilePos()
    mc.postToChat("x: {0} y: {1} z: {2}".format(str(posa.x),
                                                str(posa.y),
                                                str(posa.z)))

mc.postToChat("emptying dome")
mc.setBlocks(pos.x - int(LENGTH / 2),
             pos.y,
             pos.z - int(WIDTH / 2),
             pos.x + int(LENGTH / 2),
             pos.y + HEIGHT,
             pos.z + int(WIDTH / 2),
             block.AIR.id)