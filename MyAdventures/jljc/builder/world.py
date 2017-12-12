import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3
import os
import random

from jljc.printer_3d.coordinate_utils import CoordinateUtils
from jljc.printer_3d.scan_print_3d import ScanPrint3D
from jljc.builder.landscape import Pond, Forest


mc = minecraft.Minecraft.create()
scanner = ScanPrint3D(mc)


BASE_PATH = os.path.dirname(__file__)
RESOURCES_PATH = os.path.join(BASE_PATH, '..', '..', 'resources')
DATA_FILES = {
    'mansion_hill': os.path.join(RESOURCES_PATH, 'scans', 'houses', 'mansion_hill_001.json'),
    'talia_mansion': os.path.join(RESOURCES_PATH, 'scans', 'houses', 'talia_mansion_001.json'),
}
DATA = {}
for d in DATA_FILES:
    DATA[d] = CoordinateUtils.read_data_from_file(DATA_FILES[d])



def main():
    """
    TODO:

    all the coordinates should be saved in a data structure
    that can be shared between classes

    :return:
    """

    ## build Talia's mansion
    x = -140
    y = 0
    z = 120
    v = Vec3(x, y, z)
    scanner.print_3d(CoordinateUtils.shift_coordinates(DATA['mansion_hill'], v))
    v = Vec3(x + 4, -5, z + 8)
    scanner.print_3d(CoordinateUtils.shift_coordinates(DATA['talia_mansion'], v))


    ## build pond
    Xo = -38
    Zo = 150
    Xi = Xo + 50
    Zi = Zo + 70
    Pond.build_pond(Y=-1, Xo=Xo, Xi=Xi, Zo=Zo, Zi= Zi,
                    factor_z=6, factor_x=4)



if __name__ == '__main__':
    main()