import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

time.sleep(5)
pos = mc.player.getTilePos()
mc.postToChat("x: {0} y: {1} z: {2}".format(str(pos.x),
                                            str(pos.y),
                                            str(pos.z)))


"""

 lines up TNT and then explodes after a while:

    does not dissappear with explosion:
        - BEDROCK

    does disappear with explosion:
        - SANDSTONE



"""


"""

#
# exploding with a delay
#
time.sleep(2)

x = pos.x + 2
y = pos.y
z = pos.z


FACTOR = 3
STEPS = 10
SLEEP_SECONDS = .1
TIMER_SECONDS = 1

mc.postToChat("adding deactivated TNT...")
for n in range(0, 10):
    time.sleep(SLEEP_SECONDS)
    rx = x + n * FACTOR
    mc.setBlock(rx, y - 1, z, block.SANDSTONE.id, block.SANDSTONE.data)
    mc.setBlock(rx, y, z, block.TNT.id, 0)

mc.postToChat("exploting TNT in ")
time.sleep(2)

mc.postToChat("activating TNT...")
for n in range(0, 10):
    time.sleep(TIMER_SECONDS)
    rx = x + n * FACTOR
    mc.setBlock(rx + 1, y - 1, z, block.SANDSTONE.id, block.SANDSTONE.data)
    mc.setBlock(rx + 1, y, z, block.REDSTONE_TORCH_ACTIVE.id)

"""

#
# exploding without a delay
#
time.sleep(2)

x = pos.x + 2
y = pos.y
z = pos.z


FACTOR = 3
STEPS = 10
SLEEP_SECONDS = .1
TIMER_SECONDS = 1

mc.postToChat("adding activated TNT...")
for n in range(0, 10):
    time.sleep(SLEEP_SECONDS)
    rx = x + n * FACTOR
    mc.setBlock(rx, y - 1, z, block.SANDSTONE.id, block.SANDSTONE.data)
    mc.setBlock(rx, y, z, block.TNT.id, 0)
    mc.setBlock(rx + 1, y - 1, z, block.SANDSTONE.id, block.SANDSTONE.data)
    mc.setBlock(rx + 1, y, z, block.REDSTONE_TORCH_ACTIVE.id)


