"""
|<--------------------------------------------------------------------------->|
station.py defines a class for making instances of the space station, this
needs to have its own class because the station is spit into two images and so
is incompatible with ship.py, stations are stationary and maybe spin in place, 
depends on whether I can get the ships to move with it.

by Philip deZonia
last modified: 2017-02-26
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
import station_sprite

class Station(pygame.sprite.Sprite):
    def __init__(self, x_root, y_root, spin_speed, name): 
        """initialize sprites and state variables"""
        pygame.sprite.Sprite.__init__(self) # call sprite initializer
        
        self.pos = [x_root, y_root]
        self.omega = spin_speed
        
        if name == "Loanne":
            self.station_left = station_sprite.Loanne('L')
            self.station_right = station_sprite.Loanne('R')
        else:
            # i don't have another station sprite for now
            self.station_left = station_sprite.Loanne('L')
            self.station_right = station_sprite.Loanne('R')
            
        # tie two havles together
        self.whole_station = pygame.sprite.OrderedUpdates(self.station_left, \
        self.station_right)
        
        # assign position
        self.station_left.update_pos(self.pos)
        self.station_right.update_pos(self.pos)

    def motion(self, player_pos = [0, 0]):
        """update position of station, station doesn't really move relative to
        world coords but has to have screen position changed as player ship moves,
        only takes player ship world pos as its arguments"""
        self.station_left.update_pos(self.pos, player_pos)
        self.station_right.update_pos(self.pos, player_pos)
    
    def render(self, game_window):
        """render ship at root position, takes game surface object"""
        self.whole_station.update()
        self.whole_station.draw(game_window)