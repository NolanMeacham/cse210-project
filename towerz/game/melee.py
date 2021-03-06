import arcade
from game import constants
from game.input_service import ArcadeInputService
import time
class Melee(arcade.Sprite):
    def __init__(self,cast):
        super().__init__(constants.HERO_IMAGE, 1,image_height=10, image_width=15)
        self.offset = 0
        self.cast = cast
    def attack(self, direction):
        facing = direction
        hero = self.cast['hero'][0]
        x = hero.center_x
        y = hero.center_y
        if facing == 1:
            self.offset = 40

        elif facing == -1:
            self.offset = -40
        self.center_y = y 
        self.center_x = x + self.offset

        for zombie in self.cast['zombies']:
            if self.collides_with_sprite(zombie):
                zombie.cur_health -= 20



    def shealth_melee(self):
        hero = self.cast['hero'][0]
        x = hero.center_x
        y = hero.center_y
         
        self.center_y = y 
        self.center_x = x 

        

        
        


    
        