"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
Spaced Out: The Space Game
by Philip deZonia, started on 2017-02-05 on a rainy day in Verona.
This is the main function that calls all the functions and classes.
Will be used for testing classes in early stages of development.
This is the refactored version of space_game_main.py
"""

import os
import sys
from math import *
import pygame
import ship
import station
import laser_generator # this is an old module from before refactoring
import coordinate_converter as coord_conv
import key_reader

# initialize variables
is_done = False
screen_width = 1200
screen_height = 900

# i don't know what this does
pygame.init()

# create game objects
clock = pygame.time.Clock()
window = pygame.display.set_mode((screen_width, screen_height))
game_font = pygame.font.Font(None, 36)
player_pos = [600, 450]
player_ship = ship.Ship('Applecat', player_pos)
npc_ship = ship.Ship('Applecat', [1000, 600])
station1 = station.Station('Loanne', [600, 1000])


# game loop
while not is_done:
    window.fill((50, 50, 50))
    # go through event queue
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN 
            and event.key == pygame.K_ESCAPE)):
            is_done = True
    inputs = key_reader.get_key_inputs()
    laser_list = []
    # calculate turret angle
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    turr_ang = degrees(atan2(-mouse_y + screen_height/2, 
                       mouse_x - screen_width/2))
    player_pos = player_ship.motion(inputs, turr_ang, window, player_pos)
    npc_ship.motion([0, 0, 0, 0, 0, 0, 0], 0, window, player_pos)
    
    player_ship.render(window)
    npc_ship.render(window)
    station1.render(window)
    if pygame.mouse.get_pressed()[0]: 
        for beam in player_ship.fire_lasers(window, screen_width, screen_height):
            laser_list.append(beam)
            
    player_ship.check_damage(laser_list, window)
    station1.motion(window, player_pos)
    """End of loop work (put it all in a function)"""
    
    npc_ship.check_damage(laser_list, window)
    pygame.display.flip()
    clock.tick(30)