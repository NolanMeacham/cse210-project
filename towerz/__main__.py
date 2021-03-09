import random
from game import constants
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import ArcadeInputService
from game.output_service import ArcadeOutputService
from game.hero import Hero
from game.towerz import Towerz
from game.zombie import Zombie
from game.melee import Melee
from game.tower_sprite import TowerSprite
from game.add_enemy import Add_enemy
from game.wall import Wall
import arcade


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    # add the hero
    hero = Hero(cast)
    cast["hero"] = [hero]
    
    melee = Melee(cast)
    cast["melee"] = [melee]

    # add the zombies
    cast['zombies'] = arcade.SpriteList()


    # add the tower
    tower = TowerSprite()
    cast["tower"] = [tower]

    # add the wall
    cast["walls"] = arcade.SpriteList()


    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    add_enemy = Add_enemy()
    

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action, add_enemy]
    script["output"] = [draw_actors_action]

    # start the game
    towerz = Towerz(cast, script, input_service)
    towerz.setup()
    arcade.run()


if __name__ == "__main__":
    main()

"""
I can't believe I have to listen to this crap all the time. It is absolutely horrid. I want it to die in a very, very, very large hole that has a freaking spike in the bottom
actually, I would like that hole to have multiple spikes. If all the spikes where in the hole, then the music would definitely die. Music can't survive spikes. Nothing can.
In fact, I don't even think superman can survive spikes. You know who can survive spikes though? Me, I can. I can do it. I'm like the little train engine that could, and
everyone else is the little train engine that couldn't. HA. Fight me you insignificant piles of swelsh and slop. You can't win even if I wanted to lose. How's that for 
awsomeness. Eat my large pineapple you fiends. You never stood a chance against my genius. Don't dwell on the fact that it took about 10 seconds for me to remember how to 
spell the word "genious". I'm smarterer than you, and you know it's true. 


transcriptsubmit@byui.edu
"""