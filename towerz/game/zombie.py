import arcade
import random
import math
from game import constants
from game.sprite_with_health import SpriteWithHealth
from game.tower_sprite import TowerSprite


class Zombie(SpriteWithHealth):

    def __init__(self, x, y, cast):
        super().__init__(constants.ZOMBIE_IMAGE, constants.ZOMBIE_SCALING, 100 )
        self.center_x = x
        self.center_y = y
        self.alive = True
        self.cast = cast


    def attack_tower(self):
            start_x = self.center_x
            start_y = self.center_y

            # Get the destination location for the bullet
            dest_x = self.cast['tower'][0].center_x
            dest_y = self.cast['tower'][0].center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the bullet travels.
            self.change_x = math.cos(angle) * constants.ZOMBIE_SPEED
            self.change_y = math.sin(angle) * constants.ZOMBIE_SPEED

