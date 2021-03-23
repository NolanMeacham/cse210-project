import arcade
from game import constants

class WallMagic(arcade.Sprite):

    def __init__(self, point_list):
        super().__init__(constants.WALL_MAGIC_IMG, constants.WALL_MAGIC_SCALING)
        self.point_list = point_list
        self.start_point = self.point_list[0]
        self.end_point = self.point_list[-1]
        self.start_x = self.start_point[0]
        self.start_y = self.start_point[1]
        self.dest_x = self.end_point[0]
        self.dest_y = self.end_point[1]
        self.diff_x = self.dest_x - self.start_x
        self.diff_y = self.dest_y - self.start_y