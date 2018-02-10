import random
import copy


NUMBER_BLOCKS = 5


class Plane(object):
    def __init__(self, x=[0, 10], z=[0, 10]):
        self._x = x
        self._z = z

    def x_boundaries(self):
        return self._x

    def z_boundaries(self):
        return self._z

    def west_edge(self):
        return self._x[0]

    def east_edge(self):
        return self._x[1]

    def south_edge(self):
        return self._z[0]

    def north_edge(self):
        return self._z[1]


class Platform(object):
    _plane = Plane()
    _block_positions = []
    _block_directions = []

    def __init__(self, number_blocks=NUMBER_BLOCKS, plane=None, positions=None, directions=None):
        self._number_of_blocks = len(positions) if positions else number_blocks
        self._plane = plane if plane else Plane()
        self.set_block_positions(positions or self._initialize_block_positions())
        self.set_block_directions(directions or self._initialize_block_directions())

    def _initialize_block_positions(self):
        block_positions = []
        x_range = (self._plane.west_edge() + 1, self._plane.east_edge() - 1)
        z_range = (self._plane.south_edge() + 1, self._plane.north_edge() - 1)
        while len(block_positions) < self._number_of_blocks:
            pos = (random.randint(*x_range), random.randint(*z_range))
            if pos not in block_positions:
                block_positions.append(pos)
        return block_positions

    @staticmethod
    def random_block_direction():
        possibilities = [-1, 1]
        x = random.randint(*possibilities)
        z = random.choice(possibilities) if x == 0 else 0
        return (x,z)

    def _initialize_block_directions(self):
        block_directions = []
        for pos in range(self._number_of_blocks):
            block_directions.append(self.random_block_direction())
        return block_directions

    def block_position_exists(self, pos=None):
        return pos in self._block_positions

    def block_within_plane(self, pos=None):
        return self._plane.west_edge() < pos[0] < self._plane.east_edge() \
               and self._plane.south_edge() < pos[1] < self._plane.north_edge()

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
                    block_directions[i] = self.random_block_direction()
                if counter >= 10:
                    break
        self.set_block_positions(block_positions)
        self.set_block_directions(block_directions)


