"""
|<--------------------------------------------------------------------------->|
apple_cat_sprite.py is a class definition for the Applecat spaceship for use in our
python game. It needs to import the sprites of the ship hull and its turrets.
The role of this file is mostly graphics oriented.

Contains useful function: load_image

This doc takes a lot of advice from pygame.org/docs/tut

by Philip deZonia
last modified: 2017-02-25
"""

# import required modules
import pygame
import os, sys
import math

# we have to add hull and turrets to group so that we can draw
# them all at once
    
class Applecat(pygame.sprite.Sprite):
    """ define class for Applecat spaceship """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # call sprite initializer
        
        # load hull of ship as image/surface and as rectangle
        self.image, self.rect = self.load_image('apple_cat small3.png')
        self.original_image = self.image
    
    def update_pos(self, ship_cent, heading, player_pos = [0, 0]):
        """define position and attitude function, first argument is center
        of this ship, second is the rotation angle of it, and third is the
        position of the ship followed by the camera"""
        # perform rotation on original image
        self.image = pygame.transform.rotate(self.original_image, heading)
        
        # for recentering the image after rotating messes up the rectangle
        self.rect = self.image.get_rect()
        
        # center is screen postion, ship_cent is world position of ship,
        # player_pos is world position of player ship
        self.rect.centerx = ship_cent[0] - player_pos[0]
        self.rect.centery = ship_cent[1] - player_pos[1]
        
    def load_image(self, name, colorkey = None):
        fullname = os.path.join(
        'C:\Users\Philip H. deZonia\Documents\Python_Stuff\GamesTown', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print('Cannot load image: ', name)
            raise SystemExit, message
        image = image.convert() # comes from pygame.Surface, optimizes for screen 
        if colorkey is not None: # do optional color adjustment
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image, image.get_rect() # return surface and rectangle 