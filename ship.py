"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
ship.py is a class definition for all self-propelled vessels in the
game.
This is the refactored version of ship.py
"""

from math import *
import pygame
import physics
import applecat_sprite
import applecat_turret
import laser_generator
import fire_control


class Ship(object):
    def __init__(self, ship_type, starting_pos):
        """Initialize health, physics state, ship sprite and turret
        type, and also handle dealing and receiving damage.
        """
        self.health_points = 30
        if ship_type == 'Applecat':
            self._initialize_applecat()
        start_location = starting_pos
        self.model = physics.Simulator(
            start_location, 68000, 13237333, 1000000)
        self.turret_angle = 0
        self.heading = 0 # used by fire control to get relative angle
        # we will use this to pass the player position to fire_lasers
        # so it can draw the lasers on its own
        self.player_pos = [0, 0]

    def _initialize_applecat(self):
        """Load stats and models applicable to the Applecat ship."""
        self.hull_sprite = applecat_sprite.ApplecatHullSprite()
        self.whole_ship = pygame.sprite.OrderedUpdates(self.hull_sprite)
        self.turret_list = []
        for i in range(6):
            x = applecat_turret.ApplecatTurret(i + 1)
            self.turret_list.append(x)
            self.whole_ship.add(x)
        self.obst_check = fire_control.FireControl("Applecat")
        self.laser_range = 10000

    def motion(self, input_list, turret_angle, game_window, player_pos=[0, 0]):
        """Update the position of ship. inputs is a list of flags for
        control inputs, they are: [fwd, bwd, cw, ccw, shift, ctrl,
        and spacebar]. Return position the player ship position 
        can be known to other sprites in the event that this ship is 
        the player ship and it needs to broadcast its position to all
        other objects. Turret angle is in degrees.
        """
        self.player_pos = player_pos
        position, heading, = (self.model.calculate_timestep(input_list))
        if heading == 0: 
            sign_factor = 1
        else:
            sign_factor = heading/abs(heading)
        # for fire control function
        self.heading = abs(heading)%360*sign_factor 
        self.hull_sprite.update_pos(position, heading, 
                                    game_window, player_pos)
        self.t_positions = [] # possibly overly inefficient section
        for i in range(6):
            self.t_positions.append(
                self.turret_list[i].update_pos(
                    position, heading, turret_angle, game_window, player_pos))
        self.turret_angle = turret_angle
        return position
      
    def fire_lasers(self, game_window, screen_width, screen_height):
        """Returns laser beam trajectories by returning the length of
        the beam, the angle (in degrees), and its point of origin for
        each beam from each turret.
        """
        """Loop through turrets, only appending beams to empy list
        when obstruction detector says it's okay
        """
        turret_angle_list = [self.turret_angle]*6
        # subtract heading to get relative angle of turret to ship
        are_turrets_clear2fire = self.obst_check.check_blockage(
                                         turret_angle_list, self.heading)
        beam_list = []
        for turret_index in range(6):
            if are_turrets_clear2fire[turret_index]:
                beam_list.append([self.laser_range, 
                                  turret_angle_list[turret_index],
                                  self.t_positions[turret_index]])
        # beam_list = [[10000, self.turret_angle, self.t_positions[0]],
                     # [10000, self.turret_angle, self.t_positions[1]],
                     # [10000, self.turret_angle, self.t_positions[2]],
                     # [10000, self.turret_angle, self.t_positions[3]],
                     # [10000, self.turret_angle, self.t_positions[4]],
                     # [10000, self.turret_angle, self.t_positions[5]]]
        """Draw each beam taking into account offset between game
        coordinates and screen coordinates.
        """
        for beam in beam_list:
            screen_offset = [x - y for x, y in zip(self.player_pos, 
                                [screen_width/2, screen_height/2])]
            laser_origin = [x - y for x, y in zip(beam[2], screen_offset)]
            #print(laser_origin)
            laser_generator.draw_laser(laser_origin, beam[1], game_window)
        return beam_list
       
    def check_damage(self, beam_list, game_window):
        """Check for laser beams from other ships that overlap manually
        defined bounding box. Need to filter out beams from own ship.
        """
        filtered_beam_list = self._filter_beam_list(beam_list)
        damage = self.hull_sprite.overlap_detector(
        filtered_beam_list, game_window)
        self.health_points -= damage
        if self.health_points <= 0:
            self.hull_sprite.kill()
            for i in range(6):
                self.turret_list[i].kill()
    
    def _filter_beam_list(self, raw_beams):
        filtered_beams = []
        for beam in raw_beams:
            # currently testing with just one turret
            if not self._check_inclusion(beam[2], self.t_positions):
                filtered_beams.append(beam)
        return filtered_beams
    
    def _check_inclusion(self, point_a, turret_muzzles):
        """Check if point A is one of the points in point set."""
        match_exists = False
        for point_b in turret_muzzles:
            if point_a == point_b:
                match_exists = True
        return match_exists
    
    def render(self, game_window):
        """Render ship at new position and angle"""
        self.whole_ship.draw(game_window)