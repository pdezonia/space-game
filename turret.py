"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
turret.py is a class definition for spaceship turrets it serves as a
base class for ship specific turrets. Extending classes will replace
the sprite image and relative turret locations on the ship.
This is a refactored version of turret.py.
"""

import pygame
from math import *
from enhanced_sprite import EnhancedSprite


class Turret(EnhancedSprite):
    def __init__(self):
        """This method is meant to be overridden. Loads Applecat
        by defualt.
        """
        self.barrel_length = 24
        self.relative_x_offset = 0
        self.relative_y_offset = 0
        self.image, self.rect = (
            self.load_image('turret_small_AC.png'))
        self.original_image = self.image
    
    def update_pos(self, ship_pos, ship_angle, 
                   turret_angle, player_pos=[0, 0]):
        """Move with ship and rotate sprite image."""
        center_vector_relative = [
            self.relative_x_offset*cos(-ship_angle*pi/180)
            - self.relative_y_offset*sin(-ship_angle*pi/180),
            self.relative_x_offset*sin(-ship_angle*pi/180)
            + self.relative_y_offset*cos(-ship_angle*pi/180)]
        center_vector_relative[0] = int(center_vector_relative[0])
        center_vector_relative[1] = int(center_vector_relative[1])
        center_vector_total = [ship_pos[0] + center_vector_relative[0]
            - player_pos[0], ship_pos[1] + center_vector_relative[1]
            - player_pos[1]]
        self.image = pygame.transform.rotate(self.original_image,
                                             turret_angle)
        self.rect = self.image.get_rect()
        self.rect.center = center_vector_total
        barrel_muzzle_pos_rel = [
            self.barrel_length*cos(-turret_angle*pi/180),
            self.barrel_length*sin(-turret_angle*pi/180)]
        barrel_muzzle_pos_abs = [center_vector_total[0]
            + barrel_muzzle_pos_rel[0], center_vector_total[1]
            + barrel_muzzle_pos_rel[1]]
        return barrel_muzzle_pos_abs