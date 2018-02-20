import copy
import random

from platform.plane import Plane


NUMBER_BLOCKS = 5

class PlatformerBase(object):
    def __init__(self, number_blocks=NUMBER_BLOCKS, block_size=1, plane=None, positions=None, directions=None):
        self._set_block_size(block_size)
        self._set_plane(plane)
        self._set_number_of_blocks(number_blocks, positions)
        self.set_block_positions(positions or self._initialize_block_positions())
        self.set_block_directions(directions or self._initialize_block_directions())

    def _set_number_of_blocks(self, number_blocks, positions):
        self._number_of_blocks = len(positions) if positions else number_blocks

    def _set_block_size(self, block_size):
        assert (block_size - 1) % 2 == 0, "Invalid block size"
        self._block_size = block_size

    def _set_plane(self, plane):
        self._plane = plane if plane else Plane()
        self._initialize_plane_edges()

    @staticmethod
    def random_block_direction():
        possibilities = [-1, 1]
        x = random.randint(*possibilities)
        z = random.choice(possibilities) if x == 0 else 0
        return (x,z)

    @classmethod
    def change_block_direction(cls, current=None):
        return cls.random_block_direction()

    def _initialize_block_positions(self, already=None):
        block_positions = already or []
        x_range = (self._west_edge, self._east_edge)
        z_range = (self._south_edge, self._north_edge)
        while len(block_positions) < self._number_of_blocks:
            pos = (random.randint(*x_range), random.randint(*z_range))
            if pos not in block_positions:
                block_positions.append(pos)
        return block_positions

    def _initialize_plane_edges(self):
        padding = 1 + (self._block_size - 1) / 2
        self._west_edge  = self._plane.west_edge + padding
        self._east_edge  = self._plane.east_edge - padding
        self._south_edge = self._plane.south_edge + padding
        self._north_edge = self._plane.north_edge - padding

    def _initialize_block_directions(self):
        block_directions = []
        for pos in range(self._number_of_blocks):
            block_directions.append(self.random_block_direction())
        return block_directions

    def block_position_exists(self, pos=None):
        return pos in self._block_positions

    def block_within_plane(self, pos=None):
        return self._west_edge <= pos[0] <= self._east_edge \
               and self._south_edge <= pos[1] <= self._north_edge

    def set_block_positions(self, block_positions):
        self._block_positions = block_positions

    def get_block_positions(self):
        return copy.deepcopy(self._block_positions)

    def set_block_directions(self, block_directions):
        self._block_directions = block_directions

    def get_block_directions(self):
        return copy.deepcopy(self._block_directions)

    @staticmethod
    def calculate_new_position(position=None, direction=None):
        return (position[0] + direction[0], position[1] + direction[1])

    def move_blocks(self):
        block_positions = self.get_block_positions()
        block_directions = self.get_block_directions()
        for i in range(len(block_positions)):
            has_moved = False
            counter = 0
            while not has_moved:
                counter += 1
                new_pos = self.calculate_new_position(block_positions[i], block_directions[i])
                if self.block_within_plane(new_pos) and new_pos not in block_positions:
                    block_positions[i] = new_pos
                    has_moved = True
                else:
                    block_directions[i] = self.change_block_direction(block_directions[i])
                if counter >= 10:
                    break
        self.set_block_positions(block_positions)
        self.set_block_directions(block_directions)


class Platformer(PlatformerBase):
    pass


class StaticPlatformer(PlatformerBase):
    def __init__(self, number_blocks=NUMBER_BLOCKS, block_size=1, plane=None, positions=None, directions=None):
        super(StaticPlatformer, self).__init__(number_blocks=number_blocks, block_size=block_size,
                                               plane=plane, positions=positions, directions=None)

    @staticmethod
    def calculate_new_position(position=None, direction=None):
        return position

    @staticmethod
    def random_block_direction():
        return None

    @classmethod
    def change_block_direction(cls, current=None):
        return current

    def _initialize_block_directions(self):
        return []

    def move_blocks(self):
        pass


class ParallelPlatformer(PlatformerBase):
    MAXIMUM_GAP = 2

    def __init__(self, number_blocks=None, block_size=1, plane=None, positions=None, directions=None):
        super(ParallelPlatformer, self).__init__(number_blocks=number_blocks, block_size=block_size,
                                               plane=plane, positions=positions, directions=directions)

    def _set_number_of_blocks(self, number_blocks, positions):
        number_blocks = len(positions) if positions else number_blocks
        if not number_blocks:
            number_blocks = int((self._north_edge - self._south_edge) / self._block_size)
        self._number_of_blocks = number_blocks

    def _initialize_plane_edges(self):
        padding = 1 + (self._block_size - 1) / 2
        self._west_edge  = self._plane.west_edge + padding
        self._east_edge  = self._plane.east_edge - padding
        self._south_edge = self._plane.south_edge + 1
        self._north_edge = self._plane.north_edge - 1

    def _initialize_block_positions(self):
        block_positions = []
        x_range = (self._west_edge, self._east_edge)
        z_range = (self._south_edge, self._north_edge)

        gap = ParallelPlatformer.calculate_gap(number_blocks=self._number_of_blocks,
                                               length=(z_range[1] - z_range[0]),
                                               block_size=self._block_size)

        # set initial blocks
        jump = self._block_size + gap
        for z in range(z_range[0] + gap, z_range[1], jump):
            pos = (random.randint(*x_range), z)
            if pos not in block_positions:
                block_positions.append(pos)

        # set the rest of blocks
        return super(ParallelPlatformer, self)._initialize_block_positions(block_positions)

    @classmethod
    def calculate_gap(cls, number_blocks=None, length=None, block_size=None):
        gap = (length - (number_blocks * block_size)) / float(number_blocks + 1)
        assert gap == int(gap), "Gap size must be a whole number"
        assert gap <= cls.MAXIMUM_GAP, "Gap too wide"
        return int(gap)

    @classmethod
    def change_block_direction(cls, current=None):
        return tuple(-1 * i for i in current)

    @staticmethod
    def random_block_direction():
        possibilities = [-1, 1]
        x = random.randint(*possibilities)
        z = 0
        return (x,z)
