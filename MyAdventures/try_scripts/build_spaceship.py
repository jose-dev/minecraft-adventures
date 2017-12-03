import time

import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3

from jljc.printer_3d.coordinate_utils import CoordinateUtils
from jljc.printer_3d.scan_print_3d import ScanPrint3D


DATA_FILE = 'space_ship_001.json'
SPACE_SHIP = [
    [
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,1,1,0,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,0,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0]
    ],
    [
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,1,0,0,0],
        [0,0,1,1,0,0,0,1,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,1,0,0,0,1,1,0,0],
        [0,0,0,1,1,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0]
    ],
    [
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,1,0,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,0,1,1,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0]
    ],
    [
        [0,0,0,0,1,1,1,0,0,0,0],
        [0,0,1,1,0,0,0,1,1,0,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [1,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,0,1,1,0,0,0,1,1,0,0],
        [0,0,0,0,1,1,1,0,0,0,0]
    ],
    [
        [0,0,0,1,1,1,1,1,0,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [1,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,0,1,1,1,1,1,0,0,0]
    ]
]


mc = minecraft.Minecraft.create()
scanner = ScanPrint3D(mc)



def find_player_position():
    pos = mc.player.getTilePos()
    mc.postToChat("player is at x: {0} y: {1} z: {2}".format(str(pos.x),
                                                             str(pos.y),
                                                             str(pos.z)))



if __name__ == "__main__":
    #while True:
    for i in range(0, 5):
        find_player_position()
        time.sleep(1)


    ## starting coordiantes
    Xo = 112
    Yo= 20
    Zo = -234

    ## build spaceship
    z = Zo
    for layer in SPACE_SHIP:
        for i in range(0, len(layer)):
            y = Yo + i
            for j in range(0, len(layer[i])):
                x = Xo + j
                b = block.IRON_BLOCK if layer[i][j] == 1 else block.AIR
                mc.setBlock(x, y, z, b.id, b.data)
        z -= 1

    for n in range(0, 2):
        layer = SPACE_SHIP[-1]
        for i in range(0, len(layer)):
            y = Yo + i
            for j in range(0, len(layer[i])):
                x = Xo + j
                b = block.IRON_BLOCK if layer[i][j] == 1 else block.AIR
                mc.setBlock(x, y, z, b.id, b.data)
        z -= 1

    for n in reversed(range(0, len(SPACE_SHIP))):
        layer = SPACE_SHIP[n]
        for i in range(0, len(layer)):
            y = Yo + i
            for j in range(0, len(layer[i])):
                x = Xo + j
                b = block.IRON_BLOCK if layer[i][j] == 1 else block.AIR
                mc.setBlock(x, y, z, b.id, b.data)
        z -= 1


    for n in range(0, 7):
        layer = SPACE_SHIP[0]
        for i in range(0, len(layer)):
            y = Yo + i
            for j in range(0, len(layer[i])):
                x = Xo + j
                b = block.IRON_BLOCK if layer[i][j] == 1 else block.AIR
                mc.setBlock(x, y, z, b.id, b.data)
        z -= 1

    for layer in SPACE_SHIP:
        for i in range(0, len(layer)):
            y = Yo + i
            for j in range(0, len(layer[i])):
                x = Xo + j
                b = block.IRON_BLOCK if layer[i][j] == 1 else block.AIR
                mc.setBlock(x, y, z, b.id, b.data)
        z -= 1

    for n in range(0, 2):
        layer = SPACE_SHIP[-1]
        for i in range(0, len(layer)):
            y = Yo + i
            for j in range(0, len(layer[i])):
                x = Xo + j
                b = block.IRON_BLOCK if layer[i][j] == 1 else block.AIR
                mc.setBlock(x, y, z, b.id, b.data)
        z -= 1

    for n in reversed(range(0, len(SPACE_SHIP))):
        layer = SPACE_SHIP[n]
        for i in range(0, len(layer)):
            y = Yo + i
            for j in range(0, len(layer[i])):
                x = Xo + j
                b = block.IRON_BLOCK if layer[i][j] == 1 else block.AIR
                mc.setBlock(x, y, z, b.id, b.data)
        z -= 1


        ### box coordinates for house to scan
    #v1 = Vec3(120, 0, -217)
    #v2 = Vec3(128, 4, -208)

    ### scan house
    #data = scanner.scan_3d(v1, v2)
    #data = CoordinateUtils.calculate_relative_coordinates(data)
    #CoordinateUtils.save_data_to_file(data, DATA_FILE)

    ### point to house
    #v = Vec3(112, 0, -234)

    ### build house
    #data = CoordinateUtils.read_data_from_file(DATA_FILE)
    #data = CoordinateUtils.shift_coordinates(data, v)
    #scanner.print_3d(data)

    ### build street
    #gap_z = -10
    #orig_data = CoordinateUtils.read_data_from_file(DATA_FILE)

    #import pprint
    #pprint.pprint(orig_data)

    #gap_z += -1 * (orig_data['box']['max']['z'] - orig_data['box']['min']['z'])
    #for i in range(0, 10):
    #    print(v)
    #    data = CoordinateUtils.shift_coordinates(orig_data, v)
    #    scanner.print_3d(data)
    #    v.z += gap_z
    #    time.sleep(3)


