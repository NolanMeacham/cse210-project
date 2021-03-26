import random
from game import constants
from game.action import Action
from game.death_screen import DeathView
import time
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

        walls = cast['walls']

        tower = cast["tower"][0]

        turrets = cast["turrets"]

        bullets = cast["bullets"]

        score = cast["score"][0]

        resources = cast["resources"]

        # handle collisions for each actor appropriately:
        
        for zombie in zombies:
            zombie.attack_tower()
        
        if hero.collides_with_list(zombies):
            hero.get_hit()

        for wall in walls:
            for zombie in zombies:
                if wall.collides_with_sprite(zombie):
                    wall.get_hit()
                    zombie.velocity = [0,0]
                    if wall.get_current_health() <= 0:
                        wall.remove_from_sprite_lists()

        for resource in resources:
            if resource.get_current_health() <= 0:
                resource.remove_from_sprite_lists()
        

        for zomb in zombies:
            if zomb.collides_with_sprite(tower):
                zomb.velocity = [0,0]
                tower.cur_health -= 5
            if zomb.get_current_health() <= 0:
                zomb.update_animation()
                
                score.add_points(zomb.score_points)
                

        # update each turret.
        for turret in turrets:
            turret.on_update()
            if turret.get_current_health() <= 0:
                turret.remove_from_sprite_lists()

        # update the bullets and check for collissions.
        for bullet in bullets:
            zombies_hit = bullet.collides_with_list(zombies)
            for zombie in zombies_hit:
                zombie.cur_health -= 25

            # This removes the bullets that are off screen
            if bullet.center_x < 0 or bullet.center_y < 0:
                bullets.remove(bullet)
            if bullet.center_x > constants.MAX_X or bullet.center_y > constants.MAX_Y:
                bullets.remove(bullet)
