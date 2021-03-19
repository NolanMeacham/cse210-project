
from game import constants
import random
import arcade
import time
from game.action import Action
from game.zombie import Zombie
from game.resource import Resource
from game.bigzombie import BigZombie

class Add_enemy(Action):
    """
    A code template for adding enemies to the game
    """
    def __init__(self):
        """
        Class constructor.
        """
        self.begin_spawn()
        self.timer = time.time()


    def execute(self, cast):
        """
        Implements the abstract execute method from Action class.
        """
        self.cast = cast
        resources = cast['resources'] 
        tower = cast['tower'][0]
        if len(resources) < 5:
            self.make_resource()
        
        if tower.cur_health <= 0:
            arcade.unschedule(self.create_zombie)


    def create_zombie(self, delta_time: float):
        """Adds a new enemy to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """
        #This needs optimization
        ran = random.randint(1, 5)
        random_x = 0
        random_y = 0
        if ran == 1:
            random_x = constants.MAX_X + 20
            random_y = random.randint(0 , constants.MAX_Y)
        elif ran == 2:
            random_x = -20
            random_y = random.randint(0 , constants.MAX_Y)
        elif ran == 3:
            random_x = random.randint(0 , constants.MAX_X)
            random_y = -20
        elif ran == 4:
            random_x =  random.randint(0 , constants.MAX_X)
            random_y = constants.MAX_Y - 20

        zombie = Zombie(random_x, random_y, self.cast)

        if time.time() - self.timer >= 25:
            new_zombie = BigZombie(random_x,random_y, self.cast)
            self.cast['zombies'].append(new_zombie)
        
        self.cast['zombies'].append(zombie)


    def begin_spawn(self):
        """
        """
        arcade.schedule(self.create_zombie, 4.0)

    def make_resource(self):
        """
        """
        # ran = random.randint(1, 5)
        random_x = random.randint(20, constants.MAX_X - 20)
        random_y = random.randint(20, constants.MAX_Y - 20)
        # if ran == 1:
        #     random_x = constants.MAX_X - 20
        #     random_y = random.randint(0 , constants.MAX_Y - 20)
        # elif ran == 2:
        #     random_x = 20
        #     random_y = random.randint(0 , constants.MAX_Y - 20)
        # elif ran == 3:
        #     random_x = random.randint(0 , constants.MAX_X - 20)
        #     random_y = 20
        # elif ran == 4:
        #     random_x =  random.randint(0 , constants.MAX_X - 20)
        #     random_y = constants.MAX_Y + 20

        resource = Resource(random_x, random_y)

        self.cast['resources'].append(resource)

    

        