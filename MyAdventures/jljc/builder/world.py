import mcpi.minecraft as minecraft
from mcpi.vec3 import Vec3
import os

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
    'selina_mansion': os.path.join(RESOURCES_PATH, 'scans', 'houses', 'selina_mansion_001.json'),
    'house': os.path.join(RESOURCES_PATH, 'scans', 'houses', 'house_004.json'),
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

    exclude = []

    ## build Talia's mansion
    x = -140
    y = 0
    z = 120
    v = Vec3(x, y, z)
    hill_data = CoordinateUtils.shift_coordinates(DATA['mansion_hill'], v)
    scanner.print_3d(hill_data)
    v = Vec3(x + 4, -5, z + 8)
    scanner.print_3d(CoordinateUtils.shift_coordinates(DATA['talia_mansion'], v))
    exclude.append(hill_data['box'])


    ## build pond
    Xo = -38
    Zo = 150
    Xi = Xo + 50
    Zi = Zo + 70
    exclude.append(Pond.build_pond(Y=-1, Xo=Xo, Xi=Xi, Zo=Zo, Zi= Zi,
                                   factor_z=6, factor_x=4))


    ## build Talia's mansion
    x = -140
    y = 0
    z = 220
    v = Vec3(x, y, z)
    hill_data = CoordinateUtils.shift_coordinates(DATA['mansion_hill'], v)
    scanner.print_3d(hill_data)
    v = Vec3(x + 4, -5, z + 8)
    scanner.print_3d(CoordinateUtils.shift_coordinates(DATA['selina_mansion'], v))
    exclude.append(hill_data['box'])


    ## build houses
    x = 40
    y = -9
    z = 120
    for i in range(0, 4):
        v = Vec3(x, y, z)
        house_data = CoordinateUtils.shift_coordinates(DATA['house'], v)
        scanner.print_3d(house_data)
        z += 50
        exclude.append(house_data['box'])


    ## village
    Xo = -43
    Zo = 4
    Xe = 30
    Ze = 88
    exclude.append({'min':{'x': Xo, 'y': 0, 'z': Zo},
                    'max': {'x': Xe, 'y': 0, 'z': Ze}})


    ## grow forest within world limits
    Xo = -150
    Xe = 80
    Zo = -4
    Ze = 320
    Forest.grow_forest(Xo, Xe, 0, Zo, Ze, exclude)


if __name__ == '__main__':
    main()