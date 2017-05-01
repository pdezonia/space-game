"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
applecat_sprite.py is a class definition for the Applecat spaceship.
This is also the starting point for the campaign to spell Applecat
without a space and with only one uppercase letter.
This is the refactored version of apple_cat_sprite.py.
"""

import pygame
import enhanced_sprite


class ApplecatHullSprite(enhanced_sprite.EnhancedSprite):
    def __init__(self):
        """Change default sprite to the Applecat's hull."""
        self.dot_spacing = 10
        self._create_sprite_image('apple_cat small3.png')
        self._create_hitboxes()
        
    def _create_hitboxes(self):
        """For each turret, there is one 3-tuple of numbers which
        represent x offset, y offset, and radius. X and y offsets are
        to be used in the ship-local coordinate system.
        """
        self.hitbox_offsets_and_radii = [[0, 0, 50],
                                         [-20, 0, 50], [20, 0, 50]]