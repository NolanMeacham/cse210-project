import arcade
from game import constants
from game.action import Action
from game.death_screen import  DeathView
from game.towerz import TowerzView
from game.add_enemy import Add_enemy

class HandleLoseOrWinAction(Action):

    def __init__(self, window, start_screen):
        self.window = window
        self.start = start_screen

    
    def execute(self, cast):
        tower = cast['tower'][0]
        zombies = cast['zombies']
        resource = cast['resource_counter'][0]
        hero = cast['hero'][0]




        if tower.cur_health <= 0:
            for zombie in zombies:
                zombie.remove_from_sprite_lists()
            death_screen = DeathView(self.start, tower)
            self.window.show_view(death_screen)
            resource.cur_health = 0
            hero.cur_health = 100
            for zombie in zombies:
                zombie.remove_from_sprite_lists()
            






