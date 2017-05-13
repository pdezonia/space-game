"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
coordinate_converter.py is a module containing the function that
converts actual game coordinate to screen coordinates.
"""

import pygame
import os, sys
from math import *

def det_screen_coords(true_pos, player_pos, game_window):
    """ Takes actual position of an object (inside the game world), the
    position of the player ship (more precisely the point in space that
    the camera is centered around), and the game window to determine
    where in the game window the object should be rendered.
    """
    # calculate screen size
    to_center = [game_window.get_width()/2, game_window.get_height()/2]
    # calculate screen coordinate origin location
    screen_origin_pos = [x - y for x, y in zip(player_pos, to_center)]
    return [x - y for x, y in zip(true_pos, screen_origin_pos)]