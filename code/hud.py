"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
hud.py is a class definition for displaying the instrument panel
and useful information.
"""

from math inport *
import pygame
import cfg


class HUD(object):
    def __init__(self):
        """Initialize heads up display sprite, color palete"""
        self.pos = [0, 0]
        self.heading = 0

    def update(self, ship_obj):
        """Update data displayed by hud"""
        self.pos = ship_obj.player_pos
        self.heading = ship_obj.heading
        _display_pose()

    def _display_pose(self):
        pass