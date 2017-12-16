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
RESOURCES_PATH = os.path.join(BASE_PATH, '..', '..', 'resources', 'scans', 'spaceships')
DATA_FILES = {
    'command':  os.path.join(RESOURCES_PATH, 'command_ship_001.json'),
    'explorer': os.path.join(RESOURCES_PATH, 'explorer_ship_001.json'),
    'mother':   os.path.join(RESOURCES_PATH, 'mother_ship_001.json'),
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


    ## build comand ship 1
    x = -140
    y = 60
    z = 50
    v = Vec3(x, y, z)
    command_data = CoordinateUtils.shift_coordinates(DATA['command'], v)
    scanner.print_3d(command_data)
    exclude.append(command_data['box'])


    ## build mother
    x = -40
    y = 60
    z = 50
    v = Vec3(x, y, z)
    mother_data = CoordinateUtils.shift_coordinates(DATA['mother'], v)
    scanner.print_3d(mother_data)
    exclude.append(mother_data['box'])


    ## build comand ship 2
    x = 60
    y = 60
    z = 50
    v = Vec3(x, y, z)
    command_data = CoordinateUtils.shift_coordinates(DATA['command'], v)
    scanner.print_3d(command_data)
    exclude.append(command_data['box'])


    ## build explorer ships
    x = -130
    y = 60
    Zs = [200, 250]
    gap_x = 30
    for i in range(0, 8):
        for z in Zs:
            v = Vec3(x, y, z)
            explorer_data = CoordinateUtils.shift_coordinates(DATA['explorer'], v)
            scanner.print_3d(explorer_data)
            exclude.append(explorer_data['box'])
        x += gap_x



if __name__ == '__main__':
    main()