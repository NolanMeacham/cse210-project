import arcade
from game import constants
from game.input_service import ArcadeInputService
import time
class Melee(arcade.Sprite):
    """
    """
    def __init__(self,cast):
        """
        Class constructor.
        Calls the constructor of the parent class.

        Args:
            self (Melee): an instance of Melee
            cast (dict): dictionary that holds all the actors

        """
        super().__init__(constants.CROSS_HAIR, 0.25)
        self.offset = 0
        self.cast = cast
        self.timer = time.time()

        self.slash_sound = arcade.load_sound(constants.HERO_SLASH_SOUND)
        self.hit_resource_sound = arcade.load_sound(constants.HERO_RESOURCE_SOUND)


    def attack(self):
        """
        Attack method. Attacks zombies.

        Args:
            self (Melee): an instance of Melee

        """
        if time.time() - self.timer >= 0.5:
            self.timer = time.time()
            
            for zombie in self.cast['zombies']:
                if self.collides_with_sprite(zombie):
                    arcade.play_sound(self.slash_sound)
                    zombie.cur_health -= 20
                    self.cast['hero'][0].attacking = True
                    self.cast['hero'][0].update_animation()
                
            for resource in self.cast['resources']:
                if self.collides_with_sprite(resource):
                    arcade.play_sound(self.hit_resource_sound)
                    resource.get_smaller()
                    
                    resource.cur_health -= 20

                    if self.cast["resource_counter"][0].cur_health < 100:

                        self.cast["resource_counter"][0].cur_health += 10
                    self.cast['hero'][0].attacking = True
                    self.cast['hero'][0].update_animation()
            
            
            
        
    





    def shealth_melee(self):
        """
        Sheath

        Args:
            self (Melee): an instance of Melee

        """
        hero = self.cast['hero'][0]
        x = hero.center_x
        y = hero.center_y
         
        self.center_y = y 
        self.center_x = x 
 