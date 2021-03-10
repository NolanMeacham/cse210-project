import sys
from game.point import Point
from game.hero import Hero
import arcade

class ArcadeInputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _keys (list): up, dn, lt, rt.
    """

    def __init__(self):
        """The class constructor."""
        self._keys = []
        self.mouse_x = 0
        self.mouse_y = 0
    
    def set_key(self, key, modifiers):
        #Ignoring modifies at this point...
        self._keys.append(key)

    def remove_key(self, key, modifiers):
        self._keys.remove(key)
    
    def is_attacking(self):
        if arcade.key.SPACE in self._keys:
            return True

    def is_building(self):
        while arcade.key.Z in self._keys:
            return True
    
    def cast_magic(self):
        if arcade.key.Q in self._keys:
            return True

    def mouse_move(self, x, y):
        self.mouse_x = x 
        self.mouse_y = y

    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        x = 0
        y = 0

        if arcade.key.A in self._keys:
            x = -1
        elif arcade.key.D in self._keys:
            x = 1

        if arcade.key.W in self._keys:
            y = 1
        elif arcade.key.S in self._keys:
            y = -1

            

        velocity = Point(x, y)
        return velocity
            

