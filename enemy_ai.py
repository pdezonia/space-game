"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
enemy_ai.py is a class definition for the computer controller of
enemy ships. It takes the its own pose and velocity and the postion of
the player, civilian ships, and player allied ships. The AI seeks to
stay close enough to its target to be within vision range, based on
the screen size.
"""

from math import *
import pygame
import cfg


class EnemyAI():
    def __init__(self, difficulty):
        """
        Initialize trailing distance, attack frequency, and aim delay.
        """
        self.target_dist = cfg.screen_height/2
        
        pass