import random
from game import constants
from game.action import Action
import arcade 
class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        hero = cast['hero'][0]

        zombies = cast['zombies']

        walls = cast['walls']

        tower = cast["tower"][0]

        for zombie in zombies:
            zombie.attack_tower()
        
        if hero.collides_with_list(zombies):
            hero.get_hit()

        for wall in walls:
            for zombie in zombies:
                if wall.collides_with_sprite(zombie):
                    wall.get_hit()
                    zombie.velocity = [0,0]
                    if wall.get_current_health() <= 0:
                        wall.remove_from_sprite_lists()
        

        for zomb in zombies:
            if zomb.collides_with_sprite(tower):
                zomb.velocity = [0,0]
                tower.cur_health -= 0.1
            if zomb.get_current_health() <= 0:
                zomb.remove_from_sprite_lists()


