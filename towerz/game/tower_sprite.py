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
        self.texture = arcade.load_texture("towerz/images/castle_tile.png", 80, 0, 40, 40)
        self.points = [[-15, -13], [15, -13], [15, 13], [-15, 13]]

    def draw_health_bar(self):
        """ 
        Draw the tower health bar.
        
        Args:
            self (TowerSprite): an instance of TowerSprite
        """
        # Draw the 'unhealthy' background
        if self.cur_health <  self.max_health and self.cur_health > 0:
            arcade.draw_rectangle_filled(center_x= constants.TOWER_HEALTH_X,
                                        center_y= constants.TOWER_HEALTH_Y+ constants.HERO_HEALTHBAR_OFFSET_Y,
                                        width=constants.HERO_HEALTHBAR_WIDTH,
                                        height=constants.HERO_HEALTHBAR_HEIGHT,
                                        color=arcade.color.RED)

        # Calculate width based on health
        health_width = constants.HERO_HEALTHBAR_WIDTH * (self.cur_health / self.max_health)
        if self.cur_health > 0:
            arcade.draw_rectangle_filled(center_x= constants.TOWER_HEALTH_X - 0.5 * (constants.HERO_HEALTHBAR_WIDTH - health_width),
                                        center_y= constants.TOWER_HEALTH_Y,
                                        width=health_width,
                                        height=constants.HERO_HEALTHBAR_HEIGHT,
                                        color=arcade.color.GREEN)
            display_health = round(self.cur_health)
            arcade.draw_text(f"Tower HP: {display_health}",
                        constants.TOWER_HEALTH_X - 178, constants.TOWER_HEALTH_Y + 30, arcade.color.WHITE, 14, width=200, align="center")