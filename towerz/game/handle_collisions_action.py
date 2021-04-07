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

        magicks = cast["magicks"]

        # handle collisions for each actor appropriately:
        
        for zombie in zombies:
            zombie.attack_tower()

        for zombie in zombies:
            if hero.collides_with_sprite(zombie):
                
                zombie.attacking = True
                zombie.update_animation()
                hero.get_hit()
                zombie.velocity = [0,0]


        for wall in walls:
            for zombie in zombies:
                if wall.collides_with_sprite(zombie):
                    wall.get_hit()
                    zombie.attacking = True
                    zombie.update_animation()
                    zombie.velocity = [0,0]
                    if wall.get_current_health() <= 0:
                        wall.remove_from_sprite_lists()

        for magic in magicks:

            for zombie in zombies:
                if magic.collides_with_sprite(zombie):
                    if zombie.cur_health > (zombie.max_health / 4):
                        zombie.cur_health /= 2
                        sound_effect = constants.MAGIC_SOUND
                        sound_effect = arcade.load_sound(sound_effect)
                        arcade.play_sound(sound_effect)
                    else:
                        zombie.cur_health == (zombie.max_health / 4)

            if magic.center_x < 0 or magic.center_y < 0  :
                magicks.remove(magic)
            elif magic.center_x > constants.MAX_X or magic.center_y > constants.MAX_Y:
                magicks.remove(magic)

        for resource in resources:
            if resource.get_current_health() <= 0:
                resource.remove_from_sprite_lists()
        

        for zombie in zombies:
            if zombie.get_current_health() <= 0:
                zombie.update_animation()
                
                score.add_points(zombie.score_points)
            if zombie.collides_with_sprite(tower):
                zombie.attacking = True
                zombie.update_animation()
                zombie.velocity = [0,0]
                tower.cur_health -= 1
                

        # update each turret.
        for turret in turrets:
            turret.on_update()
            if turret.get_current_health() <= 0:
                turret.remove_from_sprite_lists()

        # update the bullets and check for collissions.
        for bullet in bullets:
            zombies_hit = bullet.collides_with_list(zombies)
            if bullet.center_x < 0 or bullet.center_y < 0  :
                bullets.remove(bullet)
            elif bullet.center_x > constants.MAX_X or bullet.center_y > constants.MAX_Y:
                bullets.remove(bullet)
            else: 
                for zombie in zombies_hit:
                    zombie.cur_health -= 50
                    bullets.remove(bullet)
                    break
