"""
|<--------------------------------------------------------------------------->|
ship.py is meant to clean up the main program by grouping together
all code related to an individual ship. This should make it easier to create
fleets of ships.

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

class Ship(pygame.sprite.Sprite):
    def __init__(self, x_start, y_start):
        """intialize sprites and state variables"""
        pygame.sprite.Sprite.__init__(self) # call sprite initializer
        self.ship_hull = Applecat() # create ship hull sprite currently just the applecat
        
        self.health_points = 30     # initialize ship health
        
        self.pos = [x_start, y_start] #initialize ship position
        self.heading = 0      # angle of ship       # and a bunch of other shit
        self.vel = 0          # magitude of velocity of ship
        self.omega = 0        # magnitude of angular velocity of ship
        self.delta_v = 0      # velocity change due to thrusters
        self.delta_omega = 0  # angular velocity change due to thrusters
        self.thrust_angle = 0 # angle at time of thrusting
        self.aim_angle = 0    # angle turrets are pointing
        
        # create turret sprites
        self.turrets = []
        for i in range(6):
            self.turrets.append(Turret('AC', i + 1))
        
        # create ship sprite group
        self.whole_ship = pygame.sprite.OrderedUpdates(self.ship_hull, \
        self.turrets[0], self.turrets[1], self.turrets[2], \
        self.turrets[3], self.turrets[4], self.turrets[5])
        
        self.ship_laser_beams = pygame.sprite.OrderedUpdates()
    
    def motion(self, inputs, in_angle, player_pos = [0, 0]):
        """update position of ship and turrets. inputs is a tuple of bools: 
        fwd, bwd, cw, ccw, shift, ctrl, space. aim_angle is where turrets are
        pointing, last argument is position of camera center in world coords"""
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
        self.ship_hull.update_pos(self.pos, self.heading, player_pos)
        
        # don't know why I didn't just do this instead of modifying every function
        # adjust turret position to move by ship
        turret_pos = [self.pos[0] - player_pos[0], self.pos[1] - player_pos[1]]
        
        # update turret positions and angles
        self.t_pos = []
        for i in range(6):
            self.t_pos.append(self.turrets[i].move_and_rotate(turret_pos, self.heading, self.aim_angle))
        
        return self.pos
        
        # add player ship position for offseting
    def render(self, game_window, is_firing):
        """Render ship at new position and angle, takes game screen surface object"""
        self.whole_ship.update() # update sprite statuses
        self.whole_ship.draw(game_window)
        if is_firing:
            # for i in range(6):
                # draw_laser(self.t_pos[i], self.aim_angle, game_window)
            self.shoot(game_window)
        if not is_firing:
            self.ship_laser_beams.empty()
    
    def shoot(self, game_window):
        if not bool(self.ship_laser_beams):
            self.beam_group = []
            for i in range(6):
                self.beam_group.append(LaserBeam())
                self.beam_group[i].place_laser(self.t_pos[i], self.aim_angle)
        
            self.ship_laser_beams.add(self.beam_group)
            self.ship_laser_beams.update()
            self.ship_laser_beams.draw(game_window)
    
    def take_damage(self):
        self.health_points -= 1
# A
# | Give
# | me
# | space
# V