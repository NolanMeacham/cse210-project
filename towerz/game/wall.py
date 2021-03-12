from arcade.color import BLIZZARD_BLUE
from game.point import Point
from game import constants
from game.sprite_with_health import SpriteWithHealth
import arcade
import time

class Wall(SpriteWithHealth):
    def __init__(self, x, y, cast):
        super().__init__(constants.WALL_IMAGE, constants.WALL_SCALING, 10)

        self.center_x = x
        self.center_y = y
        self.cast = cast
        self.timer = time.time()
        self._lifetime = constants.WALL_LIFETIME
        self.alive = True
        self._point_list = []
    
    """
    Detects a hit from a zombie
    """
    def get_hit(self):
        if self.cur_health > 0:
            self.cur_health = self.cur_health - constants.ZOMBIE_HIT

    """
    Gives a timed death to the wall object
    """
    def timed_death(self):
        if time.time() - self.timer >= self._lifetime:        
            self.remove_from_sprite_lists()

    """
    TODO: CASTS THE MAGIC THAT INTERACTS BETWEEN ALL OF THE WALLS.

    """
    def cast_magic(self):
        cast = self.cast
        zombies = cast["zombies"]
        walls = cast['walls']
        
        point_list = []
        for wall in walls:
            point = wall._get_position()
            point_list.append(point)
        point_list.append(point_list[0])
        self._point_list = point_list

    def draw_magic(self):
        if len(self._point_list) > 2:
            arcade.draw_line_strip(self._point_list, arcade.color.RED, 3)
        self._point_list = []

        