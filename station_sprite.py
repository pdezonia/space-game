"""
|<--------------------------------------------------------------------------->|
station_sprite.py is a class definition for the main sprite of the station. 
The station has no turrets but does have lights that need to go on an off.

by Philip deZonia
last modified: 2017-02-26
"""

# import required modules
import pygame
import os, sys
import math
import apple_cat_sprite

class Loanne(apple_cat_sprite.Applecat): # is this how you inherit?
    def __init__(self, side_id):
        """get sprite image and rectangle, argument is 'L' or 'R' to designate
        sprite halves"""
        # is this how you override? yeah
        pygame.sprite.Sprite.__init__(self) #call sprite initializer
        
        if side_id == 'L':
            self.is_left = True
        if side_id == 'R':
            self.is_left = False
        
        # load hull of ship as image/surface and as rectangle
        if self.is_left:
            self.image, self.rect = self.load_image('station left half large transfer.png')
            self.original_image = self.image
        else:
            self.image, self.rect = self.load_image('station right half large transfer.png')
            self.original_image = self.image
    
    def update_pos(self, position, player_pos = [0, 0]):
        """decide where center of station is as [x, y] in world coords, 
        third argument is player ship world position if this object is 
        not followed by the camera"""
        if self.is_left:
            self.rect.right = position[0] - player_pos[0]
            self.rect.centery = position[1] - player_pos[1]
        else:
            self.rect.left = position[0] - player_pos[0]
            self.rect.centery = position[1] - player_pos[1]