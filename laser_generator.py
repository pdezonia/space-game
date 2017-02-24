"""
|<--------------------------------------------------------------------------->|
laser_generator.py is a module for rendering laser beams given turret position
and angle.


by Philip deZonia
last modified: 2017-02-16
"""

# import required modules (maybe reduntantly)
import pygame
import os, sys
from math import *

# start modules required by pygame
pygame.init()

def draw_laser(origin_point, angle, screen_object):
    """ draw a thin rectangle from the point of origin and that is 
    long enougth to go off the screen. Origin point is where the
    on-screen end of the laser should be given as pixel coordinates
    and angle is expressed in degrees, ccw is positive, and starts 
    pointing to the right. screen_object is the the main window."""
    # create local (global?) variables
    end_point = [0, 0]    
    # calculate end point
    end_point[0] = origin_point[0] + 1500*cos(-radians(angle))
    end_point[1] = origin_point[1] + 1500*sin(-radians(angle))
    # draw beam
    pygame.draw.line(screen_object, (25, 255, 25), origin_point, end_point, 2)
    