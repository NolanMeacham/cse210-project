
from game import constants
import random
import arcade
from game.action import Action
from game.zombie import Zombie

class Add_enemy(Action):
    """
    A code template for adding enemies to the game
    """
    def __init__(self):
        self.begin_spawn()
    def execute(self, cast):
        self.cast = cast




    
    
    
    def create_zombie(self, delta_time: float):
        """Adds a new enemy to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """
        #This needs optimization
        ran = random.randint(1, 4)
        if ran == 1:
            random_x = constants.MAX_X + 20
            random_y = random.randint(0 , constants.MAX_Y)
        if ran == 2:
            random_x = -20
            random_y = random.randint(0 , constants.MAX_Y)
        if ran == 3:
            random_x = random.randint(0 , constants.MAX_X)
            random_y = -20
        if ran == 4:
            random_x =  random.randint(0 , constants.MAX_X)
            random_y = constants.MAX_Y - 20
        random_y =  random.randint(constants.MAX_Y,(constants.MAX_Y+20))
        zombie = Zombie(random_x, random_y, self.cast)

        self.cast['zombies'].append(zombie)

    def begin_spawn(self):
        arcade.schedule(self.create_zombie, 2.0)

    

        