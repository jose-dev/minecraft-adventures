import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3
import os
import random
import time
import datetime
import numpy

from jljc.printer_3d.coordinate_utils import CoordinateUtils
from jljc.printer_3d.scan_print_3d import ScanPrint3D


mc = minecraft.Minecraft.create()
scanner = ScanPrint3D(mc)

BLOCK_ID = block.DIAMOND_BLOCK.id
BASE_PATH = os.path.dirname(__file__)
RESOURCES_PATH = os.path.join(BASE_PATH, '..', 'resources', 'scans', 'game')
DATA_FILES = {
    'city':  os.path.join(RESOURCES_PATH, 'city_world_002.json'),
    'spaceship_fleet':  os.path.join(RESOURCES_PATH, 'spaceship_fleet_001.json'),
}
DATA = {}
for d in DATA_FILES:
    DATA[d] = CoordinateUtils.read_data_from_file(DATA_FILES[d])



POTENTIAL_HIDDEN_DIAMONDS = {
    '1': {'where': 'village', 'coord': Vec3(20, 0, 56)},
    '2': {'where': 'village', 'coord': Vec3(1, 0, 78)},
}


def choose_hidden_diamonds(n=2):
    return POTENTIAL_HIDDEN_DIAMONDS


def place_hidden_diamonds(data):
    for i in data:
        v = data[i]['coord']
        mc.setBlock(v.x, v.y, v.z, BLOCK_ID, 0)


def _explode_box(obj, what='city'):
    STEPS = 1
    xo = obj['box']['min']['x']
    xe = obj['box']['max']['x']
    zo = obj['box']['min']['z']
    ze = obj['box']['max']['z']
    number_of_levels = 1 if 'levels' not in obj else obj['levels']
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


def _explode_coord(obj, what='city'):
    STEPS = 1
    count = 1
    bomb = 0
    for coord in obj['data']:
        point = coord['coord']
        if count % STEPS == 0 and coord['block']['id'] != 0:
            b = block.TNT.id if bomb % 5 == 0 else block.REDSTONE_TORCH_ACTIVE.id
            mc.setBlock(point['x'], point['y'] + 1, point['z'], b, 0)
            bomb += 1
        count += 1



def explode(data, what='city'):
    print("Explode stuff...")

    mc.postToChat("adding activated TNT...")
    for obj in data:
        if 'data' in obj:
            SLEEP_BETWEEN_OBJECTS_SECONDS = 10
            _explode_coord(obj)
        else:
            SLEEP_BETWEEN_OBJECTS_SECONDS = 20
            _explode_box(obj)
        time.sleep(SLEEP_BETWEEN_OBJECTS_SECONDS)


def _euclidian_distance(va, vb):
    a = numpy.array((va.x, va.y, va.z))
    b = numpy.array((vb.x, vb.y, vb.z))
    return numpy.linalg.norm(a-b)


def _distance_to_next_diamond(player_pos, diamond_pos):
    return Vec3(diamond_pos.x - player_pos.x,
                diamond_pos.y - player_pos.y,
                diamond_pos.z - player_pos.z)


def diamond_quest_was_successful(diamonds, no_seconds=30):
    start = datetime.datetime.now()
    found = {}
    while (datetime.datetime.now()-start).total_seconds() <= no_seconds and len(diamonds) > len(found):
        player_pos = mc.player.getTilePos()
        shortest_distance = 999999999999
        closest_diamond = None
        for i in diamonds:
            if i in found:
                continue
            v = diamonds[i]['coord']
            if mc.getBlock(v.x, v.y, v.z) != BLOCK_ID:
                found[i] = 1
                mc.postToChat("Diamonds remaining: {}".format(str(len(diamonds) - len(found))))
            else:
                dist = _euclidian_distance(player_pos, v)
                if shortest_distance > dist:
                    shortest_distance = dist
                    closest_diamond = i
        if len(diamonds) > len(found):
            pos_to_next_diamond = _distance_to_next_diamond(player_pos, diamonds[closest_diamond]['coord'])
            seconds_remaining = int(no_seconds - (datetime.datetime.now()-start).total_seconds())
            mc.postToChat("Closest diamond x: {0} y: {1} z: {2} - Seconds remaining: {3}" \
                          .format(str(pos_to_next_diamond.x),
                                  str(pos_to_next_diamond.y),
                                  str(pos_to_next_diamond.z),
                                  str(seconds_remaining)))
            time.sleep(.5)
    return len(diamonds) == len(found)



def main():


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


    mc.postToChat("Hidding the diamonds ...")
    diamonds = choose_hidden_diamonds()
    place_hidden_diamonds(diamonds)

    mc.postToChat("Let's search for the diamonds, the clock is ticking...")
    all_found = diamond_quest_was_successful(diamonds, 60)
    if all_found:
        mc.postToChat("Well done - the city is saved - good-bye aliens...")
        what_to_explode = DATA['spaceship_fleet']
    else:
        mc.postToChat("Oh no - get out quickly - the city is about to explode...")
        what_to_explode = DATA['city']


    #time.sleep(10)
    #pos = mc.player.getTilePos()
    #mc.postToChat("x: {0} y: {1} z: {2}".format(str(pos.x),
    #                                            str(pos.y),
    #                                            str(pos.z)))

    explode(what_to_explode)






if __name__ == '__main__':
    main()