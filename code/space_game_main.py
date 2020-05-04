"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
Spaced Out: The Space Game
by Philip deZonia, started on 2017-02-05 on a rainy day in Verona.
This is the main function that calls all the functions and classes.
Will be used for testing classes in early stages of development.
This is the refactored version of space_game_main.py

TODO: 
Turn off / destroy ship ai when ship dies
"""

import os
import sys
import time
from math import *
import pygame
import cfg
import ship
import station
import laser_generator # this is an old module from before refactoring
import coordinate_converter as coord_conv
import key_reader
import general_ai

# initialize variables
is_done = False

# Initialize pygame
pygame.init()
# Load in fonts
if not pygame.font:
    print("Warning: fonts not loaded")

# create game objects
clock = pygame.time.Clock()
window = pygame.display.set_mode((cfg.screen_width, cfg.screen_height))
background = pygame.Surface(window.get_size())
background = background.convert() # Done to improve performance while blitting
background.fill((50, 50, 50))
hud_text_surf = pygame.Surface((window.get_width(), 100))
hud_text_origin = (0, window.get_height() - 100)
#hud_text_surf.set_alpha(128) # 0 means completely transparent
hud_text_surf = hud_text_surf.convert()

if pygame.font:
    game_font = pygame.font.Font(None, 36)
    # Testing text drawing
    text = game_font.render("Testing ...", 1, (255, 255, 255))
    text_pos = text.get_rect(centerx=background.get_width()/2)
    background.blit(text, text_pos)

player_pos = [600, 450]
player_ship = ship.Ship('Applecat', player_pos)
npc_pos = [1000, 600]
npc_heading = 0
npc_ship = ship.Ship('Applecat', npc_pos)
npc_control = general_ai.GeneralAI()
station1 = station.Station('Loanne', [600, 1000])

frame_start_time = time.time()
last_fps_msg_time = time.time()
fps_msg = '0'

# game loop
while not is_done:
    #window.fill((50, 50, 50))
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
    turr_ang = degrees(atan2(-mouse_y + cfg.screen_height/2, 
                       mouse_x - cfg.screen_width/2))
    player_pos = player_ship.motion(inputs, turr_ang, window, player_pos)
    this_cmd = npc_control.go_to_point(npc_heading, npc_pos, [600, 1000])
    # print this_cmd
    npc_pos = npc_ship.motion(this_cmd, 0, window, player_pos)
    npc_heading = npc_ship.get_heading()
    #print(npc_pos, npc_heading)
    
    # Drawing phase
    window.blit(background, (0, 0))
    # Make it so that all sprites are drawn by RenderPlain
    station1.render(window)
    player_ship.render(window)
    npc_ship.render(window)
    if pygame.mouse.get_pressed()[0]: 
        for beam in player_ship.fire_lasers(window):
            laser_list.append(beam)
    
    # Testing realtime text updates
    coord_msg = str(round(player_pos[0])) + ", " + str(round(player_pos[1]))
    coord_text = game_font.render(coord_msg, 1, (0, 255, 0))
    coord_text_pos = coord_text.get_rect(centerx = cfg.screen_width/2 -100)

    frame_end_time = time.time()
    frame_duration =  frame_end_time - frame_start_time
    frame_rate = 1/frame_duration
    frame_start_time = frame_end_time
    if time.time() - last_fps_msg_time >= 1:
        fps_msg = 'FPS: ' + str(round(frame_rate))
        last_fps_msg_time = time.time()
    fps_text = game_font.render(fps_msg, 1, (255, 255, 255))
    fps_text_pos = fps_text.get_rect(centerx = cfg.screen_width - 200)
    hud_text_surf.fill((0, 0, 0))
    hud_text_surf.blit(coord_text, coord_text_pos)
    hud_text_surf.blit(fps_text, fps_text_pos)
    window.blit(hud_text_surf, hud_text_origin)

    player_ship.check_damage(laser_list, window)
    station1.motion(window, player_pos)


    """End of loop work (put it all in a function)"""
    npc_ship.check_damage(laser_list, window)
    pygame.display.flip()
    clock.tick(cfg.frame_rate)