import time

import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3

from jljc.builder.spaceship import Spaceship
from jljc.printer_3d.coordinate_utils import CoordinateUtils
from jljc.printer_3d.scan_print_3d import ScanPrint3D

SCAN_DATA = {
    #'command': {
    #    'file': 'command_ship_001.json',
    #    'coord': [Vec3(90, 119, -238), Vec3(160, 130, -116)]
    #},
    'explorer': {
        'file': 'explorer_ship_001.json',
        'coord': [Vec3(81, 119, -235), Vec3(94, 130, -200)]
    },
    #'mother': {
    #    'file': 'mother_ship_001.json',
    #    'coord': [Vec3(198, 119, -238), Vec3(276, 130, -116)]
    #}
}

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
    Xo = 82
    Yo= 120
    Zo = -234


    ### build some ships
    #spaceship_builder = Spaceship()
    #spaceship_builder.build_explorer_ship(Vec3(Xo, Yo, Zo),
    #                                      [block.GLOWSTONE_BLOCK, block.OBSIDIAN, block.OBSIDIAN, block.GLOWSTONE_BLOCK],
    #                                      [block.OBSIDIAN])
    #spaceship_builder.build_mother_ship(Vec3(Xo+150, Yo, Zo),
    #                                    [block.GLOWSTONE_BLOCK, block.OBSIDIAN, block.OBSIDIAN, block.GLOWSTONE_BLOCK],
    #                                    [block.OBSIDIAN])
    #spaceship_builder.build_command_ship(Vec3(Xo+40, Yo, Zo),
    #                                    [block.GLOWSTONE_BLOCK, block.OBSIDIAN, block.OBSIDIAN, block.GLOWSTONE_BLOCK],
    #                                    [block.OBSIDIAN])


    ## scan ships
    for md in SCAN_DATA:
        print("Scanning {}...".format(md))
        v1 = SCAN_DATA[md]['coord'][0]
        v2 = SCAN_DATA[md]['coord'][1]
        data_file = SCAN_DATA[md]['file']
        data = scanner.scan_3d(v1, v2)
        data = CoordinateUtils.calculate_relative_coordinates(data)
        CoordinateUtils.save_data_to_file(data, data_file)


    ### build ships
    v = Vec3(0, 20, -100)
    for md in SCAN_DATA:
        print("Printing {}...".format(md))
        data_file = SCAN_DATA[md]['file']
        data = CoordinateUtils.read_data_from_file(data_file)
        data = CoordinateUtils.shift_coordinates(data, v)
        scanner.print_3d(data)
        v.y += 20



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


