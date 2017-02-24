"""
|<--------------------------------------------------------------------------->|
station.py defines a class for making instances of the space station, this
needs to have its own class because the station is spit into two images and so
is incompatible with ship.py, stations are stationary and maybe spin in place, 
depends on whether I can get the ships to move with it.

by Philip deZonia
last modified: 2017-02-23
"""

# import required modules (maybe reduntantly)
import pygame
import os, sys
from math import *

# import custom made modules
from apple_cat_sprite import *
from turret import *
from physics import *
from laser_generator import *

class Station(pygame.sprite.Sprite):
    def __init__(self, x_root, y_root, spin_speed, name): 
        """initialize sprites and state variables"""
        pygame.sprite.Sprite.__init__(self) # call sprite initializer
        
        self.pos = [x_root, y_root]
        self.omega = spin_speed
        
        if name == "Loanne":
            self.station_left = Loanne()
            self.station_right = Loanne()
        else
            # i don't have another station sprite for now
            self.station_left = Loanne()
            self.station_right = Loanne()
            
        # tie two havles together
        self.whole_station = pygame.sprite.OrderedUpdates(self.station_left, \
        self.station_right)
    def render(self, game_window):
        