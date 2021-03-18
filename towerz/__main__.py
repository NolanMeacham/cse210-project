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
from game.towerz import TowerzView
from game.start_screen import StartView
from game.zombie import Zombie
from game.melee import Melee
from game.tower_sprite import TowerSprite
from game.add_enemy import Add_enemy
from game.wall import Wall
from game.turret import Turret
from game.score import Score
from game.resource_counter import ResourceCounter
from game.death_screen import DeathView
from game.handle_lose_or_win import HandleLoseOrWinAction
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

    # add the turret
    cast["turrets"] = arcade.SpriteList()

    # add the bullets
    cast["bullets"] = []

    # add the resources
    cast['resources'] = arcade.SpriteList()

    # add the score
    score = Score()
    cast["score"] = [score]

    # add the resource counter
    resource_counter = ResourceCounter(200,50)
    cast['resource_counter'] = [resource_counter]


    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    

    window = arcade.Window(constants.MAX_X, constants.MAX_Y, "Towerz") 
    start_screen = StartView(cast, script, input_service)   

    handle_lose_or_win = HandleLoseOrWinAction(window, start_screen)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action, handle_lose_or_win]
    script["output"] = [draw_actors_action]

    # start the game
    window.show_view(start_screen)
    arcade.run()


if __name__ == "__main__":
    main()
