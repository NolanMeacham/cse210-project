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
        super().__init__(constants.HERO_IMAGE, 2, 100)

        self.center_x = int(constants.MAX_X / 2)
        self.center_y = int(constants.HERO_Y)
        self.cast = cast
        self._position_list = []
        self.change_angle = 45
        # self.texture = arcade.load_texture(constants.HERO_IMAGE)
        self.alive = True   

        # Default to face-right
        self.character_face_direction = constants.RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0
        self.cur_texture1 = 0
        self.cur_texture2 = 0

        # Adjust the collision box. Default includes too much empty space
        # side-to-side. Box is centered at sprite center, (0, 0)

        self.points = [[-8, -20], [8, -20], [8, 20], [-8, 20]]

        # --- Load Textures ---

        main_path = "towerz/images/adventurer"
 

        # Load textures for idle standing
        self.idle_textures = []
        for i in range(15):
            texture = self.load_texture_pair('towerz/images/Knightidle_strip.png', i*64, 0, 64, 64)
            self.idle_textures.append(texture)
        
        # Load texures for running
        # self.run_textures = []
        # for i in range(5):
        #     texture = self.load_texture_pair(f'{main_path}-run-0{i+1}.png')
        #     self.run_textures.append(texture)
        self.run_textures = []
        for i in range(8):
            texture = self.load_texture_pair('towerz/images/Knightrun_strip.png', i*96, 0, 96, 64)
            self.run_textures.append(texture)
        
        self.attack_textures = []
    



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


    def update_animation(self, delta_time: float = 1/60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == constants.RIGHT_FACING:
            self.character_face_direction = constants.LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == constants.LEFT_FACING:
            self.character_face_direction = constants.RIGHT_FACING

        # Attack animation
        
        
            
            

        

        # Idle animation
        
        self.cur_texture1 += 1
        if self.cur_texture1 >= 10 * constants.UPDATES_PER_FRAME:
            self.cur_texture1 = 0
        if self.change_x == 0 and self.change_y == 0 and self.alive == True :
            frame = self.cur_texture1 // constants.UPDATES_PER_FRAME
            direction = self.character_face_direction
            self.texture = self.idle_textures[frame-1][direction]
            return

        #Walking animation
        self.cur_texture += 1
        if self.cur_texture >= 8 * constants.UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // constants.UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = self.run_textures[frame][direction]


       
        


        

    def load_texture_pair(self, filename, x_inc, y_inc, width, height):
            """
            Load a texture pair, with the second being a mirror image.
            """
            return [(arcade.load_texture(filename, x=x_inc, y=y_inc, width= width, height=height )), (arcade.load_texture(filename, x=x_inc, y=y_inc, width= width, height=height, flipped_horizontally=True))]
        
        
        