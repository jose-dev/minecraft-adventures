import time

import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3

from jljc.builder.house import House
from jljc.printer_3d.coordinate_utils import CoordinateUtils
from jljc.printer_3d.scan_print_3d import ScanPrint3D


STARTING_MANSION_DATA = 'mansion_003.json'
MANSION_DATA = 'talia_mansion_001.json'


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



    ##### initial coordinates
    Xo = -166
    Yo= 0
    Zo = 34

    ##### build original mansion on top of ground
    v = Vec3(Xo, Yo, Zo)
    print("Printing ...")
    data_file = STARTING_MANSION_DATA
    data = CoordinateUtils.read_data_from_file(data_file)
    data = CoordinateUtils.shift_coordinates(data, v)
    scanner.print_3d(data)


    ###### scan mansion
    #print("Scanning ...")
    #v1 = Vec3(Xo, Yo, Zo)
    #v2 = Vec3(-129, 24, 67)
    #data_file = MANSION_DATA
    #data = scanner.scan_3d(v1, v2)
    #data = CoordinateUtils.calculate_relative_coordinates(data)
    #CoordinateUtils.save_data_to_file(data, data_file)



    #### build mansion
    #x = 40
    #y = 0
    #z  = 0
    #v = Vec3(x, y, z)
    #print("Printing ...")
    #data_file = MANSION_DATA
    #data = CoordinateUtils.read_data_from_file(data_file)
    #data = CoordinateUtils.shift_coordinates(data, v)
    #scanner.print_3d(data)




