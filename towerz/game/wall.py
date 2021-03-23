from game.wall_magic import WallMagic
from game import constants
from game.sprite_with_health import SpriteWithHealth
import numpy as np
import arcade
import time

class Wall(SpriteWithHealth):
    """
    """
    def __init__(self, x, y, cast):
        """
        Class constructor.
        Calls the constructor for parent class.

        Args:
            self (Wall): an instance of Wall
            x (int): value representing x position
            y (int): value representing y position
            cast (dict): dictionary that holds all the actors
            
        """
        super().__init__(constants.WALL_IMAGE, constants.WALL_SCALING, 10)
        
        
        self.center_x = x
        self.center_y = y
        self.cast = cast
        self.timer = time.time()
        self._lifetime = constants.WALL_LIFETIME
        self.alive = True
        self._point_list = []

    def draw(self):
        super().draw()

    def draw_health_bar(self):
        pass
   
    def get_hit(self):
        """
        Detects a hit from a zombie
        """
        if self.cur_health > 0:
            self.cur_health = self.cur_health - constants.ZOMBIE_HIT
        elif self.cur_health <= 0:
            self._point_list = []

    
    def timed_death(self):
        """
        Gives a timed death to the wall object
        """
        # if time.time() - self.timer >= self._lifetime:        
        #     self.remove_from_sprite_lists()
        pass

    
    def cast_magic(self):
        """
        TODO: CASTS THE MAGIC THAT INTERACTS BETWEEN ALL OF THE WALLS.

        """
        cast = self.cast
        zombies = cast["zombies"]
        walls = cast['walls']
        
        point_list = []
        for wall in walls:
            point = wall._get_position()
            point_list.append(point)
        point_list.append(point_list[0])
        self._point_list = point_list
        self.add_magic_to_cast()


    def add_magic_to_cast(self):
        """
        Draws the red line between walls.

        """
        cast = self.cast
        zombies = cast["zombies"]
        walls = cast['walls']
        if len(self._point_list) >= 2:
            point_list = self._point_list
            for i in self._point_list:                
                lightning = WallMagic(point_list)
                self.cast["magic"].append(lightning)
                np.roll(point_list,1)
                point_list.tolist()
        # self._point_list = []

        