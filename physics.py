"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
physics.py is a class definition holding functions for the "physics"
engine.
Issues:
    physics are inaccurate, ship immediately changes direction on 
    new thrust input; monoprop motion has no velocity
    might want to switch to cartesian system
This is the refactored version of physics.py.
Candidate for further refactoring: reduce mean function size.
"""

from math import *


class Simulator(object):
    def __init__(self, start_location):
        self.position = start_location
        self.vel = 0
        self.delta_v = 0
        self.heading = 0
        self.omega = 0
        self.delta_omega = 0
        self.thrust_angle = 0
        self.accel = 0.2
        self.time_step = 1
        
    def calculate_timestep(self, control_inputs):
        """ When shift is pressed, switch to rcs thrusters. Control
        inputs are as follows: forwards, backwards, clockwise,
        counterclockwise, rcs_mode, reduced thrust, and drift canceler.
        """
        rcs_disp = [0, 0]
        if control_inputs[4]:
            if control_inputs[0]: rcs_disp[0] += 1
            if control_inputs[1]: rcs_disp[0] -= 1
            if control_inputs[2]: rcs_disp[1] += 1
            if control_inputs[3]: rcs_disp[1] -= 1
        else:
            if control_inputs[0]:
                self.delta_v += self.accel*0.1
                self.thrust_angle = self.heading
            if control_inputs[1]:
                self.delta_v -= self.accel*0.1
                self.thrust_angle = self.heading
            if control_inputs[3]: self.delta_omega += self.accel*0.1
            if control_inputs[2]: self.delta_omega -= self.accel*0.1
        if control_inputs[5]:
            self.delta_omega *= 0.5
            self.delta_v *= 0.5
        if control_inputs[0] == False and control_inputs[1] == False:
            self.delta_v = 0
        if control_inputs[3] == False and control_inputs[2] == False:
            self.delta_omega = 0
        
        self.vel += self.delta_v
        self.omega += self.delta_omega
        if self.vel > 5: self.vel = 5
        if self.vel < -5: self.vel = -5
        if self.omega > 5: self.omega = 5
        if self.omega < -5: self.omega = -5
        if abs(self.vel) < 0.1: self.vel = 0
        if abs(self.omega) < 0.1: self.omega = 0
        if control_inputs[6]:
            self.vel = self.vel*0.9
            self.omega = self.omega*0.9
        self.heading += self.omega*self.time_step
        self.position[0] += (
            self.vel*self.time_step*cos(-radians(self.thrust_angle))
            + rcs_disp[0]*cos(-radians(self.heading))
            - rcs_disp[1]*sin(-radians(self.heading)))
        self.position[1] += (
            self.vel*self.time_step*sin(-radians(self.thrust_angle))
            + rcs_disp[0]*sin(-radians(self.heading))
            -rcs_disp[1]*cos(-radians(self.heading)))
        return self.position, self.vel, self.heading, self.omega, self.thrust_angle