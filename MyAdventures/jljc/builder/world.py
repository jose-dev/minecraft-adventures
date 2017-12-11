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


def main():
    Pond.build_pond(Y=-1, Xo=40, Xi=110, Zo=0, Zi= 50,
                    factor_z=4, factor_x=6)



if __name__ == '__main__':
    main()