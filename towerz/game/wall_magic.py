import arcade
from game import constants
import math
import random

class WallMagic(arcade.Sprite):

    def __init__(self, point_list):
        super().__init__(constants.WALL_MAGIC_IMG, constants.WALL_MAGIC_SCALING)
        self.point_list = point_list
        rand_1 = random.randint(0,3)
        rand_2 = random.randint(0,3)
        if rand_1 == rand_2:
            if rand_2 == 3:
                rand_2 -= 1
            elif rand_2 == 0:
                rand_2 += 1
            else:
                rand_2 += 1
        self.start_point = self.point_list[rand_1]
        self.end_point = self.point_list[rand_2]
        self.center_x = self.start_point[0]
        self.center_y = self.start_point[1]
        self.dest_x = self.end_point[0]
        self.dest_y = self.end_point[1]
        self.diff_x = self.dest_x - self.center_x
        self.diff_y = self.dest_y - self.center_y
        self.angle = math.atan2(self.diff_y, self.diff_x)
        self.change_x = math.cos(self.angle) * constants.MAGIC_SPEED
        self.change_y = math.sin(self.angle) * constants.MAGIC_SPEED