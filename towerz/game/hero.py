from game.point import Point
from game import constants
from game.sprite_with_health import SpriteWithHealth
from game.wall import Wall
from game.turret import Turret
import arcade

class Hero(SpriteWithHealth):
    """
    Hero is a SpriteWithHealth
    This is the main playable character.

    Stereotype:
        ?

    """
    def __init__(self, cast):
        """
        Class constructor.

        Args:
            self (Hero): an instance of Hero
            cast (dict): dictionary that holds all the actors in the game
        """
        super().__init__(constants.HERO_IMAGE, constants.HERO_SCALING, 100)

        self.center_x = int(constants.MAX_X / 2)
        self.center_y = int(constants.HERO_Y)
        self.cast = cast
        self._position_list = []
        self.change_angle = 45

        self.alive = True


    def draw_health_bar(self):
        """
        Draw the health bar 
        
        """
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
            display_health = round(self.cur_health)
            arcade.draw_text(f"Hero HP: {display_health}",
                        constants.HERO_HEALTH_X - 181, constants.HERO_HEALTH_Y + 30, arcade.color.WHITE, 14, width=200, align="center")
    
    
    def get_hit(self):
        """
        Reduces the hero's health by the amoung declared in constants.
        """
        if self.cur_health > 0:
            self.cur_health = self.cur_health - constants.ZOMBIE_HIT


    def gather_position_list(self):
        """
        """
        position = (self._get_position())
        self._position_list.append(position)
        if len(self._position_list) > 2:
            self._position_list.pop(0)


    def get_position_list(self):
        """
        """
        return self._position_list

    def build_wall(self):
        """
        """
        if len(self.cast['walls']) < 4:
            pos_list = self.get_position_list()
            x = pos_list[1][0]
            y = pos_list[1][1]
            wall = Wall(x,y,self.cast)
            self.cast['walls'].append(wall)

    def build_turret(self):
        """
        Builds a turret at the hero's current location
        """
        x = self._get_center_x()
        y = self._get_center_y()
        turret = Turret(x, y, self.cast)
        self.cast['turrets'].append(turret)
            
