import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3

from jljc.printer_3d.scan_print_3d import ScanPrint3D


mc = minecraft.Minecraft.create()
scanner = ScanPrint3D(mc)

class Spaceship(object):
    window_block = block.AIR
    FRAME_LAYERS = [
        [
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,1,1,0,0,0,0],
            [0,0,0,1,0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0,1,0,0,0],
            [0,0,0,0,1,1,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0]
        ],
        [
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,1,1,1,1,1,0,0,0],
            [0,0,1,1,0,0,0,1,1,0,0],
            [0,0,1,0,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,0,1,0,0],
            [0,0,1,1,0,0,0,1,1,0,0],
            [0,0,0,1,1,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0]
        ],
        [
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,1,1,1,1,1,0,0,0],
            [0,0,1,0,0,0,0,0,1,0,0],
            [0,1,0,0,0,0,0,0,0,1,0],
            [0,1,0,0,0,0,0,0,0,1,0],
            [0,1,0,0,0,0,0,0,0,1,0],
            [0,1,0,0,0,0,0,0,0,1,0],
            [0,1,0,0,0,0,0,0,0,1,0],
            [0,0,1,0,0,0,0,0,1,0,0],
            [0,0,0,1,1,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0]
        ],
        [
            [0,0,0,0,1,1,1,0,0,0,0],
            [0,0,1,1,0,0,0,1,1,0,0],
            [0,1,0,0,0,0,0,0,0,1,0],
            [0,1,0,0,0,0,0,0,0,1,0],
            [1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,1],
            [0,1,0,0,0,0,0,0,0,1,0],
            [0,1,0,0,0,0,0,0,0,1,0],
            [0,0,1,1,0,0,0,1,1,0,0],
            [0,0,0,0,1,1,1,0,0,0,0]
        ],
        [
            [0,0,0,1,1,1,1,1,0,0,0],
            [0,0,1,0,0,0,0,0,1,0,0],
            [0,1,0,0,0,0,0,0,0,1,0],
            [1,0,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,2],
            [1,0,0,0,0,0,0,0,0,0,1],
            [0,1,0,0,0,0,0,0,0,1,0],
            [0,0,1,0,0,0,0,0,1,0,0],
            [0,0,0,1,1,1,1,1,0,0,0]
        ]
    ]
    x_shift = len(FRAME_LAYERS[0])



    def _build_body(self, pos, length=None, blocks=[block.IRON_BLOCK]):
        ## starting coordinates
        Xo = pos.x
        Yo= pos.y
        Zo = pos.z

        # build
        z = Zo
        bindex = 0
        for layer in self.FRAME_LAYERS:
            for i in range(0, len(layer)):
                y = Yo + i
                for j in range(0, len(layer[i])):
                    x = Xo + j
                    b = block.AIR
                    if layer[i][j] == 1:
                        b = blocks[bindex]
                    elif layer[i][j] == 2:
                        b = self.window_block
                    mc.setBlock(x, y, z, b.id, b.data)
            bindex += 1
            if bindex >= len(blocks):
                bindex = 0
            z += 1

        for n in range(0, length + 1):
            layer = self.FRAME_LAYERS[-1]
            for i in range(0, len(layer)):
                y = Yo + i
                for j in range(0, len(layer[i])):
                    x = Xo + j
                    b = block.AIR
                    if layer[i][j] == 1:
                        b = blocks[bindex]
                    elif layer[i][j] == 2:
                        b = self.window_block
                    mc.setBlock(x, y, z, b.id, b.data)
            bindex += 1
            if bindex >= len(blocks):
                bindex = 0
            z += 1

        for n in reversed(range(0, len(self.FRAME_LAYERS))):
            layer = self.FRAME_LAYERS[n]
            for i in range(0, len(layer)):
                y = Yo + i
                for j in range(0, len(layer[i])):
                    x = Xo + j
                    b = block.AIR
                    if layer[i][j] == 1:
                        b = blocks[bindex]
                    elif layer[i][j] == 2:
                        b = self.window_block
                    mc.setBlock(x, y, z, b.id, b.data)
            bindex += 1
            if bindex >= len(blocks):
                bindex = 0
            z += 1

        return Vec3(Xo, Yo, z)


    def _build_neck(self, pos, length=None, blocks=[block.IRON_BLOCK]):
        ## starting coordinates
        Xo = pos.x
        Yo= pos.y
        z = pos.z

        ## build spaceship neck
        bindex = 0
        for n in range(0, length + 1):
            layer = self.FRAME_LAYERS[0]
            for i in range(0, len(layer)):
                y = Yo + i
                for j in range(0, len(layer[i])):
                    x = Xo + j
                    b = blocks[bindex] if layer[i][j] == 1 else block.AIR
                    mc.setBlock(x, y, z, b.id, b.data)
            bindex += 1
            if bindex >= len(blocks):
                bindex = 0
            z += 1

        return Vec3(Xo, Yo, z)


    ##### EXLORER SHIP
    #
    #
    #
    def build_explorer_ship(self, pos, body_blocks=[block.IRON_BLOCK], neck_blocks=[block.IRON_BLOCK]):
        pos = self._build_body(pos, 2, body_blocks)
        pos = self._build_neck(pos, 7, neck_blocks)
        pos = self._build_body(pos, 2, body_blocks)
        return pos


    ##### COMMAND SHIP
    #
    #
    #
    def build_command_ship(self, pos, body_blocks=[block.IRON_BLOCK], neck_blocks=[block.IRON_BLOCK]):
        # main
        pos = self._build_body(pos, 7, body_blocks)
        pos = self._build_neck(pos, 4, neck_blocks)
        pos = self._build_body(pos, 20, body_blocks)
        pos = self._build_neck(pos, 7, neck_blocks)
        saved_pos = Vec3(pos.x, pos.y, pos.z)
        pos = self.build_explorer_ship(pos, body_blocks, neck_blocks)

        # sides
        self._build_command_ship_left_tail(saved_pos, body_blocks, neck_blocks)
        self._build_command_ship_right_tail(saved_pos, body_blocks, neck_blocks)

        return pos


    def _build_command_ship_tail(self, pos, body_blocks=[block.IRON_BLOCK], neck_blocks=[block.IRON_BLOCK], factor=0):
        pos = Vec3(pos.x + factor, pos.y, pos.z)

        pos = self._build_body(pos, 2, body_blocks)
        pos = self._build_neck(pos, 7, neck_blocks)
        saved_pos = Vec3(pos.x, pos.y, pos.z)
        pos = self.build_explorer_ship(pos, body_blocks, neck_blocks)

        # further sides
        p1 = Vec3(saved_pos.x + factor, saved_pos.y, saved_pos.z)
        self.build_explorer_ship(p1, body_blocks, neck_blocks)

        return pos


    def _build_command_ship_left_tail(self, pos, body_blocks=[block.IRON_BLOCK], neck_blocks=[block.IRON_BLOCK]):
        self._build_command_ship_tail(pos, body_blocks, neck_blocks, self.x_shift)


    def _build_command_ship_right_tail(self, pos, body_blocks=[block.IRON_BLOCK], neck_blocks=[block.IRON_BLOCK]):
        self._build_command_ship_tail(pos, body_blocks, neck_blocks, self.x_shift * -1)


    ##### MOTHER SHIP
    #
    #
    #
    def build_mother_ship(self, pos, body_blocks=[block.IRON_BLOCK], neck_blocks=[block.IRON_BLOCK]):
        # central
        pos = self._build_body(pos, 7, body_blocks)
        pos = self._build_neck(pos, 4, neck_blocks)
        saved_pos = Vec3(pos.x, pos.y, pos.z)
        pos = self._build_mother_ship_tail(pos, body_blocks, neck_blocks)

        # sides
        self._build_mother_ship_side_left_tail(saved_pos, body_blocks, neck_blocks)
        self._build_mother_ship_side_right_tail(saved_pos, body_blocks, neck_blocks)

        return pos


    def _build_mother_ship_tail(self, pos, body_blocks=[block.IRON_BLOCK], neck_blocks=[block.IRON_BLOCK]):
        pos = self._build_body(pos, 20, body_blocks)
        pos = self._build_neck(pos, 7, neck_blocks)
        pos = self.build_explorer_ship(pos, body_blocks, neck_blocks)
        return pos


    def _build_mother_ship_side_left_tail(self, pos, body_blocks=[block.IRON_BLOCK], neck_blocks=[block.IRON_BLOCK]):
        return self._build_mother_ship_side_tail(pos, body_blocks, neck_blocks, self.x_shift)


    def _build_mother_ship_side_right_tail(self, pos, body_blocks=[block.IRON_BLOCK], neck_blocks=[block.IRON_BLOCK]):
        return self._build_mother_ship_side_tail(pos, body_blocks, neck_blocks, self.x_shift * -1)


    def _build_mother_ship_side_tail(self, pos, body_blocks=[block.IRON_BLOCK], neck_blocks=[block.IRON_BLOCK], factor=None):
        # inner side
        pos = Vec3(pos.x + factor, pos.y, pos.z)
        pos = self._build_body(pos, 20, body_blocks)
        pos = self._build_neck(pos, 7, neck_blocks)
        saved_pos = Vec3(pos.x, pos.y, pos.z)
        pos = self._build_command_ship_tail(pos, body_blocks, neck_blocks)

        # further sides
        p1 = Vec3(saved_pos.x + factor, saved_pos.y, saved_pos.z)
        self._build_command_ship_tail(p1, body_blocks, neck_blocks)

        # further sides
        p2 = Vec3(saved_pos.x + factor * 2, saved_pos.y, saved_pos.z)
        pos = self._build_body(p2, 2, [block.AIR])
        pos = self._build_neck(pos, 7, [block.AIR])
        pos = self.build_explorer_ship(pos, body_blocks, neck_blocks)


