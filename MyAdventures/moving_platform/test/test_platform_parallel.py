import unittest
import random

from platform.moving_platform import PlatformParallel, Plane


class TestPlatformParallel(unittest.TestCase):
    def setUp(self):
        random.seed(13)

    def test_default_platform(self):
        result = PlatformParallel()
        self.assertEqual(len(result.get_block_positions()), len(list(set(result.get_block_positions()))))
        self.assertEqual(len(result.get_block_positions()), len(result.get_block_directions()))

    def test_basic_custom_platform(self):
        result = PlatformParallel(number_blocks=10)
        self.assertEqual(10, len(result.get_block_positions()))
        self.assertEqual(len(result.get_block_positions()), len(list(set(result.get_block_positions()))))
        self.assertEqual(len(result.get_block_positions()), len(result.get_block_directions()))

    def test_platform_successfully_created_with_different_number_of_blocks_and_sizes(self):
        r = PlatformParallel(number_blocks=4)
        print(r.__dict__)
        r = PlatformParallel(number_blocks=3, block_size=3)
        print(r.__dict__)
        r = PlatformParallel(number_blocks=1, block_size=5, plane=Plane([0, 7], [0, 7]))
        print(r.__dict__)

    def test_platform_requires_more_blocks_raises_error(self):
        try:
            r = PlatformParallel(number_blocks=2)
            self.assertTrue(False)
        except AssertionError as e:
            self.assertTrue(True)
            self.assertEqual(e.message, 'Not enough blocks')

    def test_platform_leaves_gap_at_the_end_raises_error(self):
        try:
            r = PlatformParallel(number_blocks=1, block_size=5)
            print(r.__dict__)
            self.assertTrue(False)
        except AssertionError as e:
            self.assertTrue(True)
            self.assertEqual(e.message, 'Gap too big at the end')

    def test_platform_requires_odd_block_sizes_raises_error(self):
        try:
            PlatformParallel(block_size=2)
            self.assertTrue(False)
        except AssertionError as e:
            self.assertTrue(True)
            self.assertEqual(e.message, 'Invalid block size')

    def test_platform_with_custom_positions(self):
        result = PlatformParallel(number_blocks=10, positions=[(2, 3), (3, 4)])
        self.assertEqual(2, len(result.get_block_positions()))
        self.assertTrue(result.block_position_exists((2, 3)))
        self.assertListEqual([(2, 3), (3, 4)], result.get_block_positions())
        self.assertEqual(len(result.get_block_positions()), len(result.get_block_directions()))

    def test_platform_with_custom_positions_and_directions(self):
        result = PlatformParallel(number_blocks=10, positions=[(2, 3), (3, 4)], directions=[(-1, 0), (1, 0)])
        self.assertEqual(2, len(result.get_block_positions()))
        self.assertTrue(result.block_position_exists((2, 3)))
        self.assertListEqual([(2, 3), (3, 4)], result.get_block_positions())
        self.assertListEqual([(-1, 0), (1, 0)], result.get_block_directions())

    def test_block_will_hit_the_walls_in_the_next_move(self):
        platform = PlatformParallel(positions=[(1, 1)], directions=[(-1, 0)])
        result = platform.calculate_new_position((1, 1), (-1, 0))
        self.assertEqual((0, 1), result)
        self.assertFalse(platform.block_within_plane(result))

    def test_block_will_not_hit_the_walls_in_the_next_move(self):
        platform = PlatformParallel(positions=[(2, 1)], directions=[(-1, 0)])
        result = platform.calculate_new_position((2, 1), (-1, 0))
        self.assertEqual((1, 1), result)
        self.assertTrue(platform.block_within_plane(result))

    def test_block_of_bigger_size_will_hit_the_walls_in_the_next_move(self):
        platform = PlatformParallel(positions=[(2, 1)], directions=[(-1, 0)], block_size=3)
        result = platform.calculate_new_position((2, 1), (-1, 0))
        self.assertEqual((1, 1), result)
        self.assertFalse(platform.block_within_plane(result))

    def test_a_single_block_moves_one_iteration_successfully(self):
        platform = PlatformParallel(positions=[(2, 1)], directions=[(-1, 0)])
        platform.move_blocks()
        self.assertEqual(1, len(platform.get_block_positions()))
        self.assertTrue(platform.block_position_exists((1, 1)))
        self.assertListEqual([(1, 1)], platform.get_block_positions())
        self.assertListEqual([(-1, 0)], platform.get_block_directions())

    def test_a_single_block_moves_two_iterations_successfully(self):
        platform = PlatformParallel(positions=[(3, 1)], directions=[(-1, 0)])
        for i in range(2):
            platform.move_blocks()
        self.assertEqual(1, len(platform.get_block_positions()))
        self.assertTrue(platform.block_position_exists((1, 1)))
        self.assertListEqual([(1, 1)], platform.get_block_positions())
        self.assertListEqual([(-1, 0)], platform.get_block_directions())

    def test_two_blocks_move_one_iteration_successfully(self):
        platform = PlatformParallel(positions=[(2, 1), (3, 2)], directions=[(-1, 0), (1, 0)])
        platform.move_blocks()
        self.assertEqual(2, len(platform.get_block_positions()))
        self.assertTrue(platform.block_position_exists((1, 1)))
        self.assertTrue(platform.block_position_exists((4, 2)))
        self.assertListEqual([(1, 1), (4, 2)], platform.get_block_positions())
        self.assertListEqual([(-1, 0), (1, 0)], platform.get_block_directions())

    def test_two_blocks_move_two_iterations_successfully(self):
        platform = PlatformParallel(positions=[(3, 1), (3, 2)], directions=[(-1, 0), (1, 0)])
        for i in range(2):
            platform.move_blocks()
        self.assertEqual(2, len(platform.get_block_positions()))
        self.assertTrue(platform.block_position_exists((1, 1)))
        self.assertTrue(platform.block_position_exists((5, 2)))
        self.assertListEqual([(1, 1), (5, 2)], platform.get_block_positions())
        self.assertListEqual([(-1, 0), (1, 0)], platform.get_block_directions())

    def test_two_blocks_move_30_iterations_successfully(self):
        platform = PlatformParallel(positions=[(3, 1), (3, 2)], directions=[(-1, 0), (1, 0)])
        for i in range(30):
            platform.move_blocks()
            self.assertEqual(2, len(platform.get_block_positions()))
            self.assertEqual(len(platform.get_block_positions()), len(list(set(platform.get_block_positions()))))

    def test_10_blocks_move_30_iterations_successfully(self):
        platform = PlatformParallel(number_blocks=10)
        for i in range(30):
            platform.move_blocks()
            self.assertEqual(10, len(platform.get_block_positions()))
            self.assertEqual(len(platform.get_block_positions()), len(list(set(platform.get_block_positions()))))

    def test_10_blocks_of_bigger_size_move_30_iterations_successfully(self):
        platform = PlatformParallel(number_blocks=10, block_size=3)
        for i in range(30):
            platform.move_blocks()
            self.assertEqual(10, len(platform.get_block_positions()))
            self.assertEqual(len(platform.get_block_positions()), len(list(set(platform.get_block_positions()))))

    def test_a_single_block_of_parallel_platform_moves_correctly_after_hitting_the_wall(self):
        platform = PlatformParallel(positions=[(1, 1)], directions=[(-1, 0)])
        platform.move_blocks()
        self.assertEqual(1, len(platform.get_block_positions()))
        self.assertTrue(platform.block_position_exists((2, 1)))
        self.assertListEqual([(2, 1)], platform.get_block_positions())
        self.assertListEqual([(1, 0)], platform.get_block_directions())
