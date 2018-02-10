import unittest

from game.moving_platform import Plane


class TestPlane(unittest.TestCase):
    def test_default_plane(self):
        result = Plane()
        self.assertListEqual([0, 10], result.x_boundaries())
        self.assertListEqual([0, 10], result.z_boundaries())

    def test_custom_plane(self):
        result = Plane(x=[0, 2], z=[3, 5])
        self.assertListEqual([0, 2], result.x_boundaries())
        self.assertListEqual([3, 5], result.z_boundaries())
        self.assertEqual(0, result.west_edge())
        self.assertEqual(2, result.east_edge())
        self.assertEqual(3, result.south_edge())
        self.assertEqual(5, result.north_edge())
