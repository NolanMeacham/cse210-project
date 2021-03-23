import arcade
from game import constants
import math

class WallMagic(arcade.Sprite):

    def __init__(self, point_list):
        super().__init__(constants.WALL_MAGIC_IMG, constants.WALL_MAGIC_SCALING)
        self.point_list = point_list
        self.start_point = self.point_list[0]
        self.end_point = self.point_list[2]
        self.center_x = self.start_point[0]
        self.center_y = self.start_point[1]
        self.dest_x = self.end_point[0]
        self.dest_y = self.end_point[1]
        self.diff_x = self.dest_x - self.center_x
        self.diff_y = self.dest_y - self.center_y
        self.angle = math.atan2(self.diff_y, self.diff_x)
        self.change_x = math.cos(self.angle)
        self.change_y = math.sin(self.angle)