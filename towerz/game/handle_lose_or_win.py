import arcade
from game import constants
from game.action import Action
from game.death_screen import  DeathView
from game.towerz import TowerzView
from game.add_enemy import Add_enemy

class HandleLoseOrWinAction(Action):
    """
    """
    def __init__(self, window, start_screen):
        """
        Class constructor

        Args:
            self ():
            window ():
            start_screen ():
        """
        self.window = window
        self.start = start_screen

    
    def execute(self, cast):
        """
        Implements the execute method from Action class.

        Args:
            self ():
            cast (dict):
        """
        tower = cast['tower'][0]
        zombies = cast['zombies']
        resource = cast['resource_counter'][0]
        hero = cast['hero'][0]
        turrets = cast['turrets']

        if tower.get_current_health() <= 0:
            for zombie in zombies:
                zombie.remove_from_sprite_lists()
            for turret in turrets:
                turret.remove_from_sprite_lists()
            
            resource.cur_health = 0
            hero.cur_health = 100

            death_screen = DeathView(self.start, tower)
            self.window.show_view(death_screen)
            






