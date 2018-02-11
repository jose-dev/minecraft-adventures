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


"""

HOW TO PLAY:
------------

    (1) --> set CREATIVE mode
        >gamemode 1 WoodieWooJr
        11:14:22 [INFO] CONSOLE: Set WoodieWooJr's game mode to CREATIVE mode

    (2) --> add a sword to inventory (plus other goodies you may want)

    (3) --> set SURVIVAL mode
        >gamemode 0 WoodieWooJr
        11:14:17 [INFO] CONSOLE: Set WoodieWooJr's game mode to SURVIVAL mode

    (4) --> start python script and play :)

        python game.py

"""

mc = minecraft.Minecraft.create()
scanner = ScanPrint3D(mc)

NUMBER_OF_MINUTES = 15
NUMBER_OF_SECONDS = NUMBER_OF_MINUTES * 60
NUMBER_OF_DIAMONDS = 7
BLOCK_ID = block.DIAMOND_BLOCK.id
BASE_PATH = os.path.dirname(__file__)
RESOURCES_PATH = os.path.join(BASE_PATH, '..', 'resources', 'scans', 'game')
DATA_FILES = {
    'city':  os.path.join(RESOURCES_PATH, 'xmas_2017_game_world_city.json'),
    'spaceship_fleet':  os.path.join(RESOURCES_PATH, 'xmas_2017_game_world_spaceship_fleet.json'),
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
    '43': {'where': 'forest', 'coord': Vec3(67, 0, 46)},
    '44': {'where': 'forest', 'coord': Vec3(89, 0, 53)},
    '45': {'where': 'forest', 'coord': Vec3(62, 28, 95)},
    '46': {'where': 'houses', 'coord': Vec3(72, 0, 125)},
    '47': {'where': 'houses', 'coord': Vec3(48, 2, 127)},
    '48': {'where': 'houses', 'coord': Vec3(64, 1, 129)},
    '49': {'where': 'houses', 'coord': Vec3(55, 5, 130)},
    '50': {'where': 'houses', 'coord': Vec3(57, 5, 131)},
    '51': {'where': 'forest', 'coord': Vec3(32, 0, 153)},
    '52': {'where': 'houses', 'coord': Vec3(54, 9, 178)},
    '53': {'where': 'houses', 'coord': Vec3(55, 9, 183)},
    '54': {'where': 'houses', 'coord': Vec3(49, 1, 181)},
    '55': {'where': 'houses', 'coord': Vec3(66, -1, 173)},
    '56': {'where': 'houses', 'coord': Vec3(63, -3, 180)},
    '57': {'where': 'houses', 'coord': Vec3(43, -3, 179)},
    '58': {'where': 'houses', 'coord': Vec3(62, 5, 181)},
    '59': {'where': 'houses', 'coord': Vec3(61, 5, 183)},
    '60': {'where': 'houses', 'coord': Vec3(53, 5, 177)},
    '61': {'where': 'houses', 'coord': Vec3(44, 6, 180)},
    '62': {'where': 'forest', 'coord': Vec3(53, 0, 210)},
    '63': {'where': 'forest', 'coord': Vec3(65, 12, 213)},
    '64': {'where': 'houses', 'coord': Vec3(68, 0, 232)},
    '65': {'where': 'houses', 'coord': Vec3(66, 9, 229)},
    '66': {'where': 'forest', 'coord': Vec3(36, 11, 226)},
    '67': {'where': 'houses', 'coord': Vec3(38, 0, 225)},
    '68': {'where': 'houses', 'coord': Vec3(43, 1, 230)},
    '69': {'where': 'houses', 'coord': Vec3(60, 1, 231)},
    '70': {'where': 'houses', 'coord': Vec3(53, -3, 226)},
    '71': {'where': 'houses', 'coord': Vec3(63, -3, 228)},
    '72': {'where': 'houses', 'coord': Vec3(65, 3, 223)},
    '73': {'where': 'houses', 'coord': Vec3(66, 5, 230)},
    '74': {'where': 'houses', 'coord': Vec3(57, 5, 231)},
    '75': {'where': 'houses', 'coord': Vec3(46, 5, 227)},
    '76': {'where': 'houses', 'coord': Vec3(46, 5, 230)},
    '77': {'where': 'forest', 'coord': Vec3(77, 2, 256)},
    '78': {'where': 'forest', 'coord': Vec3(85, 0, 258)},
    '79': {'where': 'forest', 'coord': Vec3(48, 0, 263)},
    '80': {'where': 'houses', 'coord': Vec3(53, 9, 279)},
    '81': {'where': 'houses', 'coord': Vec3(68, 0, 276)},
    '82': {'where': 'houses', 'coord': Vec3(64, 0, 283)},
    '83': {'where': 'houses', 'coord': Vec3(40, 0, 280)},
    '84': {'where': 'houses', 'coord': Vec3(48, 2, 278)},
    '85': {'where': 'houses', 'coord': Vec3(49, 1, 281)},
    '86': {'where': 'houses', 'coord': Vec3(63, 1, 276)},
    '87': {'where': 'houses', 'coord': Vec3(66, -1, 273)},
    '88': {'where': 'houses', 'coord': Vec3(65, -3, 279)},
    '89': {'where': 'houses', 'coord': Vec3(43, -3, 274)},
    '90': {'where': 'houses', 'coord': Vec3(66, 3, 273)},
    '91': {'where': 'houses', 'coord': Vec3(61, 5, 281)},
    '92': {'where': 'houses', 'coord': Vec3(61, 5, 273)},
    '93': {'where': 'houses', 'coord': Vec3(47, 5, 281)},
    '94': {'where': 'forest', 'coord': Vec3(35, 0, 299)},
    '95': {'where': 'forest', 'coord': Vec3(41, 4, 314)},
    '96': {'where': 'forest', 'coord': Vec3(32, 0, 317)},
    '97': {'where': 'forest', 'coord': Vec3(30, 12, 315)},
    '98': {'where': 'forest', 'coord': Vec3(23, 11, 301)},
    '99': {'where': 'forest', 'coord': Vec3(13, 0, 291)},
    '100': {'where': 'forest', 'coord': Vec3(-8, 0, 298)},

}


