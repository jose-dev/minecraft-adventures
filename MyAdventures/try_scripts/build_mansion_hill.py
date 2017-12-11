import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from mcpi.vec3 import Vec3

from jljc.printer_3d.coordinate_utils import CoordinateUtils
from jljc.printer_3d.scan_print_3d import ScanPrint3D


MANSION_HILL_DATA = 'mansion_hill_001.json'
MANSION_DATA = 'talia_mansion_001.json'


mc = minecraft.Minecraft.create()
scanner = ScanPrint3D(mc)



mc = minecraft.Minecraft.create()


time.sleep(2)
pos = mc.player.getTilePos()
mc.postToChat("x: {0} y: {1} z: {2}".format(str(pos.x),
                                            str(pos.y),
                                            str(pos.z)))


## starting coordinates
Yo = 0
Xo = 50
Xi = 100
Zo = 0
Zi = 50

factor_x = 1
factor_z = 1
factor_y = 1

### build hill
#print("Build mansion hill...")
#for i in range(0, 3+1):
#    v1 = Vec3(Xo, Yo, Zo)
#    v2 = Vec3(Xi, Yo, Zi)
#    mc.setBlocks(v1.x, v1.y, v1.z,
#                 v2.x, v2.y, v2.z,
#                 block.GRASS)
#    Xo += factor_x
#    Xi -= factor_x
#    Zo += factor_z
#    Zi -= factor_z
#    Yo += factor_y
#

###### filling gap left by mansion cellar
mc.setBlocks(Xo + 3, Yo + 3, Zo + 3,
             Xi - 3, Yo + 3, Zi - 3,
             block.GRASS)

###### scan mansion hill
print("Scanning ...")
v1 = Vec3(Xo, Yo, Zo)
v2 = Vec3(Xi + 1, 3, Zi + 1)
data_file = MANSION_HILL_DATA
data = scanner.scan_3d(v1, v2)
data = CoordinateUtils.calculate_relative_coordinates(data)
CoordinateUtils.save_data_to_file(data, data_file)




##### build mansion hill
x = Xo 
y = Yo
z  = Zo + 100
v = Vec3(x, y, z)
print("Printing ...")
data_file = MANSION_HILL_DATA
data = CoordinateUtils.read_data_from_file(data_file)
data = CoordinateUtils.shift_coordinates(data, v)
scanner.print_3d(data)


##### build mansion
#x = Xo + 4
#y = -5
#z  = Zo + 4
#v = Vec3(x, y, z)
#print("Printing ...")
#data_file = MANSION_DATA
#data = CoordinateUtils.read_data_from_file(data_file)
#data = CoordinateUtils.shift_coordinates(data, v)
#scanner.print_3d(data)
#