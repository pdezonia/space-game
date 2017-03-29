"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
station.py is a class definition for all space stations in the game.
This is the refactored version of station.py
"""

import station_sprite


class Station(object):
    def __init__(self, station_type, starting_pos):
        self.health_points = 100
        if station_type == 'Loanne':
            self._initialize_loanne()
            
    def _initialize_loanne():
        pass