def choose_hidden_diamonds(n=NUMBER_OF_DIAMONDS):
    chosen = {}
    ids = POTENTIAL_HIDDEN_DIAMONDS.keys()
    while len(chosen) < n:
        id = random.choice(ids)
        if id not in chosen:
            chosen[id] = POTENTIAL_HIDDEN_DIAMONDS[id]
            print(chosen)
    return chosen


def place_hidden_diamonds(data):
    for i in data:
        v = data[i]['coord']
        mc.setBlock(v.x, v.y, v.z, BLOCK_ID, 0)


def _explode_box(obj):
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


def _explode_coord(obj):
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



def explode(data):
    print("Explode stuff...")

    mc.postToChat("adding activated TNT...")
    time.sleep(5)
    for obj in data:
        mc.postToChat("exploding a {}".format(obj['name']))
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

def _get_hits():
    hits = []
    events = mc.events.pollBlockHits()
    for e in events:
        hits.append(e.pos)
    return hits


def diamond_quest_was_successful(diamonds, no_seconds=30):
    start = datetime.datetime.now()
    found = {}
    while (datetime.datetime.now()-start).total_seconds() <= no_seconds and len(diamonds) > len(found):
        player_pos = mc.player.getTilePos()
        shortest_distance = 999999999999
        closest_diamond = None
        hits = _get_hits()
        for i in diamonds:
            if i in found:
                continue
            v = diamonds[i]['coord']
            if v in hits:
                found[i] = 1
                mc.setBlock(v.x, v.y, v.z, block.AIR.id, 0)
                mc.postToChat("Diamonds remaining: {}".format(str(len(diamonds) - len(found))))
            else:
                dist = _euclidian_distance(player_pos, v)
                if shortest_distance > dist:
                    shortest_distance = dist
                    closest_diamond = i
        if len(diamonds) > len(found):
            pos_to_next_diamond = _distance_to_next_diamond(player_pos, diamonds[closest_diamond]['coord'])
            diamonds_remaining = len(diamonds) - len(found)
            seconds_remaining = int(no_seconds - (datetime.datetime.now()-start).total_seconds())
            #mc.postToChat("Diamonds remaining: {} - Seconds remaining: {}" \
            #              .format(str(diamonds_remaining),
            #                      str(seconds_remaining)))
            mc.postToChat("Closest x: {0} y: {1} z: {2} - remaining d: {3} sec: {4}" \
                          .format(str(pos_to_next_diamond.x),
                                  str(pos_to_next_diamond.y),
                                  str(pos_to_next_diamond.z),
                                  str(diamonds_remaining),
                                  str(seconds_remaining)))
            time.sleep(.5)
    return len(diamonds) == len(found)


def select_for_test(data, value_name=None, key_name=None):
    if type(data) is dict:
        return _select_for_test_dict(data, value_name, 'where')
    else:
        return _select_for_test_array(data, value_name, 'name')


def _select_for_test_array(data, value_name=None, key_name='name'):
    selected = []
    for row in data:
        if key_name in row and row[key_name] == value_name:
            selected.append(row)
    return selected


def _select_for_test_dict(data, value_name=None, key_name=None):
    selected = {}
    for k in data:
        if key_name in data[k] and data[k][key_name] == value_name:
            selected[k] = data[k]
    return selected


def play():
    mc.postToChat("Hidding the diamonds ...")
    diamonds = choose_hidden_diamonds(NUMBER_OF_DIAMONDS)
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
    parser.add_argument("-t", "--test", help="Test mode", action="store_true")
    #parser.add_argument("-p", "--multiplayer", help="Multiplayer mode", action="store_true")
    args = parser.parse_args()

    ## validatig arguments
    NUMBER_OF_SECONDS = int(args.number_minutes * 60)
    NUMBER_OF_DIAMONDS = args.number_diamonds

    ## extract only a sub-set of data if running in test mode
    if args.test:
        POTENTIAL_HIDDEN_DIAMONDS = select_for_test(POTENTIAL_HIDDEN_DIAMONDS, 'village')
        DATA['city'] = select_for_test(DATA['city'], 'village')
        DATA['spaceship_fleet'] = select_for_test(DATA['spaceship_fleet'], 'mother')

    ## play game
    play()