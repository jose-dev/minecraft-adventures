import unittest
import random

from platform.platformer import StaticPlatformer


class TestStaticPlatformer(unittest.TestCase):
    def setUp(self):
        random.seed(13)

    def test_default_platform(self):
        result = StaticPlatformer()
        self.assertEqual(len(result.get_block_positions()), len(list(set(result.get_block_positions()))))
        self.assertEqual(0, len(result.get_block_directions()))
        self.assertListEqual([], result.get_block_directions())

    def test_basic_custom_platform(self):
        result = StaticPlatformer(number_blocks=10)
        self.assertEqual(10, len(result.get_block_positions()))
        self.assertEqual(len(result.get_block_positions()), len(list(set(result.get_block_positions()))))
        self.assertEqual(0, len(result.get_block_directions()))
        self.assertListEqual([], result.get_block_directions())

    def test_platform_requires_odd_block_sizes_raises_error(self):
        try:
            StaticPlatformer(block_size=2)
            self.assertTrue(False)
        except AssertionError as e:
            self.assertTrue(True)
            self.assertEqual(e.message, 'Invalid block size')

    def test_platform_with_custom_positions(self):
        result = StaticPlatformer(number_blocks=10, positions=[(2, 3), (3, 4)])
        self.assertEqual(2, len(result.get_block_positions()))
        self.assertTrue(result.block_position_exists((2, 3)))
        self.assertListEqual([(2, 3), (3, 4)], result.get_block_positions())
        self.assertEqual(0, len(result.get_block_directions()))

    def test_platform_with_custom_positions_and_directions(self):
        result = StaticPlatformer(number_blocks=10, positions=[(2, 3), (3, 4)], directions=[(0, 1), (1, 0)])
        self.assertEqual(2, len(result.get_block_positions()))
        self.assertTrue(result.block_position_exists((2, 3)))
        self.assertListEqual([(2, 3), (3, 4)], result.get_block_positions())
        self.assertListEqual([], result.get_block_directions())

    def test_a_single_block_does_not_move_after_one_iteration_successfully(self):
        platform = StaticPlatformer(positions=[(2, 1)])
        platform.move_blocks()
        self.assertEqual(1, len(platform.get_block_positions()))
        self.assertTrue(platform.block_position_exists((2, 1)))
        self.assertListEqual([(2, 1)], platform.get_block_positions())
        self.assertListEqual([], platform.get_block_directions())

    def test_a_single_block_does_not_move_after_two_iterations_successfully(self):
        platform = StaticPlatformer(positions=[(3, 1)])
        for i in range(2):
            platform.move_blocks()
        self.assertEqual(1, len(platform.get_block_positions()))
        self.assertListEqual([(3, 1)], platform.get_block_positions())
        self.assertListEqual([], platform.get_block_directions())

    def test_two_blocks_do_not_move_after_one_iteration_successfully(self):
        platform = StaticPlatformer(positions=[(2, 1), (3, 2)])
        platform.move_blocks()
        self.assertEqual(2, len(platform.get_block_positions()))
        self.assertListEqual([(2, 1), (3, 2)], platform.get_block_positions())
        self.assertListEqual([], platform.get_block_directions())

    def test_two_blocks_do_not_move_two_iterations_successfully(self):
        platform = StaticPlatformer(positions=[(3, 1), (3, 2)])
        for i in range(2):
            platform.move_blocks()
        self.assertEqual(2, len(platform.get_block_positions()))
        self.assertListEqual([(3, 1), (3, 2)], platform.get_block_positions())
        self.assertListEqual([], platform.get_block_directions())

    def test_two_blocks_do_not_move_30_iterations_successfully(self):
        platform = StaticPlatformer(positions=[(3, 1), (3, 2)])
        for i in range(30):
            platform.move_blocks()
            self.assertEqual(2, len(platform.get_block_positions()))
            self.assertListEqual([(3, 1), (3, 2)], platform.get_block_positions())

    def test_10_blocks_move_30_iterations_successfully(self):
        platform = StaticPlatformer(number_blocks=10)
        for i in range(30):
            platform.move_blocks()
            self.assertEqual(10, len(platform.get_block_positions()))
            self.assertEqual(len(platform.get_block_positions()), len(list(set(platform.get_block_positions()))))

    def test_10_blocks_of_bigger_size_move_30_iterations_successfully(self):
        platform = StaticPlatformer(number_blocks=10, block_size=3)
        for i in range(30):
            platform.move_blocks()
            self.assertEqual(10, len(platform.get_block_positions()))
            self.assertEqual(len(platform.get_block_positions()), len(list(set(platform.get_block_positions()))))
