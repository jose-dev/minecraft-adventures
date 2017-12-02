from jljc.printer_3d.coordinate_utils import CoordinateUtils
import unittest
import copy

from mcpi.vec3 import Vec3



class TestCoordinateUtils(unittest.TestCase):
    def test_find_vertices(self):
        a = Vec3(10, 20, 30)
        b = Vec3(0, -10, 50)

        result = CoordinateUtils._find_vertices(a, b)

        self.assertEquals(result[0].x, 0)
        self.assertEquals(result[0].y, -10)
        self.assertEquals(result[0].z, 30)
        self.assertEquals(result[1].x, 10)
        self.assertEquals(result[1].y, 20)
        self.assertEquals(result[1].z, 50)


    def test_calculate_relative_coordinates(self):
        datain = {'box': {'min': {'x': 10, 'y': 15, 'z': 20}, 'max': {'x': 20, 'y': 25, 'z': 30}},
                  'data':[{'coord': {'x': 10, 'y': 15, 'z': 20}, 'block': {'id': 1, 'data': 0}},
                          {'coord': {'x': 20, 'y': 25, 'z': 30}, 'block': {'id': 1, 'data': 0}}]}
        expected = {'box': {'min': {'x': 0, 'y': 0, 'z': 0}, 'max': {'x': 10, 'y': 10, 'z': 10}},
                    'data':[{'coord': {'x': 0, 'y': 0, 'z': 0}, 'block': {'id': 1, 'data': 0}},
                            {'coord': {'x': 10, 'y': 10, 'z': 10}, 'block': {'id': 1, 'data': 0}}]}
        saved = copy.deepcopy(datain)

        result = CoordinateUtils.calculate_relative_coordinates(datain)

        self.assertDictEqual(result, expected)
        self.assertDictEqual(saved, datain)


    def test_shift_coordinates(self):
        datain = {'box': {'min': {'x': 0, 'y': 0, 'z': 0}, 'max': {'x': 10, 'y': 10, 'z': 10}},
                  'data':[{'coord': {'x': 0, 'y': 0, 'z': 0}, 'block': {'id': 1, 'data': 0}},
                          {'coord': {'x': 10, 'y': 10, 'z': 10}, 'block': {'id': 1, 'data': 0}}]}
        expected = {'box': {'min': {'x': 10, 'y': 15, 'z': 20}, 'max': {'x': 20, 'y': 25, 'z': 30}},
                    'data':[{'coord': {'x': 10, 'y': 15, 'z': 20}, 'block': {'id': 1, 'data': 0}},
                            {'coord': {'x': 20, 'y': 25, 'z': 30}, 'block': {'id': 1, 'data': 0}}]}
        saved = copy.deepcopy(datain)

        result = CoordinateUtils.shift_coordinates(datain, Vec3(10, 15, 20))

        self.assertDictEqual(result, expected)
        self.assertDictEqual(saved, datain)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCoordinateUtils)
    unittest.TextTestRunner(verbosity=2).run(suite)