from mcpi.vec3 import Vec3
import copy



class CoordinateUtils(object):

    @staticmethod
    def _find_lower_higher(a, b):
        return sorted([a, b])


    @staticmethod
    def _find_vertices(v1, v2):
        x1, x2 = CoordinateUtils._find_lower_higher(v1.x, v2.x)
        y1, y2 = CoordinateUtils._find_lower_higher(v1.y, v2.y)
        z1, z2 = CoordinateUtils._find_lower_higher(v1.z, v2.z)
        return [Vec3(x1, y1, z1),
                Vec3(x2, y2, z2)]


    @staticmethod
    def data_to_relative_coordinates(data):
        min = data['box']['min']

        out = copy.deepcopy(data)

        # recalculate box coordnantes
        for t in ['min', 'max']:
            for coord in min:
                out['box'][t][coord] -= min[coord]

        # recalculate block coordinates
        for i in range(0, len(data['data'])):
            for coord in min:
                out['data'][i]['coord'][coord] -= min[coord]

        return out



"""
    TODO
    -------


    * mirrored_data = mirror_data(data, coord='x')

        mirror data according to algorithm described in notepad.



    * data = calculate_coord_to_print3d(template, coord=Ve3(start_coords))

        calculate coordinates for building based on template and
        starting coordinated


"""


