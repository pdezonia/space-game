"""
|<--------------------------------------------------------------------------->|
ship.py is meant to clean up the main program by grouping together
all code related to an individual ship. This should make it easier to create
fleets of ships.

by Philip deZonia
last modified: 2017-02-19
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

class Ship(pygame.sprite.Sprite):
    def __init__(self, x_start, y_start):
        """intialize sprites and state variables"""
        pygame.sprite.Sprite.__init__(self) # call sprite initializer
        self.ship_hull = Applecat() # create ship hull sprite currently just the applecat
        
        self.pos = [x_start, y_start] #initialize ship position
        self.heading = 0      # angle of ship       # and a bunch of other shit
        self.vel = 0          # magitude of velocity of ship
        self.omega = 0        # magnitude of angular velocity of ship
        self.delta_v = 0      # velocity change due to thrusters
        self.delta_omega = 0  # angular velocity change due to thrusters
        self.thrust_angle = 0 # angle at time of thrusting
        self.aim_angle = 0    # angle turrets are pointing
        
        # create turret sprites
        self.turret1 = Turret('AC', 1)
        self.turret2 = Turret('AC', 2)
        self.turret3 = Turret('AC', 3)
        self.turret4 = Turret('AC', 4)
        self.turret5 = Turret('AC', 5)
        self.turret6 = Turret('AC', 6)
        self.whole_ship = pygame.sprite.OrderedUpdates((self.ship_hull, \
        self.turret1, self.turret2, self.turret3, self.turret4, self.turret5, self.turret6))
    
    def motion(self, inputs, in_angle):
        """update position of ship and turrets. inputs is a tuple of bools: 
        fwd, bwd, cw, ccw, shift, ctrl, space. aim_angle is where turrets are pointing"""
        # take in aim_angle
        self.aim_angle = in_angle
        
        #use physics module to calculate new postion heading, etc
        state = advance(self.pos, self.vel, self.heading, \
        self.omega, self.thrust_angle, 1, 1, inputs)
        self.pos = state[0]
        self.vel = state[1]
        self.heading = state[2]
        self.omega = state[3]
        self.thrust_angle = state[4]
        
        # update ship position and pose
        self.ship_hull.update_pos(self.pos, self.heading)
        
        # update turret positions and angles
        self.t1pos = self.turret1.move_and_rotate(self.pos, self.heading, self.aim_angle)
        self.t2pos = self.turret2.move_and_rotate(self.pos, self.heading, self.aim_angle)
        self.t3pos = self.turret3.move_and_rotate(self.pos, self.heading, self.aim_angle)
        self.t4pos = self.turret4.move_and_rotate(self.pos, self.heading, self.aim_angle)
        self.t5pos = self.turret5.move_and_rotate(self.pos, self.heading, self.aim_angle)
        self.t6pos = self.turret6.move_and_rotate(self.pos, self.heading, self.aim_angle)
        
    def render(self, game_window, is_firing):
        """Render ship at new position and angle, takes game screen surface object"""
        self.whole_ship.update() # update sprite statuses
        self.whole_ship.draw(game_window)
        if is_firing:
            draw_laser(self.t1pos, self.aim_angle, game_window)
            draw_laser(self.t2pos, self.aim_angle, game_window)
            draw_laser(self.t3pos, self.aim_angle, game_window)
            draw_laser(self.t4pos, self.aim_angle, game_window)
            draw_laser(self.t5pos, self.aim_angle, game_window)
            draw_laser(self.t6pos, self.aim_angle, game_window)
# A
# | Give
# | me
# | space
# V