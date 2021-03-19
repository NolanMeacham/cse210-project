from game.sprite_with_health import SpriteWithHealth
from game import constants
import arcade

class Resource(SpriteWithHealth):
    """
    Resource is a SpriteWithHealth
    Resource for user to gather and use. Gets smaller as it is gathered.

    Stereotype:
        Information Holder

    """
    def __init__(self, x, y):
        """
        Class constructor, calls the parent class constructor first.

        Args:
            self (Resource): an instance of Resource
            x (int): value representing the x position
            y (int): value representing the y position
        """
        super().__init__(constants.RESOURCE_IMAGE, 0.1, 100 )
        self.center_x = x
        self.center_y = y
        self.alive = True
        self.health_color = arcade.color.PURPLE

    def get_smaller(self):
        """
        Changes the image scale, causes the image to display smaller.

        Args:
            self (Resource): an instance of Resource
        """
        self.scale -= 0.02

    
    
