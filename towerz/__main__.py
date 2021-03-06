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
from game.tower_sprite import TowerSprite
import arcade


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    # add the hero
    hero = Hero()
    cast["hero"] = [hero]

    # add the zombies
    cast['zombies'] = arcade.SpriteList()

    for i in range (5):
        random_x = random.randint(0, (constants.MAX_X-50))
        random_y =  random.randint(0,(constants.MAX_Y-50))
        zombie = Zombie(random_x, random_y)
        cast["zombies"].append(zombie)

    # add the tower
    tower = TowerSprite()
    cast["tower"] = [tower]


    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    towerz = Towerz(cast, script, input_service)
    towerz.setup()
    arcade.run()


if __name__ == "__main__":
    main()