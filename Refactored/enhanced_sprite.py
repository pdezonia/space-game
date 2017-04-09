"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
enhanced_sprite.py is a class definition that adds custom functionality
for the sprites used in our space game such as loading images and
changing position and heading.
"""

import os
import sys
from math import *
import pygame


class EnhancedSprite(pygame.sprite.Sprite):
    def __init__(self):
        """ The initialization method is intended to be overridden to
        load the image file belonging to the sprite in question. If not
        overridden, will load a strange image of a square.
        """
        self._create_sprite_image('testBackSquare.png')
        _create_hitboxes()
        
    def _create_sprite_image(self, file_name):
        """Loads sprite image and original image for preserving quality
        on transformations.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = self.load_image(file_name)
        self.original_image = self.image
        
    def _create_hitboxes(self):
        """Makes a list of circle centers and radii of form 
        [centerx, centery, radius]"""
        self.hit_box_centers_and_radii = []
    
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
        
    def overlap_detector(self, incoming_beams):
        """Takes list of lines and counts how many overlap with sprite
        hitbox cirlces. Lines are expressed as (length, angle, origin)
        Returns number of lines that overlap with at
        least one circle.
        """
        dot_spacing = 10
        number_of_hits = 0
        for beam in incoming_beams:
            length, angle, x0, y0 = beam
            angle = radians(angle)
            beam_points = range(0, length, dot_spacing)
            for point in beam_points:
                beam_point_coord = [x0 + point*cos(angle),
                                    y0 + point*sin(angle)]
                for hitbox in self.hit_box_centers_and_radii:
                    if self._dist([hitbox[0], hitbox[1]],
                                   beam_point_coord) < hitbox[2]:
                        number_of_hits += 1
        return number_of_hits
        
    def _dist(self, point1, point2):
        """Return pythagorean distance between 
        two points in cartesian space.
        """
        return sqrt(
            (abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]))**2)
    
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
        # return surface and rectangle 
        return image, image.get_rect() 