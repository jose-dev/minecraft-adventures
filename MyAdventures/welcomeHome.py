import mcpi.minecraft as minecraft
import time

X1 = -173
X2 = -170
Z1 = -16
Z2 = -9
Y1 = -1


mc = minecraft.Minecraft.create()
mc.player.setPos(X1, Y1, Z1)

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    mc.postToChat("x: {0} y: {1} z: {2}".format(str(pos.x),
                                                str(pos.y),
                                                str(pos.z)))
    if X1 <= pos.x <= X2 and Z1 <= pos.z <= Z2 and pos.y < Y1:
        mc.postToChat("In hole!!!!")
    else:
        mc.postToChat("Out of the whole")

