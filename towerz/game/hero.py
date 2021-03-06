from game.point import Point
from game import constants
from game.sprite_with_health import SpriteWithHealth
import arcade

class Hero(SpriteWithHealth):
    def __init__(self):
        super().__init__(constants.HERO_IMAGE, constants.HERO_SCALING, 100 )

        self.center_x = int(constants.MAX_X / 2)
        self.center_y = int(constants.HERO_Y)

        self.alive = True
    def draw_health_bar(self):
        """ Draw the health bar """

        # Draw the 'unhealthy' background
        if self.cur_health <  self.max_health and self.cur_health > 0:
            arcade.draw_rectangle_filled(center_x= constants.HERO_HEALTH_X,
                                        center_y= constants.HERO_HEALTH_Y + constants.HERO_HEALTHBAR_OFFSET_Y,
                                        width=constants.HERO_HEALTHBAR_WIDTH,
                                        height=constants.HERO_HEALTHBAR_HEIGHT,
                                        color=arcade.color.RED)

        # Calculate width based on health
        health_width = constants.HERO_HEALTHBAR_WIDTH * (self.cur_health / self.max_health)
        if self.cur_health > 0:
            arcade.draw_rectangle_filled(center_x= constants.HERO_HEALTH_X - 0.5 * (constants.HERO_HEALTHBAR_WIDTH - health_width),
                                        center_y= constants.HERO_HEALTH_Y,
                                        width=health_width,
                                        height=constants.HERO_HEALTHBAR_HEIGHT,
                                        color=arcade.color.GREEN)
    def get_hit(self):
        if self.cur_health > 0:
            self.cur_health = self.cur_health - 0.1



            
