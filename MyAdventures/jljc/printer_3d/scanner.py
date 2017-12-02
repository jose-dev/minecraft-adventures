import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3
import time
import pprint
import copy


#mc = minecraft.Minecraft.create()
#
#
#
#
#def find_player_position():
#    pos = mc.player.getTilePos()
#    mc.postToChat("player is at x: {0} y: {1} z: {2}".format(str(pos.x),
#                                                             str(pos.y),
#                                                             str(pos.z)))


class Scanner3D(object):
    def __init__(self, mc):
        self.mc = mc

    def scan(self, v1, v2):
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







"""
    TODO
    -------


    * print3d(calculated_data)

        print building (it usually takes as input the output of
        calculate_coord_to_print3d())


"""




if __name__ == "__main__":
    #while True:
    #    find_player_position()
    #    time.sleep(1)


    ## scan tree
    #v1 = Vec3(49, 15, 29)
    #v2 = Vec3(37, 27, 39)
    #scanner = Scanner3D(mc)
    #data = scanner.scan(v1, v2)
    #pprint.pprint(data)

    pass



