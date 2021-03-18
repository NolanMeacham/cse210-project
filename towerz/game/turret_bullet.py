from game import constants
import arcade
import time

class TurretBullet(arcade.Sprite):
    """
    Bullet that is fired by the turret.

    Stereotype:
        ?

    """
    def __init__(self, x, y, change_x, change_y, cast):
        """
        class constructor.

        Args:
            self (TurretBullet): an instance of TurretBullet
            x (int): starting x position
            y (int): starting y position

        """
        super().__init__(constants.BULLET_IMAGE, constants.BULLET_SCALE)

        self.center_x = x
        self.center_y = y
        self.change_x = change_x
        self.change_y = change_y

        self.cast = cast

        self.bullet_sound = arcade.load_sound(constants.BULLET_SOUND)

