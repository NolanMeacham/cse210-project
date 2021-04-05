import arcade
from game import constants
from game.action import Action
from game.death_screen import  DeathView
from game.towerz import TowerzView
from game.add_enemy import Add_enemy
from game.win_screen import WinView

class HandleLoseOrWinAction(Action):

    def __init__(self, window, start_screen, script):
        """
        Class constructor

        Args:
            self ():
            window ():
            start_screen ():
        """
        self.window = window
        self.start = start_screen
        self.script = script

    
    def execute(self, cast):
        tower = cast['tower'][0]
        zombies = cast['zombies']
        resource = cast['resource_counter'][0]
        hero = cast['hero'][0]
        turrets = cast['turrets']

        if tower.get_current_health() <= 0 or hero.get_current_health() <= 0:
        
            add_enemy = self.script['update'][3]
            arcade.unschedule(add_enemy.create_zombie)
            if self.script['update'][3].wave == 'Survival':
                
                win_screen = WinView(self.start, tower, cast)
                self.window.show_view(win_screen)
                tower.cur_health = constants.TOWER_HEALTH

            else:
                death_screen = DeathView(self.start, tower)
                self.window.show_view(death_screen)
                tower.cur_health = constants.TOWER_HEALTH

        
            






