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
        """Based on ship type code, load a different set of rules for
        which angles each gun is allowed to fire. There is one range
        set for each turret 
        """
        self.clear_angles = []
        if ship_type == 'Applecat':
            self.clear_angles.append([[0, 122], [238, 359]])
            self.clear_angles.append([[0, 165], [285, 305], [335, 359]])
            self.clear_angles.append([[15, 200], [235, 255]])
            self.clear_angles.append([[50, 310]])
            self.clear_angles.append([[105, 125], [200, 245]])
            self.clear_angles.append([[0, 25], [55, 75], [195, 359]])
    
    def check_blockage(self, turret_angle_list):
        """Given a list of turret angles, and already knowing the ship
        type, returns a copy of the list with the angles replaced by a
        true value indicating when the turret is blocked and a false
        when it is not.
        """
        if len(turret_angle_list) != len(self.clear_angles):
            print("Error: incorrect number of turrets")
            return
        is_blocked = []
        for turret_index in range(len(turret_angle_list)):
            turret_angle = turret_angle_list[turret_index]
            is_clear = False
            for angle_set in self.clear_angles[turret_index]:
                print angle_set[0], ', ', angle_set[1]
                print(turret_angle)
                if (turret_angle >= angle_set[0] 
                    and turret_angle <= angle_set[1]):
                    is_clear = True
            is_blocked.append(not is_clear)
        return is_blocked
        
        