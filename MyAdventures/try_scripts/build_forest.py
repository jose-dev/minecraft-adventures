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
Y = -1
Xo = -175
Xi = -125
Zo = 0
Zi = 50

factor = 2

## bedrock base
print("Build pond...")
for i in range(0, 6):
    v1 = Vec3(Xo, Y, Zo)
    v2 = Vec3(Xi, Y, Zi)
    mc.setBlocks(v1.x,
                 v1.y,
                 v1.z,
                 v2.x,
                 v2.y,
                 v2.z,
                 block.WATER_STATIONARY)
    Xo -= factor
    Xi -= factor
    Zo += factor
    Zi += factor
