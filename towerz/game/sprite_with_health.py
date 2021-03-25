import arcade
from game import constants

class SpriteWithHealth(arcade.Sprite):
    """ 
    SpriteWithHealth is an arcade.Sprite and inherits attributes
    and methods from the parent class.

    Sprite with hit points, a base class to represent all sprites
    that have health.

    Stereotype:
        ?

    """

    def __init__(self, image, scale, max_health):
        """
        Class constructor, calls the parent class constructor first.

        Args:
            self (SpriteWithHealth): an instance of SpriteWithHealth
        """
        super().__init__(image, scale)

        # Add extra attributes for health
        self.max_health = max_health
        self.cur_health = max_health
        self.obj_name = 'test'
        self.health_color = arcade.color.RED

    def draw(self):
        """
        Override the draw method to include drawing health bar and number.

        Args:
            self (SpriteWithHealth): an instance of SpriteWithHealth

        """
        super().draw()
        self.draw_health_bar()
        # self.draw_health_number()

    def draw_health_number(self):
        """
        Draw how many hit points we have 

        Args:
            self (SpriteWithHealth): an instnace of the class
        """

        health_string = f"{self.cur_health}"
        arcade.draw_text(health_string,
                         start_x=self.center_x + constants.HEALTH_NUMBER_OFFSET_X,
                         start_y=self.center_y + constants.HEALTH_NUMBER_OFFSET_Y,
                         font_size=12,
                         color=arcade.color.WHITE)

    def draw_health_bar(self):
        """
        Draw the health bar 

        Args:
            self (SpriteWithHealth): an instance of the class
        """
        # Draw the 'unhealthy' background
        if self.cur_health <  self.max_health and self.cur_health > 0:
            arcade.draw_rectangle_filled(center_x=self.center_x,
                                        center_y=self.center_y + constants.HEALTHBAR_OFFSET_Y,
                                        width=constants.HEALTHBAR_WIDTH,
                                        height=3,
                                        color=self.health_color)

            

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
        """
        Get the Sprite's current health.

        Args:
            self (SpriteWithHealth): an instance of SpriteWithHealth

        Returns:
            cur_health (int): the Sprite's current health
        """
        return self.cur_health

    def set_current_health(self, health):
        """
        Updates the current health by adding the given value,
        which can also be negative numbers.

        Args:
            self (SpriteWithHealth): an instance of SpriteWithHealth
            health (int): a positive or negative value used to update the current health
        """
        self.cur_health += health

    def load_texture_pair(self, filename):
        """
        Load a texture pair, with the second being a mirror image.
        """
        return [(arcade.load_texture(filename)), (arcade.load_texture(filename, flipped_horizontally=True))]
        

    def update_animation(self, delta_time: float = 1/60):

        # # Figure out if we need to flip face left or right
        # if self.change_x < 0 and self.character_face_direction == constants.RIGHT_FACING:
        #     self.character_face_direction = constants.LEFT_FACING
        # elif self.change_x > 0 and self.character_face_direction == constants.LEFT_FACING:
        #     self.character_face_direction = constants.RIGHT_FACING

        # # Idle animation
        # if self.change_x == 0 and self.change_y == 0:
        #     self.texture = self.idle_texture_pair[self.character_face_direction]
        #     return

        # # Walking animation
        # self.cur_texture += 1
        # if self.cur_texture > 7 * constants.UPDATES_PER_FRAME:
        #     self.cur_texture = 0
        # frame = self.cur_texture // constants.UPDATES_PER_FRAME
        # direction = self.character_face_direction
        # self.texture = self.walk_textures[frame][direction]
        pass
                