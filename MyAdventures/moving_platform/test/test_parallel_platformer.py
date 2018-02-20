import unittest
import random

from platform.platformer import ParallelPlatformer
from platform.plane import Plane


class ParallelTestPlatformer(unittest.TestCase):
    def setUp(self):
        random.seed(13)

    def test_calculate_gap_of_value_zero_with_block_size_of_one(self):
        result = ParallelPlatformer.calculate_gap(number_blocks=12, length=12, block_size=1)
        self.assertEqual(0, result)

    def test_calculate_gap_of_value_zero_with_block_size_larger_than_one(self):
        result = ParallelPlatformer.calculate_gap(number_blocks=4, length=12, block_size=3)
        self.assertEqual(0, result)

    def test_calculate_gap_of_value_one(self):
        result = ParallelPlatformer.calculate_gap(number_blocks=3, length=13, block_size=3)
        self.assertEqual(1, result)

    def test_fails_when_calculated_gap_is_not_integer(self):
        try:
            result = ParallelPlatformer.calculate_gap(number_blocks=3, length=12, block_size=3)
            self.assertTrue(False)
        except AssertionError as e:
            self.assertEqual(e.message, 'Gap size must be a whole number')

    def test_fails_when_calculated_gap_is_larger_than_maximum_allowed(self):
        try:
            result = ParallelPlatformer.calculate_gap(number_blocks=1, length=11, block_size=1)
            self.assertTrue(False)
        except AssertionError as e:
            self.assertEqual(e.message, 'Gap too wide')

    def test_default_platform(self):
        result = ParallelPlatformer()
        self.assertEqual(8, len(result.get_block_positions()))
        self.assertEqual(len(result.get_block_positions()), len(list(set(result.get_block_positions()))))
        self.assertEqual(len(result.get_block_positions()), len(result.get_block_directions()))

    def test_basic_custom_platform(self):
        result = ParallelPlatformer(number_blocks=4, plane=Plane(z=[0, 11]))
        self.assertEqual(4, len(result.get_block_positions()))
        self.assertEqual(len(result.get_block_positions()), len(list(set(result.get_block_positions()))))
        self.assertEqual(len(result.get_block_positions()), len(result.get_block_directions()))

    def test_platform_successfully_created_with_different_number_of_blocks_and_sizes(self):
        r = ParallelPlatformer(number_blocks=4, plane=Plane(z=[0, 11]))
        r = ParallelPlatformer(number_blocks=3, block_size=3, plane=Plane(z=[0, 11]))
        r = ParallelPlatformer(number_blocks=1, block_size=5, plane=Plane([0, 7], [0, 7]))

    def test_platform_leaves_gap_at_the_end_raises_error(self):
        try:
            r = ParallelPlatformer(number_blocks=1, block_size=3, plane=Plane(z=[0, 11]))
            print(r.__dict__)
            self.assertTrue(False)
        except AssertionError as e:
            self.assertTrue(True)
            self.assertEqual(e.message, 'Gap too wide')

    def test_platform_requires_odd_block_sizes_raises_error(self):
        try:
            ParallelPlatformer(block_size=2)
            self.assertTrue(False)
        except AssertionError as e:
            self.assertTrue(True)
            self.assertEqual(e.message, 'Invalid block size')

    def test_platform_with_custom_positions(self):
        result = ParallelPlatformer(number_blocks=10, positions=[(2, 3), (3, 4)])
        self.assertEqual(2, len(result.get_block_positions()))
        self.assertTrue(result.block_position_exists((2, 3)))
        self.assertListEqual([(2, 3), (3, 4)], result.get_block_positions())
        self.assertEqual(len(result.get_block_positions()), len(result.get_block_directions()))

    def test_platform_with_custom_positions_and_directions(self):
        result = ParallelPlatformer(number_blocks=10, positions=[(2, 3), (3, 4)], directions=[(-1, 0), (1, 0)])
        self.assertEqual(2, len(result.get_block_positions()))
        self.assertTrue(result.block_position_exists((2, 3)))
        self.assertListEqual([(2, 3), (3, 4)], result.get_block_positions())
        self.assertListEqual([(-1, 0), (1, 0)], result.get_block_directions())

    def test_block_will_hit_the_walls_in_the_next_move(self):
        platform = ParallelPlatformer(positions=[(1, 1)], directions=[(-1, 0)])
        result = platform.calculate_new_position((1, 1), (-1, 0))
        self.assertEqual((0, 1), result)
        self.assertFalse(platform.block_within_plane(result))

    def test_block_will_not_hit_the_walls_in_the_next_move(self):
        platform = ParallelPlatformer(positions=[(2, 1)], directions=[(-1, 0)])
        result = platform.calculate_new_position((2, 1), (-1, 0))
        self.assertEqual((1, 1), result)
        self.assertTrue(platform.block_within_plane(result))

    def test_block_of_bigger_size_will_hit_the_walls_in_the_next_move(self):
        platform = ParallelPlatformer(positions=[(2, 1)], directions=[(-1, 0)], block_size=3)
        result = platform.calculate_new_position((2, 1), (-1, 0))
        self.assertEqual((1, 1), result)
        self.assertFalse(platform.block_within_plane(result))

    def test_a_single_block_moves_one_iteration_successfully(self):
        platform = ParallelPlatformer(positions=[(2, 1)], directions=[(-1, 0)])
        platform.move_blocks()
        self.assertEqual(1, len(platform.get_block_positions()))
        self.assertTrue(platform.block_position_exists((1, 1)))
        self.assertListEqual([(1, 1)], platform.get_block_positions())
        self.assertListEqual([(-1, 0)], platform.get_block_directions())

    def test_a_single_block_moves_two_iterations_successfully(self):
        platform = ParallelPlatformer(positions=[(3, 1)], directions=[(-1, 0)])
        for i in range(2):
            platform.move_blocks()
        self.assertEqual(1, len(platform.get_block_positions()))
        self.assertTrue(platform.block_position_exists((1, 1)))
        self.assertListEqual([(1, 1)], platform.get_block_positions())
        self.assertListEqual([(-1, 0)], platform.get_block_directions())

    def test_two_blocks_move_one_iteration_successfully(self):
        platform = ParallelPlatformer(positions=[(2, 1), (3, 2)], directions=[(-1, 0), (1, 0)])
        platform.move_blocks()
        self.assertEqual(2, len(platform.get_block_positions()))
        self.assertTrue(platform.block_position_exists((1, 1)))
        self.assertTrue(platform.block_position_exists((4, 2)))
        self.assertListEqual([(1, 1), (4, 2)], platform.get_block_positions())
        self.assertListEqual([(-1, 0), (1, 0)], platform.get_block_directions())

    def test_two_blocks_move_two_iterations_successfully(self):
        platform = ParallelPlatformer(positions=[(3, 1), (3, 2)], directions=[(-1, 0), (1, 0)])
        for i in range(2):
            platform.move_blocks()
        self.assertEqual(2, len(platform.get_block_positions()))
        self.assertTrue(platform.block_position_exists((1, 1)))
        self.assertTrue(platform.block_position_exists((5, 2)))
        self.assertListEqual([(1, 1), (5, 2)], platform.get_block_positions())
        self.assertListEqual([(-1, 0), (1, 0)], platform.get_block_directions())

    def test_two_blocks_move_30_iterations_successfully(self):
        platform = ParallelPlatformer(positions=[(3, 1), (3, 2)], directions=[(-1, 0), (1, 0)])
        for i in range(30):
            platform.move_blocks()
            self.assertEqual(2, len(platform.get_block_positions()))
            self.assertEqual(len(platform.get_block_positions()), len(list(set(platform.get_block_positions()))))

    def test_10_blocks_move_30_iterations_successfully(self):
        platform = ParallelPlatformer(number_blocks=8)
        for i in range(30):
            platform.move_blocks()
            self.assertEqual(8, len(platform.get_block_positions()))
            self.assertEqual(len(platform.get_block_positions()), len(list(set(platform.get_block_positions()))))

    def test_10_blocks_of_bigger_size_move_30_iterations_successfully(self):
        platform = ParallelPlatformer(number_blocks=2, block_size=5, plane=Plane(z=[0, 12]))
        for i in range(30):
            platform.move_blocks()
            self.assertEqual(2, len(platform.get_block_positions()))
            self.assertEqual(len(platform.get_block_positions()), len(list(set(platform.get_block_positions()))))

    def test_a_single_block_of_parallel_platform_moves_correctly_after_hitting_the_wall(self):
        platform = ParallelPlatformer(positions=[(1, 1)], directions=[(-1, 0)])
        platform.move_blocks()
        self.assertEqual(1, len(platform.get_block_positions()))
        self.assertTrue(platform.block_position_exists((2, 1)))
        self.assertListEqual([(2, 1)], platform.get_block_positions())
        self.assertListEqual([(1, 0)], platform.get_block_directions())
