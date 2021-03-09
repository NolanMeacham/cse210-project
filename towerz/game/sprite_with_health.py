import arcade
from game import constants

class SpriteWithHealth(arcade.Sprite):
    """ 
    Sprite with hit points 
    """

    def __init__(self, image, scale, max_health):
        super().__init__(image, scale)

        # Add extra attributes for health
        self.max_health = max_health
        self.cur_health = max_health
        self.obj_name = 'test'

    def draw_health_number(self):
        """
        Draw how many hit points we have 
        """

        health_string = f"{self.cur_health}/{self.max_health}"
        arcade.draw_text(health_string,
                         start_x=self.center_x + constants.HEALTH_NUMBER_OFFSET_X,
                         start_y=self.center_y + constants.HEALTH_NUMBER_OFFSET_Y,
                         font_size=12,
                         color=arcade.color.WHITE)
    def draw_health_bar(self):
            """
            Draw the health bar 
            """

            # Draw the 'unhealthy' background
            if self.cur_health <  self.max_health and self.cur_health > 0:
                arcade.draw_rectangle_filled(center_x=self.center_x,
                                            center_y=self.center_y + constants.HEALTHBAR_OFFSET_Y,
                                            width=constants.HEALTHBAR_WIDTH,
                                            height=3,
                                            color=arcade.color.RED)

                

            # Calculate width based on health
            health_width = constants.HEALTHBAR_WIDTH * (self.cur_health / self.max_health)
            if self.cur_health > 0:
                arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (constants.HEALTHBAR_WIDTH - health_width),
                                        center_y=self.center_y - 10,
                                        width=health_width,
                                        height=constants.HEALTHBAR_HEIGHT,
                                        color=arcade.color.GREEN)
                arcade.draw_text(f"{self.cur_health}",
                         self.center_x - 100, self.center_y - 30, arcade.color.WHITE, 14, width=200, align="center")
    def get_current_health(self):
        return self.cur_health