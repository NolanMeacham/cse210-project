import arcade
from game import constants
from game.sprite_with_health import SpriteWithHealth


class Zombie(SpriteWithHealth):

    def __init__(self, x, y):
        super().__init__(constants.ZOMBIE_IMAGE, constants.ZOMBIE_SCALING, 100 )
        self.center_x = x
        self.center_y = y
