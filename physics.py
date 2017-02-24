"""
|<--------------------------------------------------------------------------->|
physics.py is a function host for the physics of objects in space.


by Philip deZonia
last modified: 2017-02-16
"""

# import required modules (maybe reduntantly)
import pygame
import os, sys
from math import *

# initialize variables
# is_done = False
# x_pos = 600      # x coord of ship
# y_pos = 450      # y coord of ship
# heading = 0      # angle of ship
# vel = 0          # magitude of velocity of ship
# omega = 0        # magnitude of angular velocity of ship
# time_step = .1   # define time step between frames
# delta_v = 0      # velocity change due to thrusters
# delta_omega = 0  # angular velocity change due to thrusters
# thrust_angle = 0 # angle at time of thrusting

# start modules required by pygame
pygame.init()

def control_test(p_coords, p_vel, p_heading, p_omega, p_thrust_angle, \
                  accel, time_step):
    """Compute ship position and speed in the current frame based on its 
    previous position and speed. p_coords is a pair. heading, p_omega, and 
    thrust angle are in degrees. Returns new coords, vel, heading, angular 
    velocity, and, thrust angle."""
    # initialize local variables
    # return values are set to inputs in case there is no control input
    coords = [0, 0]
    vel = p_vel
    delta_v = 0
    heading = p_heading
    omega = p_omega
    delta_omega = 0
    thrust_angle = p_thrust_angle
    
    # take in user input
    if pygame.key.get_pressed()[pygame.K_w]: 
        delta_v += accel*0.1
        thrust_angle = heading # heading at time of thrusting
    if pygame.key.get_pressed()[pygame.K_s]:
        delta_v -= accel*0.1
        thrust_angle = heading
    if pygame.key.get_pressed()[pygame.K_a]: delta_omega += accel*0.1
    if pygame.key.get_pressed()[pygame.K_d]: delta_omega -= accel*0.1
    # why would you want to go faster??? consider using shift for monoprop
    # if pygame.key.get_pressed()[pygame.K_LSHIFT]:
        # delta_omega *= 2
        # delta_v *= 2 
    if pygame.key.get_pressed()[pygame.K_LCTRL]:
        delta_omega *= 0.5
        delta_v *= 0.5
    
    # turn off thrusters if controls are released, this might be reduntant
    if pygame.key.get_pressed()[pygame.K_w] == False and \
    pygame.key.get_pressed()[pygame.K_s] == False: delta_v = 0
    if pygame.key.get_pressed()[pygame.K_a] == False and \
    pygame.key.get_pressed()[pygame.K_d] == False: delta_omega = 0
    
    # increment velocities
    vel = p_vel + delta_v
    omega = omega + delta_omega
    
    # institute speed limit
    if vel > 5: vel = 5
    if vel < -5: vel = -5
    if omega > 5: omega = 5
    if omega < -5: omega = -5
    
    # halt ship if slow enough
    if abs(vel) < 0.1: vel = 0
    if abs(omega) < 0.1: omega = 0
    
    # engage auto stay with spacebar
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        vel = vel*0.9
        omega = omega*0.9
    
    # calculate ship position and pose
    heading = heading + omega*time_step
    coords[0] = p_coords[0] + vel*time_step*cos(-radians(thrust_angle))
    coords[1] = p_coords[1] + vel*time_step*sin(-radians(thrust_angle))
    
    # return new state
    return coords, vel, heading, omega, thrust_angle

def advance(p_coords, p_vel, p_heading, p_omega, p_thrust_angle, \
                  accel, time_step, control_inputs):
    """Like control_test but also takes control_inputs which is a tuple of bools: 
    fwd, bwd, cw, ccw, shift, ctrl, space"""
    # initialize local variables
    # return values are set to inputs in case there is no control input
    coords = [0, 0]
    vel = p_vel
    delta_v = 0
    heading = p_heading
    omega = p_omega
    delta_omega = 0
    thrust_angle = p_thrust_angle
    
    # take in user input
    if control_inputs[0]: 
        delta_v += accel*0.1
        thrust_angle = heading # heading at time of thrusting
    if control_inputs[1]:
        delta_v -= accel*0.1
        thrust_angle = heading
    if control_inputs[3]: delta_omega += accel*0.1
    if control_inputs[2]: delta_omega -= accel*0.1
    # why would you want to go faster??? consider using shift for monoprop
    # if pygame.key.get_pressed()[pygame.K_LSHIFT]:
        # delta_omega *= 2
        # delta_v *= 2 
    if control_inputs[5]:
        delta_omega *= 0.5
        delta_v *= 0.5
    
    # turn off thrusters if controls are released, this might be reduntant, might be reduntant
    if control_inputs[0] == False and control_inputs[1] == False: delta_v = 0
    if control_inputs[3] == False and control_inputs[2] == False: delta_omega = 0
    
    # increment velocities
    vel = p_vel + delta_v
    omega = omega + delta_omega
    
    # institute speed limit
    if vel > 5: vel = 5
    if vel < -5: vel = -5
    if omega > 5: omega = 5
    if omega < -5: omega = -5
    
    # halt ship if slow enough
    if abs(vel) < 0.1: vel = 0
    if abs(omega) < 0.1: omega = 0
    
    # engage auto stay with spacebar
    if control_inputs[6]:
        vel = vel*0.9
        omega = omega*0.9
    
    # calculate ship position and pose
    heading = heading + omega*time_step
    coords[0] = p_coords[0] + vel*time_step*cos(-radians(thrust_angle))
    coords[1] = p_coords[1] + vel*time_step*sin(-radians(thrust_angle))
    
    # return new state
    return coords, vel, heading, omega, thrust_angle