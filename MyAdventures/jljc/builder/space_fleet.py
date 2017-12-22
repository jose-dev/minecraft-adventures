import mcpi.minecraft as minecraft
from mcpi.vec3 import Vec3
import os

from jljc.printer_3d.coordinate_utils import CoordinateUtils
from jljc.printer_3d.scan_print_3d import ScanPrint3D


mc = minecraft.Minecraft.create()
scanner = ScanPrint3D(mc)


SPACESHIP_FLEET = 'spaceship_fleet_001.json'

BASE_PATH = os.path.dirname(__file__)
RESOURCES_PATH = os.path.join(BASE_PATH, '..', '..', 'resources', 'scans', 'spaceships')
DATA_FILES = {
    'command':  os.path.join(RESOURCES_PATH, 'command_ship_002.json'),
    'explorer': os.path.join(RESOURCES_PATH, 'explorer_ship_002.json'),
    'mother':   os.path.join(RESOURCES_PATH, 'mother_ship_002.json'),
}
DATA = {}
for d in DATA_FILES:
    DATA[d] = CoordinateUtils.read_data_from_file(DATA_FILES[d])



def main():
    coord_to_save = []


    ## build explorer ships
    x = -130
    y = 40
    Zs = [200, 250]
    gap_x = 30
    for i in range(0, 8):
        for z in Zs:
            v = Vec3(x, y, z)
            explorer_data = CoordinateUtils.shift_coordinates(DATA['explorer'], v)
            scanner.print_3d(explorer_data)
            coord_to_save.append(explorer_data)
            explorer_data['name'] = 'explorer'
        x += gap_x


    ## build comand ship 1
    x = -140
    y = 40
    z = 50
    v = Vec3(x, y, z)
    command_data = CoordinateUtils.shift_coordinates(DATA['command'], v)
    scanner.print_3d(command_data)
    command_data['name'] = 'command'
    coord_to_save.append(command_data)


    ## build comand ship 2
    x = 60
    y = 40
    z = 50
    v = Vec3(x, y, z)
    command_data = CoordinateUtils.shift_coordinates(DATA['command'], v)
    scanner.print_3d(command_data)
    command_data['name'] = 'command'
    coord_to_save.append(command_data)


    ## build mother
    x = -40
    y = 40
    z = 50
    v = Vec3(x, y, z)
    mother_data = CoordinateUtils.shift_coordinates(DATA['mother'], v)
    scanner.print_3d(mother_data)
    mother_data['name'] = 'mother'
    coord_to_save.append(mother_data)


    CoordinateUtils.save_data_to_file(coord_to_save, SPACESHIP_FLEET)

if __name__ == '__main__':
    main()