from game.sprite_with_health import SpriteWithHealth
from game import constants
import arcade

class Resource(SpriteWithHealth):
    def __init__(self, x, y):
        super().__init__(constants.RESOURCE_IMAGE, constants.ZOMBIE_SCALING, 100 )
        self.center_x = x
        self.center_y = y
        self.alive = True
        self.health_color = arcade.color.PURPLE

    
    
