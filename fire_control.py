"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
fire_control.py is a class definition holding functions that make
sure that the turrets do not fire into each other or the ship cockpit.
Doesn't really have to be a class in the current state of the game.
"""

from math import *

class FireControl(object):
    def __init__(self, ship_type):
        """Based on ship type code, load a different set of 
        rules for which angles each gun is allowed to fire.
        """
        if ship_type == 'Applecat':
            