import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3

from jljc.printer_3d.scan_print_3d import ScanPrint3D


mc = minecraft.Minecraft.create()
scanner = ScanPrint3D(mc)

class House(object):
    window_block = block.AIR
    FRAME_LAYERS = {
        'cellar': {
            'blocks': {'1': block.WOOD_PLANKS, '0': block.AIR},
            'data': [
                       """
                       11111111111111111111111111
                       11111111111111111111111111
                       11111111111111111111111111
                       11111111111111111111111111
                       11111111111111111111111111
                       11111111111111111111111111
                       11111111111111111111111111
                       11111111111111111111111111
                       11111111111111111111111111
                       11111111111111111111111111
                       11111111111111111111111111
                       """,
                       """
                       11111111111111111111111111
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       11111111111111111111111111
                       """,
                       """
                       11111111111111111111111111
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       11111111111111111111111111
                       """,
                       """
                       11111111111111111111111111
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       10000000000000000000000001
                       11111111111111111111111111
                       """,
                    ]
        },
        'ground': {
            'blocks': {'1': block.WOOD_PLANKS,
                       '0': block.AIR,
                       '2': block.GLASS},
            'data': [
                """
                 11111111111111111111111111
                 11111111111111111111110001
                 11111111111111111111110001
                 11111111111111111111110001
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                """,
                """
                 12222222222222222222222221
                 20000000000000000000000002
                 20000000000000000000000002
                 20000000000000000100000002
                 20000000000000000100000002
                 20000000000000000100000002
                 21111100000011111100000002
                 20000000000010000000000000
                 20000000000010000000000000
                 20000000000010000000000002
                 12222222222222222222222221
                """,
                """
                 12222222222222222222222221
                 20000000000000000000000002
                 20000000000000000000000002
                 20000000000000000100000002
                 20000000000000000100000002
                 20000000000000000100000002
                 21111100000011111100000002
                 20000000000010000000000000
                 20000000000010000000000000
                 20000000000010000000000002
                 12222222222222222222222221
                """,
                """
                 12222222222222222222222221
                 20000000000000000000000002
                 20000000000000000000000002
                 20000000000000000100000002
                 20000000000000000100000002
                 20000000000000000100000002
                 21111100000011111100000002
                 20000000000010000000000002
                 20000000000010000000000002
                 20000000000010000000000002
                 12222222222222222222222221
                """
            ]
        },
        'first': {
            'blocks': {'1': block.WOOD_PLANKS,
                       '0': block.AIR,
                       '2': block.GLASS},
            'data': [
                """
                 11111111111111111111111111
                 11111111111111111111110001
                 11111111111111111111110001
                 11111111111111111111110001
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                """,
                """
                  12222222222222222222222221
                  20000000000100000000000002
                  20000000000000000000000002
                  20000000000000000000000002
                  20000000000100000000000002
                  21111111111110011111001112
                  20000000000000001000000000
                  20000000000000000000000000
                  20000000000000000000000000
                  20000000000000001000000000
                  12222222222222222000000000
                 """,
                """
                  12222222222222222222222221
                  20000000000100000000000002
                  20000000000000000000000002
                  20000000000000000000000002
                  20000000000100000000000002
                  21111111111110011111001112
                  20000000000000001000000000
                  20000000000000000000000000
                  20000000000000000000000000
                  20000000000000001000000000
                  12222222222222222000000000
                 """,
                """
                  12222222222222222222222221
                  20000000000100000000000002
                  20000000000000000000000002
                  20000000000000000000000002
                  20000000000100000000000002
                  21111111111110011111001112
                  20000000000000001000000000
                  20000000000000000000000000
                  20000000000000000000000000
                  20000000000000001000000000
                  12222222222222222000000000
                 """,
            ]
        },
        'roof': {
            'blocks': {'1': block.WOOD_PLANKS},
            'data': [
                """
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                 11111111111111111111111111
                """
            ]
        }
    }
 

    @staticmethod
    def _panel_to_matrix(panel):
        return filter(lambda y: len(y) > 0, map(lambda x: list(x.replace(" ", "")), panel.split('\n')))


    def _print_panel(self, panel=None, pos=None, blocks=None):
        ## starting coordinates
        Xo = pos.x
        Zo = pos.z
        Yo = pos.y

        panel = self._panel_to_matrix(panel)

        # build
        y = Yo
        for i in range(0, len(panel)):
            z = Zo + i
            for j in range(0, len(panel[i])):
                x = Xo + j
                b = blocks[panel[i][j]]
                mc.setBlock(x, y, z, b.id, b.data)

        return Vec3(Xo, Yo + 1, Zo)



    def build_house(self, pos):
        for level in ['cellar', 'ground', 'first', 'roof']:
            for panel in self.FRAME_LAYERS[level]['data']:
                pos = self._print_panel(panel, pos, self.FRAME_LAYERS[level]['blocks'])
        return pos

