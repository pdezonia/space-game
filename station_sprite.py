"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
station_sprite.py is a class definition for sprites for either half of 
the very large space station. It is overridden to accomodate different
space station images, the defualt sprite is the same as the Loanne.
This is the refactored version of station_sprite.py.
"""

import enhanced_sprite
import coordinate_converter as coord_conv


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
                'station left half large.png', -1)
        else:
            self.image, self.rect = self.load_image(
                'station right half large.png', -1)
        self.original_image = self.image
    
    def update_pos(self, position, game_window, player_pos=[0, 0]):
        """Place the image on the left or right side of the given
        point depending on which half it is. Modifies right or 
        left and centery.
        """
        screen_pos = coord_conv.det_screen_coords(position, player_pos, 
                                                  game_window)
        if self.side_id == 'L':
            self.rect.right = screen_pos[0]
        else:
            self.rect.left = screen_pos[0]
        self.rect.centery = screen_pos[1]