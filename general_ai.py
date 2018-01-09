"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
general_ai.py is a class definition for the computer controller of
npc ships. A base class which establishes point to point navigation.
"""

from math import *
import pygame
import cfg


class GeneralAI():
    def __init__(self):
        """Declare commands."""
        # This must match what key_reader.py says
        self.fwd_cmd = [1, 0, 0, 0, 0, 0, 0]
        self.bwd_cmd = [0, 1, 0, 0, 0, 0, 0]
        self.rgt_cmd = [0, 0, 1, 0, 0, 0, 0]
        self.lft_cmd = [0, 0, 0, 1, 0, 0, 0]
        self.slo_cmd = [0, 0, 0, 0, 0, 0, 1]
        self.full_cmd = []
        self.cmd_num = -1 # cmd_num tracks progress on task
        self.last_cmd_num = 1
        # Call type initialize which gets overwritten
        self._type_init()
    
    def _type_init(self)
        """Specific information meant to be overwritten."""
        self.ship_accel = 14.7058823529 # m/s^2
        self.ship_ang_accel = degrees(3.77719590495) # deg/s
    
    def go_to_point(self, current_heading, current_pos, target_pos):
        """
        Must be called every timestep so long as ship is in
        motion. Flow of this program is accept target, point to
        target, move to target, and repeat.
        """
        out_cmd = [0, 0, 0, 0, 0, 0, 0]
        if self.cmd_num < 0:
            # AI just completed a task and is ready for new one
            align_cmd = align_ship(current_heading, current_pos, target_pos)
            go_cmd = line_travel(current_pos, target_pos)\
            # Add frame count of alignment phase to elements of travel phase
            for line in go_cmd:
                line[0] += align_cmd[-1][0]
            self.full_cmd = align_cmd + go_cmd
            self.last_cmd_num = self.full_cmd[-1][0]
        elif self.cmd_num <= self.last_cmd_num:
            # Check if this^ should be just a <
            for cmd_line in self.full_cmd:
                if cmd_line[0] > self.cmd_num:
                    out_cmd = cmd_line[1]
                    break
        else
            # Reached end of command sequence, revert
            self.last_cmd_num = -1
    
    def align_ship(self, current_heading, point_a, point_b):
        """Align ship to point towards target."""
        desired_heading = degrees(atan2(point_b[1] - point_a[1],
                                        point_b[0] - point_a[0]))
        # Convert desired heading to be b/w 0 and 360 degrees
        if (desired_heading < 0): desired_heading += 360
        angle_diff = desired_heading - current_heading
        # Times are converted to frames
        frames_to_midpoint = sqrt(angle_diff/self.ship_ang_accel)*cfg.frame_rate
        frames_to_target = 2*frames_to_midpoint
        if angle_diff < 0:
            out_command = [[frames_to_midpoint, self.lft_cmd],
                           [frames_to_target,   self.rgt_cmd]]
        else:
            out_command = [[frames_to_midpoint, self.rgt_cmd],
                           [frames_to_target,   self.lft_cmd]]
        
    def line_travel(self, point_a, point_b):
        """
        Travel from point A to point B using a triangular
        trajectory assumes zero initial velocity and alignment with
        target. 
        """
        delta_x = point_b[0] - point_a[0]
        delta_y = point_b[1] - point_a[1]
        target_dist = sqrt(delta_x^2 + delta_y^2)
        # Times are converted to frames
        frames_to_midpoint = sqrt(target_dist/self.ship_accel)*cfg.frame_rate
        frames_to_target = 2*frames_to_midpoint
        return [[frames_to_midpoint, self.fwd_cmd],
                [frames_to_target,   self.bwd_cmd]]