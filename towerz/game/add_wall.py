from game import constants
import random
import arcade
from game.action import Action
from game.wall import Wall

class Add_Wall(Action):

    def __init__(self):
        pass
    def execute(self, cast):
        self.cast = cast

    def build_wall(self, hero):
        list = hero.get_position_list()
        x = list[1][0]
        y = list[1][1]
        wall = Wall(x,y,self.cast)
        self.cast['walls'].append(wall)
    
