from game.action import Action
from game import constants

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            _output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()

        hero = cast["hero"][0] # there's only one
        zombies = cast['zombies']
        melee = cast['melee'][0]
        tower = cast["tower"][0]
        walls = cast['walls']
        turrets = cast['turrets']
        bullets = cast['bullets']
        resource_counter = cast['resource_counter'][0]
        resources = cast['resources']
        score = cast["score"][0]

        
    
        self._output_service.draw_actor(melee)

        for turret in turrets:
            self._output_service.draw_actor(turret)
            turret.draw_health_bar()

        for bullet in bullets:
            self._output_service.draw_actor(bullet)

        self._output_service.draw_actor(tower)

        for zombie in zombies:
            self._output_service.draw_actor(zombie)
            zombie.draw_health_bar()

        for wall in walls:
            self._output_service.draw_actor(wall)

        for resource in resources:
            self._output_service.draw_actor(resource)

        self._output_service.draw_actor(hero)
        hero.draw_health_bar()
        tower.draw_health_bar()
        resource_counter.draw_health_bar()
        melee.shealth_melee()
        if len(walls) > 2:
            for wall in walls:
                wall.draw_magic()

        self._output_service.draw_actor(score)
        
        self._output_service.flush_buffer()

