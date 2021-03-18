from game.point import Point
from game import constants
from game.sprite_with_health import SpriteWithHealth
from game.turret_bullet import TurretBullet
from math import atan, atan2, cos, sin, pi
import arcade
import time

class Turret(SpriteWithHealth):
    """
    Turret is a SpriteWithHealth.
    Turrets have a set amount of life and last for a limited amount of time.
    Turrets have the responsibility of searching for nearby targest and 
    shooting a bullet at them.

    Stereotype:
        ?
    
    """
    def __init__(self, x, y, cast):
        """
        Class constructor.

        Args:
            self (Turret): an instance of Turret.
            x (int): a value for the turret's x position.
            y (int): a value for the turret's y position.
        """
        super().__init__(constants.TURRET_IMAGE, constants.TURRET_SCALE, constants.TURRET_HEALTH)
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0
        self.timer = time.time()
        self.cast = cast

    def attack_enemy(self):
        """
        Searches for a nearby enemy and shoots the enemy with a bullet.

        Args:
            self(Turret): an instance of Turret.
        """
        zombies = self.cast["zombies"]
        # find the closest target to shoot at
        # the sprite_list.get_closest_sprite() returns a tuple that looksl like
        # (sprite, distance)

        # This if statement is necessary so the game doesn't crash if there aren't any
        # zombies when this method is called.
        if arcade.sprite_list.get_closest_sprite(self, zombies) != None:
            closest_enemy = arcade.sprite_list.get_closest_sprite(self, zombies)[0]

            # start the bullet at the turret's location
            start_x = self.center_x
            start_y = self.center_y

            # destination is the closest enemy
            dest_x = closest_enemy.center_x
            dest_y = closest_enemy.center_y

            # calculate the difference between these points
            diff_x = dest_x - start_x
            diff_y = dest_y - start_y

            # calculate the angle for the bullet
            angle = atan2(diff_y, diff_x)
            # print(f'closest enemy is at ({dest_x}, {dest_y}) at angle: {angle * 180/pi:.0f}')
            bullet_change_x = cos(angle) * constants.BULLET_SPEED
            bullet_change_y = sin(angle) * constants.BULLET_SPEED

            new_bullet = TurretBullet(start_x, start_y, bullet_change_x, bullet_change_y, self.cast)
            self.cast["bullets"].append(new_bullet)

            arcade.play_sound(new_bullet.bullet_sound)

        
    def on_update(self):
        """
        Updates the turrets health based on the time elapsed.
        This makes it so the tower loses 1 health point every 1.5 seconds.
        It also calls the attack_enemy method.

        Args:
            self (Turret): an instance of Turret.
        """
        if time.time() - self.timer > 1.5:
            self.attack_enemy()
            self.timer = time.time()
            self.cur_health -= 1
