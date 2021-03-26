from game.zombie import Zombie
from game import constants
import arcade

class BigZombie(Zombie):
    """
    BigZombie is a Zombie,
    it inherits all attributes and methods from parent class.

    Stereotype:
        ?
    """
    def __init__(self, x, y, cast):
        """
        Class constructor.
        
        Args:
            self (BigZombie): an instance of BigZombie
            x (int): value that represents the x position
            y (int): value that represents the y position
            cast (dict): dictionary that holds all actors in the game
        """
        super().__init__(x, y, cast)
        self.max_health = 200
        self.cur_health = 200
        self.scale = 2
        self.center_x = x
        self.center_y = y
        self.cast = cast
        self.score_points = constants.BIG_ZOMBIE_POINTS

