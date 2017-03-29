"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
station_sprite.py is a class definition for sprites for either half of 
the very large space station. It is overridden to accomodate different
space station images, the defualt sprite is the same as the Loanne.
This is the refactored version of station_sprite.py.
"""

import enhanced_sprite


class SpaceStationSprite(enhanced_sprite.EnhancedSprite):
    def __init__(self, side_id):
        """Loads different sprite depending on which half was
        requested. side_id is a character ('L' or 'R') specifying
        which half.
        """
        self.side_id = side_id
        pygame.sprite.Sprite.__init__(self)
        if self.side_id == 'L':
            self.image, self.rect = self.load_image(
                'station left half large.png')
        else:
            self.image, self.rect = self.load_image(
                'station right half large.png')
        self.original_image = self.image
    
    def update_pos(self, position, player_pos=[0, 0]):
        """Place the image on the left or right side of the given
        point depending on which half it is. Modifies right or 
        left and centery.
        """
        if self.side_id == 'L':
            self.rect.right = position[0] - player_pos[0]
        else:
            self.rect.left = position[0] - player_pos[0]
        self.rect.centery = position[1]