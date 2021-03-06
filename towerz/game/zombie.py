import arcade
from game import constants
from game.sprite_with_health import SpriteWithHealth


class Zombie(SpriteWithHealth):

    def __init__(self, x, y):
        super().__init__(constants.ZOMBIE_IMAGE, constants.ZOMBIE_SCALING, 100 )
        self.center_x = x
        self.center_y = y
        self.alive = True

    def add_enemy(self, delta_time: float):
        """Adds a new enemy to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """
        pass
    def get_current_health(self):
        return self.cur_health



