"""
|<--------------------------------------------------------------------------->|
turret.py is a class definition for the turret for spaceships for use in our
python game. It needs to import the sprites of the ship's turrets.
It also needs to dictate the turret locations relative to the center or top 
left corner of the ship sprite and rotate the turret.

Contains useful function: load_image

This doc takes a lot of advice from pygame.org/docs/tut

by Philip deZonia
last modified: 2017-02-09
"""

# import required modules
import pygame
import os, sys
from math import *

""" define useful function: load_image """
def load_image(name, colorkey = None):
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
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect() # return surface and rectangle

class Turret(pygame.sprite.Sprite):
    def __init__(self, ship_type, turret_num):
        pygame.sprite.Sprite.__init__(self) # call sprite initializer
        
        # ship_type [either AC or PH] determines which color turret to import
        # and where to place it
        if ship_type == 'AC':
            self.image, self.rect = load_image('turret_small_AC.png')
            # define turret locations relative to center of hull
            if turret_num == 1:
                tx, ty = 77, 0
            if turret_num == 2:
                tx, ty = 39, 32
            if turret_num == 3:
                tx, ty = -23, 31
            if turret_num == 4:
                tx, ty = -60, 0
            if turret_num == 5:
                tx, ty = -23, -31
            if turret_num == 6:
                tx, ty = 39, -32
        self.x_disp_std = tx
        self.y_disp_std = ty
        # print turret_num
        
        # save original turret sprite
        self.original_image = self.image
    
    def move_and_rotate(self, ship_pos, ship_angle, turr_angle):
        """move with ship and rotate to angle fed into function"""
        # specify length of barrel in pixels
        b_length = 24
        
        # calculate new displacement vectors
        center_vector_relative = [self.x_disp_std*cos(-ship_angle*pi/180) - \
        self.y_disp_std*sin(-ship_angle*pi/180), \
        self.x_disp_std*sin(-ship_angle*pi/180) + \
        self.y_disp_std*cos(-ship_angle*pi/180)]
        
        # print center_vector_relative
        
        center_vector_relative[0] = int(center_vector_relative[0])
        center_vector_relative[1] = int(center_vector_relative[1])
        
        center_vector_total = [ship_pos[0] + center_vector_relative[0],
        ship_pos[1] + center_vector_relative[1]]
        
        # rotate
        self.image = pygame.transform.rotate(self.original_image, turr_angle)
        
        # print(center_vector_total)
        
        # place image down
        self.rect = self.image.get_rect()
        self.rect.center = center_vector_total
        
        # calculate end of barrel location
        barrel_end_rel = [b_length*cos(-turr_angle*pi/180), \
        b_length*sin(-turr_angle*pi/180)]
        
        barrel_end_abs = [0, 0]
        barrel_end_abs[0] = center_vector_total[0] + barrel_end_rel[0]
        barrel_end_abs[1] = center_vector_total[1] + barrel_end_rel[1]
        
        # return turret positions for laser generator function
        # maybe even return position of end of barrel
        return barrel_end_abs
    # end of move_and_rotate
# A
# | Give
# | me
# | space
# V