"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
enhanced_sprite.py is a class definition that adds custom functionality
for the sprites used in our space game such as loading images and
changing position and heading.
"""

import os
import sys
import math
import pygame


class EnhancedSprite(pygame.sprite.Sprite):
    def __init__(self):
        """ The initialization method is intended to be overridden to
        load the image file belonging to the sprite in question. If not
        overridden, will load a strange image of a square.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = self.load_image('testBackSquare.png')
        self.original_image = self.image
    
    def update_pos(self, sprite_center, 
                   angular_offset, player_pos=[0, 0]):
        """player_pos is used to offset sprites other than those of
        player ship to make the world move around the player. This
        method modifies the sprite properties centerx, centery, rect,
        and image.
        """
        self.image = pygame.transform.rotate(
            self.original_image, angular_offset)
        self.rect = self.image.get_rect()
        self.rect.centerx = sprite_center[0] - player_pos[0]
        self.rect.centery = sprite_center[1] - player_pos[1]
    
    def load_image(self, name, colorkey=None):
        """This method loads sprite objects into the game environment.
        this funciton is a copy from pygame documentation at 
        http://www.pygame.org/docs/tut/ChimpLineByLine.html which was
        last accessed in March 2017.
        """
        fullname = os.path.join(
        'C:\Users\Philip H. deZonia\Documents\Python_Stuff\GamesTown', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print('Cannot load image: ', name)
            raise SystemExit, message
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image, image.get_rect() # return surface and rectangle 