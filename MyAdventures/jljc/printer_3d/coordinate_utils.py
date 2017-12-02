from mcpi.vec3 import Vec3
import copy
import json



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
    def calculate_relative_coordinates(data):
        min = data['box']['min']

        out = copy.deepcopy(data)

        # recalculate box coordinates
        for t in ['min', 'max']:
            for coord in min:
                out['box'][t][coord] -= min[coord]

        # recalculate block coordinates
        for i in range(0, len(data['data'])):
            for coord in min:
                out['data'][i]['coord'][coord] -= min[coord]

        return out


    @staticmethod
    def shift_coordinates(data, new_min=None):
        min = {'x': new_min.x, 'y': new_min.y, 'z': new_min.z}

        out = copy.deepcopy(data)

        # recalculate box coordinates
        for t in ['min', 'max']:
            for coord in min:
                out['box'][t][coord] += min[coord]

        # recalculate block coordinates
        for i in range(0, len(data['data'])):
            for coord in min:
                out['data'][i]['coord'][coord] += min[coord]

        return out


    @staticmethod
    def read_data_from_file(filein):
        with open(filein) as json_data:
            out = json.load(json_data)
        return out


    @staticmethod
    def save_data_to_file(data, fileout):
        with open(fileout, 'w') as json_file:
            json.dump(data, json_file)



    """
        TODO
        -------


        * mirrored_data = mirror_data(data, coord='x')

            mirror data according to algorithm described in notepad.


    """


