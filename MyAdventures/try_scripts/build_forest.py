import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from mcpi.vec3 import Vec3
import os
import random

from jljc.printer_3d.coordinate_utils import CoordinateUtils
from jljc.printer_3d.scan_print_3d import ScanPrint3D




TREE_GAP = 15
TREE_RANDOM_GAP = range(-3, 3)
TREE_DATA = {}
TREE_PATH = '../resources/scans/trees'
TREES = ['tree001.json', 'tree002.json']
for t in TREES:
    TREE_DATA[t] = CoordinateUtils.read_data_from_file((os.path.join(TREE_PATH, t)))



mc = minecraft.Minecraft.create()
scanner = ScanPrint3D(mc)



time.sleep(2)
pos = mc.player.getTilePos()
mc.postToChat("x: {0} y: {1} z: {2}".format(str(pos.x),
                                            str(pos.y),
                                            str(pos.z)))


## starting coordinates
Y = 0

Xo = -200
Zo = 0

Xe = -100
Ze = 100


## bedrock base
print("Growing forest...")
for i in range(Xo, Xe, TREE_GAP):
    for j in range(Zo, Ze, TREE_GAP):
        tree = random.choice(TREES)
        tree_data = TREE_DATA[tree]

        x = i + random.choice(TREE_RANDOM_GAP)
        z = j + random.choice(TREE_RANDOM_GAP)
        v = Vec3(x, Y, z)

        data = CoordinateUtils.shift_coordinates(tree_data, v)
        scanner.print_3d(data)
