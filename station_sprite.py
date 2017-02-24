"""
|<--------------------------------------------------------------------------->|
station_sprite.py is a class definition for the main sprite of the station. 
The station has no turrets but does have lights that need to go on an off.

by Philip deZonia
last modified: 2017-02-23
"""

# import required modules
import pygame
import os, sys
import math

class Loanne(apple_cat_sprite.Applecat): # is this how you inherit?
    def __init__(self, is_left):
        """load sprite image and rectangle"""
        # is this how you override?
        pygame.sprite.Sprite.__init__(self) #call sprite initializer
        
        # load hull of ship as image/surface and as rectangle
        if is_left:
            self.image, self.rect = self.load_image('station left half transfer.png')
            self.original_image = self.image
        if !is_left:
            self.image, self.rect = self.load_image('station right half transfer.png')
            self.original_image = self.image