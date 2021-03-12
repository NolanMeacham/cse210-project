
from game import constants
from game.action import Action

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction().scale(constants.HERO_MOVE_SCALE)
        hero = cast["hero"][0] # there's only one in the cast
        melee = cast['melee'][0]
        zombies = cast['zombies']
        walls = cast['walls']
        resource_counter = cast['resource_counter'][0]
        hero.change_x = direction.get_x()
        hero.change_y = direction.get_y()
        hero.gather_position_list()
        
        for wall in walls:
            wall.timed_death()

        x_dif = self._input_service.mouse_x - hero.center_x

        y_dif = self._input_service.mouse_y - hero.center_y

        per_x = x_dif * 0.1
        per_y = y_dif * 0.1

        x = hero.center_x + per_x
        y = hero.center_y + per_y

        melee.position = (x,y)



        if self._input_service.is_attacking() == True:
            melee.attack()
            
        
        
        if self._input_service.is_building() == True and resource_counter.cur_health >= 20:
            hero.build_wall()
            resource_counter.cur_health -= 20

        
        if self._input_service.cast_magic() == True:
            for wall in walls:
                wall.cast_magic()

            

