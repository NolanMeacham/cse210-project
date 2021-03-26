import arcade
import random
import math
from game import constants
from game.sprite_with_health import SpriteWithHealth
from game.tower_sprite import TowerSprite


class Zombie(SpriteWithHealth):
    """
    Zombie class is a SpriteWithHealth

    Stereotype:
        ?

    """

    def __init__(self, x, y, cast):
        """
        Class constructor. Calls the constructor for parent class first.

        Args:
            self (Zombie): an instance of Zombie
            x (int): value representing the x position
            y (int): value representing the y position
            cast (dict): dictionary that holds all the actors

        """
        super().__init__(constants.ZOMBIE_IMAGE, constants.ZOMBIE_SCALING, 100 )
        self.center_x = x
        self.center_y = y
        self.alive = True
        self.cast = cast
        self.score_points = 10
        self.speed = constants.ZOMBIE_SPEED
        self.aggro = 0

        self.character_face_direction = constants.RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0
        self.cur_texture1 = 0

        # Adjust the collision box. Default includes too much empty space
        # side-to-side. Box is centered at sprite center, (0, 0)

        self.points = [[-8, -20], [8, -20], [8, 20], [-8, 20]]

        self.idle_textures = []
        for i in range(4):
            texture = self.load_texture_pair('towerz/images/skelly_idle.png', i*150, 0, 150, 150)
            self.idle_textures.append(texture)
        
        # Load texures for running
        self.run_textures = []
        for i in range(4):
            texture = self.load_texture_pair('towerz/images/skelly_walk.png', i*150, 0, 150, 150)
            self.run_textures.append(texture)

    def attack_tower(self):
        """
        Allows Zombies to find, seek, and attack the tower.

        Args:
            self (Zombie): an instance of Zombie

        """
        hero = self.cast['hero'][0]

        start_x = self.center_x
        start_y = self.center_y

        # Get the destination location for the bullet
        if abs(hero.center_x - start_x) <= 100 and abs(hero.center_y - start_y) <= 100:


                dest_x = hero.center_x
                dest_y = hero.center_y

        else:
            dest_x = self.cast['tower'][0].center_x
            dest_y = self.cast['tower'][0].center_y

        # Do math to calculate how to get the bullet to the destination.
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        self.change_x = math.cos(angle) * self.speed
        self.change_y = math.sin(angle) * self.speed
    
    def zombie_attack(self):
        """
        Attacks whatever actor the zombie collides with

        Args:
            self (Zombie): an instance of Zombie
            
        """
        cast = self.cast
        walls = cast['walls']
        hero = cast['hero']
        tower = cast['tower']
        counter = 0
        counter += 1 
        if counter != 30:
            pass
        else:
            for wall in walls:
                if self.collides_with_sprite(wall):
                    wall.get_hit()
                    self.velocity = (0,0)
                    #TODO create strength attribute for each class. 
                    #TODO lower strength of zombie & stop zombie when collides with hero
    def update_animation(self, delta_time: float = 1/60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == constants.RIGHT_FACING:
            self.character_face_direction = constants.LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == constants.LEFT_FACING:
            self.character_face_direction = constants.RIGHT_FACING

        # Idle animation
        self.cur_texture1 += 1
        if self.cur_texture1 >= 4 * constants.UPDATES_PER_FRAME:
            self.cur_texture1 = 0
        if self.change_x == 0 and self.change_y == 0:
            frame = self.cur_texture1 // constants.UPDATES_PER_FRAME
            direction = self.character_face_direction
            self.texture = self.idle_textures[frame-1][direction]
            return


        if self.cur_texture >= 4 * constants.UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // constants.UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = self.run_textures[frame][direction]

        self.cur_texture += 1

    def load_texture_pair(self, filename, x_inc, y_inc, width, height):
            """
            Load a texture pair, with the second being a mirror image.
            """
            return [(arcade.load_texture(filename, x=x_inc, y=y_inc, width= width, height=height )), (arcade.load_texture(filename, x=x_inc, y=y_inc, width= width, height=height, flipped_horizontally=True))]