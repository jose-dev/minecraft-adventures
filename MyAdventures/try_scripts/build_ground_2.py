import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from mcpi.vec3 import Vec3



mc = minecraft.Minecraft.create()


time.sleep(2)
pos = mc.player.getTilePos()
mc.postToChat("x: {0} y: {1} z: {2}".format(str(pos.x),
                                            str(pos.y),
                                            str(pos.z)))


## starting coordinates
Xo = -200
Yo = 0
Zo = 0


## bedrock base
print("Prepare bedrock base...")
v1 = Vec3(Xo, Yo, Zo)
v2 = Vec3(v1.x + 100, v1.y + 7, v1.z + 100)
mc.setBlocks(v1.x,
             v1.y,
             v1.z,
             v2.x,
             v2.y,
             v2.z,
             block.BEDROCK)


## grass base
print("Prepare grass base...")
v11 = Vec3(Xo, v2.y + 1, Zo)
v22 = Vec3(v2.x, v11.y, v2.z)
mc.setBlocks(v11.x,
             v11.y,
             v11.z,
             v22.x,
             v22.y,
             v22.z,
             block.GRASS)


## rock slab base
print("Prepare rock slab base...")
v11 = Vec3(Xo, v2.y + 1, Zo)
v22 = Vec3(v2.x, v11.y, v2.z)
mc.setBlocks(v11.x,
             v11.y,
             v11.z,
             v22.x,
             v22.y,
             v22.z,
             block.STONE_SLAB)


