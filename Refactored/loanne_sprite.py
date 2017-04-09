"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
loanne_sprite.py is a class definition for sprites for either half of 
the Loanne space station.
"""

import pygame
import station_sprite


class LoanneSprite(station_sprite.SpaceStationSprite):
    def __init__(self, side_id):
        """Loads different sprite depending on which half was
        requested. side_id is a character ('L' or 'R') specifying
        which half.
        """
        self.side_id = side_id
        pygame.sprite.Sprite.__init__(self)
        if self.side_id == 'L':
            self.image, self.rect = self.load_image(
                'station left half large.png', -1)
        else:
            self.image, self.rect = self.load_image(
                'station right half large.png', -1)
        self.original_image = self.image