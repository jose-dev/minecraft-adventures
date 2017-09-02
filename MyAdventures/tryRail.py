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



"""
#
# this works to add tracks in zig-zag
#
#
time.sleep(2)
mc.postToChat("building a zig-zag rail track...")

x = pos.x + 2
y = pos.y
z = pos.z

for dy in range(0, 3):
    for dz in range(0, 3):
        for dx in range(0, 3):
            mc.postToChat("adding track {}".format(str(dx)))
            time.sleep(.5)
            mc.setBlock(x, y - 1, z, block.BEDROCK.id, block.BEDROCK.data)
            mc.setBlock(x, y, z, block.RAIL_NORMAL.id, block.RAIL_NORMAL.data)
            x += 1
        z += 1
        x -= 1
    y += 1
    z -= 1
"""



"""
#
# this works to build a closed tracks
#
#
time.sleep(2)
mc.postToChat("building a closed rail track...")

x = pos.x + 2
y = pos.y
z = pos.z


STEPS = 5
for dx in range(0, STEPS):
    mc.postToChat("adding track {}".format(str(dx)))
    time.sleep(.5)
    mc.setBlock(x, y - 1, z, block.BEDROCK.id, block.BEDROCK.data)
    mc.setBlock(x, y, z, block.RAIL_NORMAL.id, block.RAIL_NORMAL.data)
    x += 1
x -= 1

for dz in range(0, STEPS):
    mc.postToChat("adding track {}".format(str(dx)))
    time.sleep(.5)
    mc.setBlock(x, y - 1, z, block.BEDROCK.id, block.BEDROCK.data)
    mc.setBlock(x, y, z, block.RAIL_NORMAL.id, block.RAIL_NORMAL.data)
    z += 1
z -= 1

for dx in range(0, STEPS):
    mc.postToChat("adding track {}".format(str(dx)))
    time.sleep(.5)
    mc.setBlock(x, y - 1, z, block.BEDROCK.id, block.BEDROCK.data)
    mc.setBlock(x, y, z, block.RAIL_NORMAL.id, block.RAIL_NORMAL.data)
    x -= 1
x += 1

for dz in range(0, STEPS):
    mc.postToChat("adding track {}".format(str(dx)))
    time.sleep(.5)
    mc.setBlock(x, y - 1, z, block.BEDROCK.id, block.BEDROCK.data)
    mc.setBlock(x, y, z, block.RAIL_NORMAL.id, block.RAIL_NORMAL.data)
    z -= 1
z += 1

"""

#
# this works to build a spirally rail track
#
#
time.sleep(2)
mc.postToChat("building a spirally rail track...")

x = pos.x + 2
y = pos.y
z = pos.z


STEPS = 10
for n in range(0, 4):
    for dx in range(0, STEPS):
        mc.postToChat("adding track {}".format(str(dx)))
        time.sleep(.5)
        mc.setBlock(x, y - 1, z, block.BEDROCK.id, block.BEDROCK.data)
        mc.setBlock(x, y, z, block.RAIL_NORMAL.id, block.RAIL_NORMAL.data)
        x += 1
    x -= 1

    for dz in range(0, STEPS):
        mc.postToChat("adding track {}".format(str(dx)))
        time.sleep(.5)
        mc.setBlock(x, y - 1, z, block.BEDROCK.id, block.BEDROCK.data)
        mc.setBlock(x, y, z, block.RAIL_NORMAL.id, block.RAIL_NORMAL.data)
        z += 1
    z -= 1

    for dx in range(0, STEPS):
        mc.postToChat("adding track {}".format(str(dx)))
        time.sleep(.5)
        mc.setBlock(x, y - 1, z, block.BEDROCK.id, block.BEDROCK.data)
        mc.setBlock(x, y, z, block.RAIL_NORMAL.id, block.RAIL_NORMAL.data)
        x -= 1
    x += 1

    for dz in range(0, STEPS):
        mc.postToChat("adding track {}".format(str(dx)))
        time.sleep(.5)
        id = block.RAIL_NORMAL.id
        data = block.RAIL_NORMAL.data
        if 1 < dz < STEPS - 1:
            y += 1
            id = block.RAIL_GOLDEN.id
            data = block.RAIL_GOLDEN.data

        mc.setBlock(x, y - 1, z, block.BEDROCK.id, block.BEDROCK.data)
        mc.setBlock(x, y, z, id, data)
        z -= 1
    z += 1


