"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
applecat_sprite.py is a class definition for the Applecat spaceship.
This is also the starting point for the campaign to spell Applecat
without a space and with only one uppercase letter.

The Applecat is around 44m long, 20m wide, has a mass of 68000kg, 
moment of inertia of 13237333 kg*m^2, and effective thrust of 1000N(?).

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
        self.hitbox_offsets_and_radii = [[0, 0, 65],
                                         [-50, 0, 65], [60, 0, 65]]
    
    def switch_to_neutral_sprite(self):
        self._update_sprite_image('apple_cat small3.png')
    
    def switch_to_fwd_sprite(self):
        self._update_sprite_image('apple_cat small3 fwd.png')
        
    def switch_to_bwd_sprite(self):
        self._update_sprite_image('apple_cat small3 bwd.png')
        
    def switch_to_ccw_sprite(self):
        self._update_sprite_image('apple_cat small3 ccw.png')
        
    def switch_to_cw_sprite(self):
        self._update_sprite_image('apple_cat small3 cw.png')