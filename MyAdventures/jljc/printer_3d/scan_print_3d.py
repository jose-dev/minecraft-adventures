from mcpi.vec3 import Vec3
from coordinate_utils import CoordinateUtils



class ScanPrint3D(object):
    def __init__(self, mc):
        self.mc = mc

    def scan_3d(self, v1, v2):
        out = {'box': {}, 'data': []}

        # define box
        va, vb = CoordinateUtils._find_vertices(v1, v2)
        out['box']['min'] = {'x': va.x, 'y': va.y, 'z': va.z}
        out['box']['max'] = {'x': vb.x, 'y': vb.y, 'z': vb.z}

        # collect data
        for x in range(va.x, vb.x + 1):
            for z in range(va.z, vb.z + 1):
                for y in range(va.y, vb.y + 1):
                    v = Vec3(x, y, z)
                    b = self.mc.getBlockWithData(v)
                    out['data'].append({'coord': {'x': x, 'y': y, 'z': z},
                                        'block': {'id': b.id, 'data': b.data}})

        return out


    def print_3d(self, data):
        for b in data['data']:
            self.mc.setBlock(b['coord']['x'],
                             b['coord']['y'],
                             b['coord']['z'],
                             b['block']['id'],
                             b['block']['data'])




