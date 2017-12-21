import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3
import os
import random
import time
import datetime
import numpy
import argparse


from jljc.printer_3d.coordinate_utils import CoordinateUtils
from jljc.printer_3d.scan_print_3d import ScanPrint3D


mc = minecraft.Minecraft.create()
scanner = ScanPrint3D(mc)

NUMBER_OF_MINUTES = 15
NUMBER_OF_SECONDS = NUMBER_OF_MINUTES * 60
NUMBER_OF_DIAMONDS = 7
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
    '3': {'where': 'village', 'coord': Vec3(-18, 1, 52)},
    '4': {'where': 'village', 'coord': Vec3(-40, 10, 39)},
    '5': {'where': 'village', 'coord': Vec3(-13, 5, 42)},
    '6': {'where': 'village', 'coord': Vec3(-24, 1, 37)},
    '7': {'where': 'forest', 'coord': Vec3(-70, 0, 18)},
    '8': {'where': 'forest', 'coord': Vec3(-100, 13, 19)},
    '9': {'where': 'forest', 'coord': Vec3(-90, 0, 83)},
    '10': {'where': 'talia_mansion', 'coord': Vec3(-107, 13, 144)},
    '11': {'where': 'talia_mansion', 'coord': Vec3(-126, 13, 148)},
    '12': {'where': 'talia_mansion', 'coord': Vec3(-121, 9, 150)},
    '13': {'where': 'talia_mansion', 'coord': Vec3(-113, 9, 137)},
    '14': {'where': 'talia_mansion', 'coord': Vec3(-129, 9, 138)},
    '15': {'where': 'talia_mansion', 'coord': Vec3(-118, 9, 151)},
    '16': {'where': 'talia_mansion', 'coord': Vec3(-120, 6, 137)},
    '17': {'where': 'talia_mansion', 'coord': Vec3(-129, 5, 135)},
    '18': {'where': 'talia_mansion', 'coord': Vec3(-129, 5, 144)},
    '19': {'where': 'talia_mansion', 'coord': Vec3(-123, 0, 143)},
    '20': {'where': 'talia_mansion', 'coord': Vec3(-107, 1, 144)},
    '21': {'where': 'forest', 'coord': Vec3(-130, 0, 193)},
    '22': {'where': 'forest', 'coord': Vec3(-127, 11, 206)},
    '23': {'where': 'selina_mansion', 'coord': Vec3(-115, 18, 249)},
    '24': {'where': 'selina_mansion', 'coord': Vec3(-129, 13, 236)},
    '25': {'where': 'selina_mansion', 'coord': Vec3(-116, 14, 254)},
    '26': {'where': 'selina_mansion', 'coord': Vec3(-113, 13, 254)},
    '27': {'where': 'selina_mansion', 'coord': Vec3(-119, 13, 254)},
    '28': {'where': 'selina_mansion', 'coord': Vec3(-109, 9, 244)},
    '29': {'where': 'selina_mansion', 'coord': Vec3(-128, 9, 235)},
    '30': {'where': 'selina_mansion', 'coord': Vec3(-128, 9, 243)},
    '31': {'where': 'selina_mansion', 'coord': Vec3(-126, 9, 250)},
    '32': {'where': 'selina_mansion', 'coord': Vec3(-106, 9, 254)},
    '33': {'where': 'selina_mansion', 'coord': Vec3(-106, 7, 246)},
    '34': {'where': 'selina_mansion', 'coord': Vec3(-123, 5, 244)},
    '35': {'where': 'selina_mansion', 'coord': Vec3(-111, 2, 254)},
    '36': {'where': 'selina_mansion', 'coord': Vec3(-139, 2, 245)},
    '37': {'where': 'forest', 'coord': Vec3(-22, 0, 307)},
    '38': {'where': 'forest', 'coord': Vec3(20, 0, 275)},
    '39': {'where': 'pond', 'coord': Vec3(0, 0, 241)},
    '40': {'where': 'pond', 'coord': Vec3(13, 0, 222)},
    '41': {'where': 'pond', 'coord': Vec3(-4, -1, 209)},
    '42': {'where': 'pond', 'coord': Vec3(-41, 0, 178)},

}


def choose_hidden_diamonds(n=NUMBER_OF_DIAMONDS):
    chosen = {}
    ids = POTENTIAL_HIDDEN_DIAMONDS.keys()
    while len(chosen) < n:
        id = random.choice(ids)
        if id not in chosen:
            chosen[id] = POTENTIAL_HIDDEN_DIAMONDS[id]
    return chosen


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



def play():
    """

    TODO

    the data within DATA_FILE should be level (e.g. 'village', 'selina_mansion', 'explorer', etc
    so just one single obj can be selected for explosion (for testing purposes).

    """


    mc.postToChat("Hidding the diamonds ...")
    diamonds = choose_hidden_diamonds()
    place_hidden_diamonds(diamonds)

    mc.postToChat("Let's search for the diamonds, the clock is ticking...")
    all_found = diamond_quest_was_successful(diamonds, NUMBER_OF_SECONDS)
    if all_found:
        mc.postToChat("Well done - the city is saved - good-bye aliens...")
        what_to_explode = DATA['spaceship_fleet']
    else:
        mc.postToChat("Oh no - get out quickly - the city is about to explode...")
        what_to_explode = DATA['city']

    explode(what_to_explode)



if __name__ == '__main__':
    ## parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--number_minutes", help="Number of minutes the search will last",
                        type=float, default=NUMBER_OF_MINUTES)
    parser.add_argument("-d", "--number_diamonds", help="Number of diamonds to search for",
                        type=int, default=NUMBER_OF_DIAMONDS)
    parser.add_argument("-p", "--multiplayer", help="Multiplayer mode", action="store_true")
    args = parser.parse_args()

    ## vaidatig arguments
    NUMBER_OF_SECONDS = int(args.number_minutes * 60)
    NUMBER_OF_DIAMONDS = args.number_diamonds

    ## play game
    play()