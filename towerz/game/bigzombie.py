from game.zombie import Zombie
from game import constants
import arcade

class BigZombie(Zombie):
    def __init__(self, x, y, cast):
        super().__init__(x, y, cast)
        self.scale = 0.5
        self.center_x = x
        self.center_y = y
        self.cast = cast
        self.score_points = 50
        self.max_health = 200
        