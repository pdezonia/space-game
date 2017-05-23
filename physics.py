"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
physics.py is a class definition holding functions for the "physics"
engine.
Issues:
This is the refactored version of physics.py.
Candidate for further refactoring: reduce mean function size.
"""

from math import *


class Simulator(object):
    def __init__(self, start_location, mass, rot_inert, motor_thrust):
        """Initialize physical attributes of ship: position, attitude, 
        mass, velocity, and rocket motor thrust. 
        Also set conversion ratios between physical and game 
        measurements.
        """
        # conversions
        self.metres_p_pix = 0.2 # metres/pixel
        self.time_p_step = 0.03 # seconds/timestep aka 30fps
        
        # physical attributes
        self.mass = mass # kg (68000kg is space shuttle)
        self.motor_thrust = motor_thrust # N
        self.rotor_thrust = motor_thrust*50
        self.rot_inert = rot_inert
        
        # state
        self.pos = [start_location[0]*self.metres_p_pix, 
                    start_location[1]*self.metres_p_pix]
        self.heading = 0 # degrees ccw from right
        self.vel = [0, 0] # m/s - magnitude
        self.omega = 0 # degrees/s
        
        
    def calculate_timestep(self, control_inputs):
        """ When shift is pressed, switch to rcs thrusters. Control
        inputs are as follows: forwards, backwards, clockwise,
        counterclockwise, rcs_mode, reduced thrust, and drift canceler.
        """
        lin_accel = self.motor_thrust/self.mass
        rot_accel = self.rotor_thrust/self.rot_inert
        
        # velocity controls
        delta_v = lin_accel*self.time_p_step
        if control_inputs[0]:
            self.vel[0] += delta_v*cos(-radians(self.heading))
            self.vel[1] += delta_v*sin(-radians(self.heading))
        if control_inputs[1]:
            self.vel[0] -= delta_v*cos(-radians(self.heading))
            self.vel[1] -= delta_v*sin(-radians(self.heading))
        
        # rotation controls
        delta_omega = rot_accel*self.time_p_step
        if control_inputs[2]: self.omega -= delta_omega
        if control_inputs[3]: self.omega += delta_omega
        
        # put rcs code here
        
        # put thrust adjuster code here
        
        # drift canceler
        if control_inputs[6]:
            self.vel = [x*0.9 for x in self.vel]
            self.omega = self.omega*0.9
        
        # position updates
        displacement = [x*self.time_p_step for x in self.vel]
        self.pos = [x + y for x, y in zip(self.pos, displacement)]
        self.heading += self.omega
        
        # convert position to pixels
        pix_pos = [x/self.metres_p_pix for x in self.pos]
        
        return pix_pos, self.heading
        
        