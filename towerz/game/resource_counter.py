from game.sprite_with_health import SpriteWithHealth
from game import constants
import arcade

class ResourceCounter(SpriteWithHealth):
    def __init__(self, x, y):
        super().__init__(None, None, 100 )
        self.center_x = x
        self.center_y = y
        self.health_color = arcade.color.PURPLE

    def draw_health_bar(self):
            """
            Draw the health bar 
            """

            # Draw the 'unhealthy' background
            if self.cur_health <  self.max_health and self.cur_health > 0:
                arcade.draw_rectangle_filled(center_x=self.center_x,
                                            center_y=self.center_y + constants.HEALTHBAR_OFFSET_Y,
                                            width=250,
                                            height=20,                                            
                                            color=arcade.color.BLACK)

                

            # Calculate width based on health
            health_width = constants.HEALTHBAR_WIDTH * (self.cur_health / self.max_health)
            if self.cur_health > 0:
                arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (constants.HEALTHBAR_WIDTH - health_width),
                                        center_y=self.center_y - 10,
                                        width=250,
                                        height=20,
                                        color=self.health_color)
                display_health = round(self.cur_health)
                arcade.draw_text(f"Resources: {display_health}",
                        self.center_x - 181, self.center_y + 30, arcade.color.WHITE, 14, width=200, align="center")
    