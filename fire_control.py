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
        set for each turret.
        """
        self.clear_angles = []
        if ship_type == 'Applecat':
            self.clear_angles.append([[0, 122], [238, 360]])
            self.clear_angles.append([[0, 165], [285, 305], [335, 360]])
            self.clear_angles.append([[15, 200], [235, 255]])
            self.clear_angles.append([[50, 310]])
            self.clear_angles.append([[105, 125], [160, 345]])
            self.clear_angles.append([[0, 25], [55, 75], [195, 360]])
    
    def check_lineoffire(self, turret_angle_list, ship_heading):
        """Given a list of turret angles, and already knowing the ship
        type, returns a copy of the list with the angles replaced by a
        true value indicating when the turret is clear to fire and a 
        false when it is not. Expects turret angles between -180 and
        180 degrees and ship angles to merely be expressed in degrees.
        """
        if len(turret_angle_list) != len(self.clear_angles):
            print("Error: incorrect number of turrets")
            return
        is_clear2fire = []
        # Keep ship angle b/w 0 and 360
        # ship_heading = ship_heading % 360
        for turret_index in range(len(turret_angle_list)):
            # print 'Turret number: ', turret_index
            # Compensate for ship heading
            turret_angle = turret_angle_list[turret_index] - ship_heading
            # This converts turret angle to an angle b/w 0 and 360
            turret_angle = turret_angle % 360
            is_clear = False
            # Check 
            for angle_set in self.clear_angles[turret_index]:
                # print angle_set[0], ', ', angle_set[1]
                print(turret_angle)
                if (turret_angle >= angle_set[0] 
                    and turret_angle < angle_set[1]):
                    is_clear = True
            is_clear2fire.append(is_clear)
        return is_clear2fire
        
        