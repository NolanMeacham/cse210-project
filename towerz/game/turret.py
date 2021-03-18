from game.point import Point
from game import constants
from game.sprite_with_health import SpriteWithHealth
import arcade
import time

class Turret(SpriteWithHealth):
    """
    Turret is a SpriteWithHealth.
    Turrets have a set amount of life and last for a limited amount of time.
    Turrets have the responsibility of searching for nearby targest and 
    shooting a bullet at them.

    Stereotype:
        ?
    
    """
    def __init__(self, x, y):
        """
        Class constructor.

        Args:
            self (Turret): an instance of Turret.
            x (int): a value for the turret's x position.
            y (int): a value for the turret's y position.
        """
        super().__init__(constants.TURRET_IMAGE, constants.TURRET_SCALE, constants.TURRET_HEALTH)
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0
        self.timer = time.time()

    def attack_enemy(self):
        """
        Searches for a nearby enemy and shoots the enemy with a bullet.

        Args:
            self(Turret): an instance of Turret.
        """
        # TODO: call this method so the turret will attack the zombies
        pass
        
    def on_update(self):
        """
        Updates the turrets health based on the time elapsed.
        This makes it so the tower loses 1 health point every 1.5 seconds.

        Args:
            self (Turret): an instance of Turret.
        """
        if time.time() - self.timer > 1.5:
            self.timer = time.time()
            self.cur_health -= 1