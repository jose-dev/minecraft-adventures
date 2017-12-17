import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3
import os
import random
import time

from jljc.printer_3d.coordinate_utils import CoordinateUtils
from jljc.printer_3d.scan_print_3d import ScanPrint3D


mc = minecraft.Minecraft.create()
scanner = ScanPrint3D(mc)


BASE_PATH = os.path.dirname(__file__)
RESOURCES_PATH = os.path.join(BASE_PATH, '..', 'resources', 'scans', 'game')
DATA_FILES = {
    'city':  os.path.join(RESOURCES_PATH, 'city_world_002.json'),
    'spaceship_fleet':  os.path.join(RESOURCES_PATH, 'spaceship_fleet_001.json'),
}
DATA = {}
for d in DATA_FILES:
    DATA[d] = CoordinateUtils.read_data_from_file(DATA_FILES[d])



def main():

    exclude = DATA['city']

    #exclude = []

    ## village
    #exclude.append({'box': {'min':{'x': -43, 'y': 0, 'z': 4},
    #                        'max': {'x': 30, 'y': 0, 'z': 88}}})
    #


    ### build houses
    #x = 40
    #y = -9
    #z = 120
    #for i in range(0, 4):
    #    v = Vec3(x, y, z)
    #    house_data = CoordinateUtils.shift_coordinates(DATA['house'], v)
    #    scanner.print_3d(house_data)
    #    z += 50
    #    exclude.append(house_data)


    ### build explorer ships
    #print("Build spaceship...")
    #x = 0
    #y = 40
    #z = 100
    #v = Vec3(x, y, z)
    #explorer_data = CoordinateUtils.shift_coordinates(DATA['explorer'], v)
    #scanner.print_3d(explorer_data)
    #exclude.append(explorer_data)


    ### build mother ships
    #print("Build spaceship...")
    #x = 40
    #y = 40
    #z = 100
    #v = Vec3(x, y, z)
    #mother_data = CoordinateUtils.shift_coordinates(DATA['mother'], v)
    #scanner.print_3d(mother_data)
    #exclude.append(mother_data)


    time.sleep(10)
    pos = mc.player.getTilePos()
    mc.postToChat("x: {0} y: {1} z: {2}".format(str(pos.x),
                                                str(pos.y),
                                                str(pos.z)))



    print("Explode stuff...")
    STEPS = 1

    mc.postToChat("adding activated TNT...")
    for obj in exclude:
        if 'data' in obj:
            SLEEP_BETWEEN_OBJECTS_SECONDS = 10

            count = 1
            bomb = 0
            for coord in obj['data']:
                point = coord['coord']
                if count % STEPS == 0 and coord['block']['id'] != 0:
                    b = block.TNT.id if bomb % 5 == 0 else block.REDSTONE_TORCH_ACTIVE.id
                    mc.setBlock(point['x'], point['y'] + 1, point['z'], b, 0)
                    bomb += 1
                count += 1
        else:
            SLEEP_BETWEEN_OBJECTS_SECONDS = 20

            xo = obj['box']['min']['x']
            xe = obj['box']['max']['x']
            zo = obj['box']['min']['z']
            ze = obj['box']['max']['z']
            number_of_levels = 1 if 'levels' not in obj else obj['levels']
            #print(number_of_levels)
            count = 1
            bomb = 0
            gap_y = 4
            for x in range(xo, xe):
                for z in range(zo, ze):
                    if count % STEPS == 0:
                        b = block.TNT.id if bomb % 4 == 0 else block.REDSTONE_TORCH_ACTIVE.id
                        for i in range(0, number_of_levels):
                            y = i * gap_y + 1
                            if y > 1:
                                mc.setBlock(x, y - 1, z, block.SANDSTONE.id, 0)
                            mc.setBlock(x, y, z, b, 0)
                        bomb += 1
                    count += 1

        time.sleep(SLEEP_BETWEEN_OBJECTS_SECONDS)




if __name__ == '__main__':
    main()