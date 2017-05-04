"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
station.py is a class definition for all space stations in the game.
This is the refactored version of station.py
"""

import pygame
import loanne_sprite


class Station(object):
    def __init__(self, station_type, starting_pos):
        """choose station type and initialize health points"""
        self.health_points = 100
        self.position = starting_pos
        if station_type == 'Loanne':
            self._initialize_loanne()
            
    def _initialize_loanne(self):
        """load both halves"""
        self.left_half = loanne_sprite.LoanneSprite('L')
        self.right_half = loanne_sprite.LoanneSprite('R')
        self.whole_station = pygame.sprite.OrderedUpdates(self.left_half, 
                                                          self.right_half)
    
    def motion(self, player_pos=[0, 0]):
        """the station isn't actually moving but its position on the screen
        has to change relative to the player."""
        self.left_half.update_pos(self.position, player_pos)
        self.right_half.update_pos(self.position, player_pos)
    
    def render(self, game_window):
        """render station at relative position,
        takes game screen object"""
        self.whole_station.draw(game_window)