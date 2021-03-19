from game.sprite_with_health import SpriteWithHealth
from game import constants
import arcade

class ResourceCounter(SpriteWithHealth):
    def __init__(self, x, y):
        super().__init__(None, None, 100 )
        self.center_x = x
        self.center_y = y
        self.health_color = arcade.color.PURPLE
        self.cur_health = 0

    def draw(self):
        """
        Override the draw method

        Args:
            self (ResourceCounter): an instance of ResourceCounter
        """
        self.draw_health_bar()

    def draw_health_bar(self):
            """
            Draw the health bar 
            """

            # Draw the 'unhealthy' background
            if self.cur_health <  self.max_health:
                arcade.draw_rectangle_filled(center_x=self.center_x,
                                            center_y=self.center_y + constants.HEALTHBAR_OFFSET_Y,
                                            width=constants.RESOURCE_COUNTER_WIDTH,
                                            height=20,                                            
                                            color=arcade.color.RED)

                

            # Calculate width based on health
            health_width = constants.RESOURCE_COUNTER_WIDTH * (self.cur_health / self.max_health)
            if self.cur_health > 0:
                arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (constants.RESOURCE_COUNTER_WIDTH - health_width),
                                        center_y=self.center_y - 10,
                                        width=health_width,
                                        height=20,
                                        color=self.health_color)
            display_health = round(self.cur_health)
            arcade.draw_text(f"Resources: {display_health}",
                    self.center_x - 181, self.center_y + 30, arcade.color.WHITE, 14, width=200, align="center")
    