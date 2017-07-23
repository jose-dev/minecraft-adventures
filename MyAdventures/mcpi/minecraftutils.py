import mcpi.minecraft as minecraft
import mcpi.block as block
import csv


class MinecraftUtils(minecraft.Minecraft):
    def __init__(self, mc):
        self.mc = mc


    def get_player_position(self):
        return self.player.getTilePos()


    def log_to_console(self, msg):
        self.mc.postToChat(msg)


    def clear_area(self, point_a, length=30, width=30, height=30):
        point_b = minecraft.Vec3(point_a.x + length, point_a.y + height, point_a.z + width)
        self.mc.setBlocks(point_a.x, point_a.y, point_a.z,
                          point_b.x, point_b.y, point_b.z,
                          block.AIR.id)


    def clear_area_in_front_of(self, pos=None, length=30, width=30, height=30):
        offset = 2
        point_a = minecraft.Vec3(pos.x + offset, pos.y, pos.z)
        self.clear_area(point_a, length, width, height)


    def clear_area_centered_at(self, pos=None, length=30, width=30, height=30):
        point_a = minecraft.Vec3(pos.x - int(length / 2), pos.y, pos.z - int(width / 2))
        self.clear_area(point_a, length, width, height)


    @staticmethod
    def read_csv_drawing(filein):
        drawing = []
        with open(filein) as csvfile:
            r = csv.reader(csvfile, delimiter=',')
            for row in r:
                drawing.append(row)
        return drawing


    def make_carpet(self, pos=None, coord=None, offset_x=2):
        point = minecraft.Vec3(pos.x + offset_x, pos.y, pos.z)

        self.log_to_console("clearing in front of")
        self.clear_area_in_front_of(point, length=len(coord), width=len(coord[0]), height=1)

        self.log_to_console("doing carpet...")
        for z in range(len(coord)):
            for x in range(len(coord[0])):
                self.mc.setBlock(point.x + x,
                                 point.y,
                                 point.z + z,
                                 block.WOOL.id,
                                 int(coord[z][x]))


    def make_picture(self, pos= None, coord=None, offset_x=2, offset_y=2):
        point = minecraft.Vec3(pos.x + offset_x, pos.y + offset_y, pos.z)

        self.log_to_console("clearing in front of")
        self.clear_area_in_front_of(point, length=len(coord), width=1, height=len(coord[0]))

        self.log_to_console("doing picture...")
        y = 0
        for z in range(len(coord) - 1, -1, -1):
            for x in range(len(coord[0])):
                self.mc.setBlock(point.x + x,
                                 point.y + y,
                                 point.z,
                                 block.WOOL.id,
                                 int(coord[z][x]))
            y += 1


    def make_sculpture(self, pos= None, coord=None, offset_x=2, offset_y=2):
        point = minecraft.Vec3(pos.x + offset_x, pos.y + offset_y, pos.z)

        self.log_to_console("clearing in front of")
        self.clear_area_in_front_of(point, length=len(coord), width=1, height=len(coord[0]))

        self.log_to_console("doing sculpture...")
        y = 0
        for z in range(len(coord) - 1, -1, -1):
            for x in range(len(coord[0])):
                block_id = block.BEDROCK.id if int(coord[z][x]) > 0 else block.AIR.id
                self.mc.setBlock(point.x + x,
                                 point.y + y,
                                 point.z,
                                 block_id)
            y += 1

