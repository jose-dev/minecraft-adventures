import time

import mcpi.minecraft as minecraft
from mcpi.vec3 import Vec3

from jljc.printer_3d.coordinate_utils import CoordinateUtils
from jljc.printer_3d.scan_print_3d import ScanPrint3D


DATA_FILE = 'tree_coord.json'

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




    ### box coordinates for tree to scan
    #v1 = Vec3(122, 3, -361)
    #v2 = Vec3(133, 31, -348)
    ##mc.player.setPos(v1.x, v1.y, v1.z)

    ### scan tree
    #data = scanner.scan_3d(v1, v2)
    #data = CoordinateUtils.calculate_relative_coordinates(data)
    #CoordinateUtils.save_data_to_file(data, DATA_FILE)

    ## point to grow tree
    v = Vec3(107, 0, -273)
    #mc.player.setPos(v.x, v.y, v.z)

    ### plant tree
    #data = CoordinateUtils.read_data_from_file(DATA_FILE)
    #data = CoordinateUtils.shift_coordinates(data, v)
    #scanner.print_3d(data)

    ## plant forest
    gap_x = -20
    orig_data = CoordinateUtils.read_data_from_file(DATA_FILE)
    gap_x += -1 * (orig_data['box']['max']['z'] - orig_data['box']['min']['z'])
    for i in range(0, 5):
        data = CoordinateUtils.shift_coordinates(orig_data, v)
        scanner.print_3d(data)
        v.x += gap_x
        time.sleep(3)



    """

    #### DADDY's TREE

    ## box coordinates for tree to scan
    v1 = Vec3(49, 15, 29)
    v2 = Vec3(37, 27, 39)
    #mc.player.setPos(v1.x, v1.y, v1.z)

    ### scam tree
    #data = scanner.scan_3d(v1, v2)
    #data = CoordinateUtils.calculate_relative_coordinates(data)
    #CoordinateUtils.save_data_to_file(data, DATA_FILE)

    ## point to grow tree
    v = Vec3(69, 0, -250)
    #mc.player.setPos(v.x, v.y, v.z)

    ## plant tree
    data = CoordinateUtils.read_data_from_file(DATA_FILE)
    data = CoordinateUtils.shift_coordinates(data, v)
    scanner.print_3d(data)

    ## plant forest
    gap_x = -10
    orig_data = CoordinateUtils.read_data_from_file(DATA_FILE)
    for i in range(0, 5):
        data = CoordinateUtils.shift_coordinates(orig_data, v)
        scanner.print_3d(data)
        v.x += gap_x
        time.sleep(3)


    """





