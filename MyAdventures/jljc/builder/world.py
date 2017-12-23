import mcpi.minecraft as minecraft
from mcpi.vec3 import Vec3
import os

from jljc.printer_3d.coordinate_utils import CoordinateUtils
from jljc.printer_3d.scan_print_3d import ScanPrint3D
from jljc.builder.landscape import Pond, Forest


mc = minecraft.Minecraft.create()
scanner = ScanPrint3D(mc)


CITY_WORLD = 'city_world_003.json'

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

    exclude = []
    coord_to_save = []

    ## build Talia's mansion
    x = -140
    y = 0
    z = 120
    v = Vec3(x, y, z)
    hill_data = CoordinateUtils.shift_coordinates(DATA['mansion_hill'], v)
    scanner.print_3d(hill_data)
    v = Vec3(x + 4, -5, z + 8)
    talia_mansion = CoordinateUtils.shift_coordinates(DATA['talia_mansion'], v)
    scanner.print_3d(talia_mansion)
    exclude.append(hill_data['box'])
    coord_to_save.append({'box': talia_mansion['box'], 'levels': 5, 'name': 'talia_mansion'})


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
    selina_mansion = CoordinateUtils.shift_coordinates(DATA['selina_mansion'], v)
    scanner.print_3d(selina_mansion)
    exclude.append(hill_data['box'])
    coord_to_save.append({'box': selina_mansion['box'], 'levels': 5, 'name': 'selina_mansion'})


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
        coord_to_save.append({'box': house_data['box'], 'levels': 3, 'name': 'houses'})


    ## village
    Xo = -43
    Zo = 4
    Xe = 30
    Ze = 88
    village = {'box': {'min':{'x': Xo, 'y': 0, 'z': Zo},
                       'max': {'x': Xe, 'y': 0, 'z': Ze}}, 'levels': 1, 'name': 'village'}
    exclude.append(village['box'])
    coord_to_save.append(village)


    ## save city coordinates
    CoordinateUtils.save_data_to_file(coord_to_save, CITY_WORLD)


    ## grow forest within world limits
    Xo = -150
    Xe = 80
    Zo = -4
    Ze = 320
    Forest.grow_forest(Xo, Xe, 0, Zo, Ze, exclude)



if __name__ == '__main__':
    main()