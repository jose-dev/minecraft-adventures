import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from mcpi.vec3 import Vec3
import os
import random

from jljc.printer_3d.coordinate_utils import CoordinateUtils
from jljc.printer_3d.scan_print_3d import ScanPrint3D



SCAN_FILE = 'tree002_fixed.json'
TREE_PATH = '../resources/scans/trees'
TREE_FILE = 'tree002.json'
TREE_DATA = CoordinateUtils.read_data_from_file((os.path.join(TREE_PATH, TREE_FILE)))



mc = minecraft.Minecraft.create()
scanner = ScanPrint3D(mc)



time.sleep(2)
pos = mc.player.getTilePos()
mc.postToChat("x: {0} y: {1} z: {2}".format(str(pos.x),
                                            str(pos.y),
                                            str(pos.z)))


## starting coordinates
Xo = -100
Y = 0
Zo = 0

### original tree
#print("Printing original tree...")
#v = Vec3(Xo, Y, Zo)
#data = CoordinateUtils.shift_coordinates(TREE_DATA, v)
#scanner.print_3d(data)


#### scan fixed tree
print("Scanning {}...")
v1 = Vec3(-103, 0, 3)
v2 = Vec3(-87, 29, 15)
data_file = SCAN_FILE
data = scanner.scan_3d(v1, v2)
data = CoordinateUtils.calculate_relative_coordinates(data)
CoordinateUtils.save_data_to_file(data, data_file)


#### print fixed tree
v = Vec3(Xo, Y, Zo + 50)
print("Printing {}...")
data_file = SCAN_FILE
data = CoordinateUtils.read_data_from_file(data_file)
data = CoordinateUtils.shift_coordinates(data, v)
scanner.print_3d(data)


