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
        """Change defualt sprite to the Applecat's hull."""
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = self.load_image('apple_cat small3.png')
        self.original_image = self.image