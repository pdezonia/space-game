"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
ship.py is a class definition for all self-propelled vessels in the
game.
This is the refactored version of ship.py
"""

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

    def _initialize_applecat(self):
        self.hull_sprite = applecat_sprite.ApplecatHullSprite()
        self.whole_ship = pygame.sprite.OrderedUpdates(self.hull_sprite)
        self.turret_list = []
        for i in range(6):
            x = applecat_turret.ApplecatTurret(i + 1)
            self.turret_list.append(x)
            self.whole_ship.add(x)

    def motion(self, input_list, turret_angle, player_pos=[0, 0]):
        """Update the position of ship. inputs is a list of flags for
        control inputs, they are: [fwd, bwd, cw, ccw, shift, ctrl,
        and spacebar. Return position so player ship position 
        can be known to other sprites.
        """
        position, velocity, heading, omega, thrust_angle = (
            self.model.calculate_timestep(input_list))
        self.hull_sprite.update_pos(position, heading, player_pos)
        self.t_pos = [] # possibly overly inefficient section
        for i in range(6):
            self.t_pos.append(
                self.turret_list[i].update_pos(position, heading,
                                               turret_angle, player_pos))
        return position
      
    def fire_lasers(self):
        """Broadcast laser beam trajectories by sending out streams of
        points along a lines from each turret."""
        pass
       
    def check_damage(self):
        """Check for laser beams from other ships that overlap manually
        defined bounding box."""
        pass
      
    def render(self, game_window):
        """Render ship at new position and angle"""
        self.whole_ship.draw(game_window)