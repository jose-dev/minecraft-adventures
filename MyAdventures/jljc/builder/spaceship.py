import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3

from jljc.printer_3d.scan_print_3d import ScanPrint3D


mc = minecraft.Minecraft.create()
scanner = ScanPrint3D(mc)

class Spaceship(object):
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
            [1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,1],
            [0,1,0,0,0,0,0,0,0,1,0],
            [0,0,1,0,0,0,0,0,1,0,0],
            [0,0,0,1,1,1,1,1,0,0,0]
        ]
    ]


    def _build_body(self, pos, length=None, blocks=None):
        ## starting coordiantes
        Xo = pos.x
        Yo= pos.y
        Zo = pos.z

        ## build spaceship body
        z = Zo
        for layer in self.FRAME_LAYERS:
            for i in range(0, len(layer)):
                y = Yo + i
                for j in range(0, len(layer[i])):
                    x = Xo + j
                    b = block.IRON_BLOCK if layer[i][j] == 1 else block.AIR
                    mc.setBlock(x, y, z, b.id, b.data)
            z += 1

        for n in range(0, length + 1):
            layer = self.FRAME_LAYERS[-1]
            for i in range(0, len(layer)):
                y = Yo + i
                for j in range(0, len(layer[i])):
                    x = Xo + j
                    b = block.IRON_BLOCK if layer[i][j] == 1 else block.AIR
                    mc.setBlock(x, y, z, b.id, b.data)
            z += 1

        for n in reversed(range(0, len(self.FRAME_LAYERS))):
            layer = self.FRAME_LAYERS[n]
            for i in range(0, len(layer)):
                y = Yo + i
                for j in range(0, len(layer[i])):
                    x = Xo + j
                    b = block.IRON_BLOCK if layer[i][j] == 1 else block.AIR
                    mc.setBlock(x, y, z, b.id, b.data)
            z += 1

        return Vec3(Xo, Yo, z)


    def _build_neck(self, pos, length=None, blocks=None):
        ## starting coordiantes
        Xo = pos.x
        Yo= pos.y
        z = pos.z

        ## build spaceship neck
        for n in range(0, length + 1):
            layer = self.FRAME_LAYERS[0]
            for i in range(0, len(layer)):
                y = Yo + i
                for j in range(0, len(layer[i])):
                    x = Xo + j
                    b = block.IRON_BLOCK if layer[i][j] == 1 else block.AIR
                    mc.setBlock(x, y, z, b.id, b.data)
            z += 1

        return Vec3(Xo, Yo, z)


    def build_explorer_ship(self, pos, blocks=None):
        pos = self._build_body(pos, 2, blocks)
        pos = self._build_neck(pos, 7, blocks)
        pos = self._build_body(pos, 2, blocks)
        return pos



    def build_mother_ship(self, pos, blocks=None):
        pos = self._build_body(pos, 7, blocks)
        pos = self._build_neck(pos, 4, blocks)
        pos = self._build_body(pos, 20, blocks)
        pos = self._build_neck(pos, 7, blocks)
        pos = self._build_body(pos, 2, blocks)
        pos = self._build_neck(pos, 7, blocks)
        pos = self.build_explorer_ship(pos, blocks)
        return pos

