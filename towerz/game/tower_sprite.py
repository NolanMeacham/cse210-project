from game.point import Point
from game import constants
from game.sprite_with_health import SpriteWithHealth

import arcade

class TowerSprite(SpriteWithHealth):
    """
    TowerSprite is a sprite with health.

    Stereotype:
        Information Holder
    """
    def __init__(self):
        """
        Class constructor.

        Args:
            self (TowerSprite): an instance of TowerSprite
        """
        super().__init__(constants.TOWER_IMAGE, constants.TOWER_SCALE, constants.TOWER_HEALTH)
        self.center_x = constants.TOWER_X
        self.center_y = constants.TOWER_Y
        self.change_x = 0
        self.change_y = 0