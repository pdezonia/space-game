"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
applecat_turret.py is a class definition for sprites belonging to
Applecat ships.
Combined with refactored turret.py, this file replaces the
functionality of the original turret.py.
"""

import pygame
from turret import Turret


class ApplecatTurret(Turret):
    def __init__(self, turret_number):
        """Override initialization to specify all possible turret 
        locations and load image for specific sprite. turret_number
        specifies which turret location. Remember that y increases as a
        point moves towards the bottom of the screen.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = self.load_image('turret_small_AC.png')
        self.original_image = self.image
        self.barrel_length = 24
        if turret_number == 1:
            tx, ty = 77, 0
        if turret_number == 2:
            tx, ty = 39, -32
        if turret_number == 3:
            tx, ty = -23, -31
        if turret_number == 4:
            tx, ty = -60, 0
        if turret_number == 5:
            tx, ty = -23, 31
        if turret_number == 6:
            tx, ty = 39, 32
        self.relative_x_offset = tx
        self.relative_y_offset = ty