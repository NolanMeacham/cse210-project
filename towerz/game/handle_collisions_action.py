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
        
        
        if hero.collides_with_list(zombies):
            hero.get_hit()

