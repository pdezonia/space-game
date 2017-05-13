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


class Ship(object):
    def __init__(self, ship_type, starting_pos):
        """Initialize health, physics state, ship sprite and turret
        type, and also handle dealing and receiving damage.
        """
        self.health_points = 30
        if ship_type == 'Applecat':
            self._initialize_applecat()
        start_location = starting_pos
        self.model = physics.Simulator(start_location)
        self.turret_angle = 0

    def _initialize_applecat(self):
        self.hull_sprite = applecat_sprite.ApplecatHullSprite()
        self.whole_ship = pygame.sprite.OrderedUpdates(self.hull_sprite)
        self.turret_list = []
        for i in range(6):
            x = applecat_turret.ApplecatTurret(i + 1)
            self.turret_list.append(x)
            self.whole_ship.add(x)

    def motion(self, input_list, turret_angle, game_window, player_pos=[0, 0]):
        """Update the position of ship. inputs is a list of flags for
        control inputs, they are: [fwd, bwd, cw, ccw, shift, ctrl,
        and spacebar. Return position so player ship position 
        can be known to other sprites. Turret angle is in degrees.
        """
        position, velocity, heading, omega, thrust_angle = (
            self.model.calculate_timestep(input_list))
        self.hull_sprite.update_pos(position, heading, 
                                    game_window, player_pos)
        self.t_positions = [] # possibly overly inefficient section
        for i in range(6):
            self.t_positions.append(
                self.turret_list[i].update_pos(
                    position, heading, turret_angle, game_window, player_pos))
        self.turret_angle = turret_angle
        return position
      
    def fire_lasers(self):
        """Returns laser beam trajectories by returning the length of
        the beam, the angle (in degrees), and its point of origin for
        each beam from each turret.
        """
        # currently testing with just one turret
        return [[10000, self.turret_angle, self.t_positions[0]]]
       
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