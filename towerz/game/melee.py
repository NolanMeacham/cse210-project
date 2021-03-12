import arcade
from game import constants
from game.input_service import ArcadeInputService
import time
class Melee(arcade.Sprite):
    def __init__(self,cast):
        super().__init__(constants.HERO_IMAGE, 1,image_height=10, image_width=15)
        self.offset = 0
        self.cast = cast
        self.timer = time.time()
    def attack(self):
        if time.time() - self.timer >= 0.25:
            self.timer = time.time()
            for zombie in self.cast['zombies']:
                if self.collides_with_sprite(zombie):
                    zombie.cur_health -= 20

            for resource in self.cast['resources']:
                if self.collides_with_sprite(resource):
                    resource.get_smaller()
                    
                    resource.cur_health -= 20

                    if self.cast["resource_counter"][0].cur_health < 100:

                        self.cast["resource_counter"][0].cur_health += 10


        else:
            pass





    def shealth_melee(self):
        hero = self.cast['hero'][0]
        x = hero.center_x
        y = hero.center_y
         
        self.center_y = y 
        self.center_x = x 


        

        
        


    
        