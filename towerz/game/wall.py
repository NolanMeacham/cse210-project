from game.point import Point
from game import constants
from game.sprite_with_health import SpriteWithHealth
import arcade

class Wall(SpriteWithHealth):
    def __init__(self, x, y):
        super().__init__(constants.WALL_IMAGE, constants.WALL_SCALING, 10)

        self.center_x = x
        self.center_y = y
        

        self.alive = True
    
    def get_hit(self):
        if self.cur_health > 0:
            self.cur_health = self.cur_health - 0.1

    

