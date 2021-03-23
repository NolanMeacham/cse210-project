
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
        self.spawn_difficulty = constants.DIFFICULTY
        self.speed_difficulty = constants.DIFFICULTY
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
            self.spawn_difficulty = constants.DIFFICULTY
            self.speed_difficulty = constants.DIFFICULTY
        else:
            self.spawn_difficulty += constants.SPAWN_DIFFICULTY_MODIFIER
            self.speed_difficulty += constants.SPEED_DIFFICULTY_MODIFIER




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

        #After 5 seconds, start spawning regular zombies every 3 seconds
        if time.time() - self.timer >= 30 :
            if ran == 1:
                big_zombie = BigZombie(random_x,random_y, self.cast)
                big_zombie.speed *= self.speed_difficulty
                self.cast['zombies'].append(big_zombie)
            elif ran == 2 or ran == 3 or ran == 4:
                zombie = Zombie(random_x, random_y, self.cast)
                zombie.speed *= self.speed_difficulty
                self.cast['zombies'].append(zombie)

        else:
            zombie = Zombie(random_x, random_y, self.cast)
            zombie.speed *= self.speed_difficulty
            self.cast['zombies'].append(zombie)

    def begin_spawn(self):
        """
        """
        arcade.schedule(self.create_zombie, 3.0 / self.spawn_difficulty)

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

    

        