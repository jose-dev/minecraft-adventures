import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3
import os
import random

from jljc.printer_3d.coordinate_utils import CoordinateUtils
from jljc.printer_3d.scan_print_3d import ScanPrint3D


mc = minecraft.Minecraft.create()
scanner = ScanPrint3D(mc)


class Pond(object):
    factor_x = 6
    factor_z = 4
    N = 6

    @staticmethod
    def build_pond(Xo=None, Xi=None, Y=None, Zo=None, Zi=None,
                   factor_x=factor_x, factor_z=factor_z, N=N):
        out = {'min':{'x': Xo, 'y': Y},
               'max': {'x': Xi, 'y': Y}}
        for i in range(1, N+1):
            v1 = Vec3(Xo, Y, Zo)
            v2 = Vec3(Xi, Y, Zi)
            mc.setBlocks(v1.x,
                         v1.y,
                         v1.z,
                         v2.x,
                         v2.y,
                         v2.z,
                         block.WATER_STATIONARY)
            Xo += factor_x
            Xi -= factor_x
            Zo -= factor_z
            Zi += factor_z
        out['min']['z'] = Zo
        out['max']['z'] = Zi
        return out



class Forest(object):
    BASE_PATH = os.path.dirname(__file__)
    RESOURCES_PATH = os.path.join(BASE_PATH, '..', '..', 'resources')

    EXCLUDE_DISTANCE = 10
    TREE_GAP = 15
    TREE_RANDOM_GAP = range(-3, 3)
    TREE_DATA = {}
    TREE_PATH = os.path.join(RESOURCES_PATH, 'scans', 'trees')
    TREES = ['tree001.json', 'tree002.json']
    for t in TREES:
        TREE_DATA[t] = CoordinateUtils.read_data_from_file((os.path.join(TREE_PATH, t)))


    @classmethod
    def grow_forest(cls, Xo=None, Xe=None, Y=None, Zo=None, Ze=None, exclude=None):
        for i in range(Xo, Xe, cls.TREE_GAP):
            for j in range(Zo, Ze, cls.TREE_GAP):
                tree = random.choice(cls.TREES)
                tree_data = cls.TREE_DATA[tree]

                x = i + random.choice(cls.TREE_RANDOM_GAP)
                z = j + random.choice(cls.TREE_RANDOM_GAP)
                v = Vec3(x, Y, z)

                if not cls.is_within_excluded(v, exclude):
                    data = CoordinateUtils.shift_coordinates(tree_data, v)
                    scanner.print_3d(data)


    @classmethod
    def is_within_excluded(cls, v=None, exclude=None):
        for ex in exclude:
            if ex['min']['x'] - cls.EXCLUDE_DISTANCE <= v.x <= ex['max']['x'] + cls.EXCLUDE_DISTANCE \
                    and ex['min']['z'] - cls.EXCLUDE_DISTANCE <= v.z <= ex['max']['z'] + cls.EXCLUDE_DISTANCE:
                return True
        return False
