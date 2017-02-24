"""
|<--------------------------------------------------------------------------->|
Spaced Out: The Space Game
by Philip deZonia, started on 2017-02-05 on a rainy day in Verona.

This is the main function that calls all the functions and classes.
Will be used for testing classes in early stages of development.
"""

# import required modules (maybe reduntantly)
import pygame
import os, sys
from math import *

# import custom made modules
from apple_cat_sprite import *
from turret import *
from physics import *
from laser_generator import *
import ship

# start modules required by pygame
pygame.init()

# create clock timer to limit frame rate
clock = pygame.time.Clock()

# create game window
window = pygame.display.set_mode((1200, 900))

# initialize variables
is_done = False
x_pos = 600      # x coord of ship
y_pos = 450      # y coord of ship
heading = 0      # angle of ship
vel = 0          # magitude of velocity of ship
omega = 0        # magnitude of angular velocity of ship
time_step = .1   # define time step between frames
delta_v = 0      # velocity change due to thrusters
delta_omega = 0  # angular velocity change due to thrusters
thrust_angle = 0 # angle at time of thrusting

# get fonts ready, i guess?
ourFont = pygame.font.Font(None, 36)

# create objects
da_ship = Applecat()
da_shipTest = ship.Ship(700, 500)
second_ship = ship.Ship(800, 600)

second_ship.motion([1, 0, 0, 1, 0, 0, 0], 90)

turret1 = Turret('AC', 1)
turret2 = Turret('AC', 2)
turret3 = Turret('AC', 3)
turret4 = Turret('AC', 4)
turret5 = Turret('AC', 5)
turret6 = Turret('AC', 6)

allsprites = pygame.sprite.OrderedUpdates((da_ship, \
turret1, turret2, turret3, turret4, turret5, turret6))

# testing
_image_library = {} # it's an empty set?
# initialize picture manager function thing
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canon_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canon_path)
        _image_library[path] = image
    return image

# keep game running
while not is_done:
    
    # go through event cue
    for event in pygame.event.get(): 
        # check if user exited window or pressed escape
        if event.type == pygame.QUIT or \
        (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            is_done = True
    
    # reset inputs array
    inputs = [0, 0, 0, 0, 0, 0, 0] # w, s, d, a, shift, ctrl, space
    # take in user input
    if pygame.key.get_pressed()[pygame.K_w]: inputs[0] = 1
    if pygame.key.get_pressed()[pygame.K_s]: inputs[1] = 1
    if pygame.key.get_pressed()[pygame.K_a]: inputs[3] = 1
    if pygame.key.get_pressed()[pygame.K_d]: inputs[2] = 1
    # why would you want to go faster??? consider using shift for monoprop
    # if pygame.key.get_pressed()[pygame.K_LSHIFT]:
        # delta_omega *= 2
        # delta_v *= 2 
    if pygame.key.get_pressed()[pygame.K_LCTRL]: inputs[5] = 1
    if pygame.key.get_pressed()[pygame.K_SPACE]: inputs[6] = 1
    
    phys_output = control_test((x_pos, y_pos), vel, heading, \
    omega, thrust_angle, 1, 1)
    
    x_pos = phys_output[0][0]
    y_pos = phys_output[0][1]
    vel = phys_output[1]
    heading = phys_output[2]
    omega = phys_output[3]
    thrust_angle = phys_output[4]
    
    # update ship position and pose
    da_ship.update_pos([x_pos, y_pos], heading)
    
    # calculate turret angle
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    turr_ang = math.degrees(atan2(- mouse_y + da_shipTest.pos[1], mouse_x - da_shipTest.pos[0]))

    # calculate turret position and pose
    t1pos = turret1.move_and_rotate([x_pos, y_pos], heading, turr_ang)
    t2pos = turret2.move_and_rotate([x_pos, y_pos], heading, turr_ang)
    t3pos = turret3.move_and_rotate([x_pos, y_pos], heading, turr_ang)
    t4pos = turret4.move_and_rotate([x_pos, y_pos], heading, turr_ang)
    t5pos = turret5.move_and_rotate([x_pos, y_pos], heading, turr_ang)
    t6pos = turret6.move_and_rotate([x_pos, y_pos], heading, turr_ang)
    
    # load crosshairs
    crosshairs = get_image('crosshairs1.png')
    # get center offset
    xc = crosshairs.get_size()[0]/2
    yc = crosshairs.get_size()[1]/2
    # print inputs
    da_shipTest.motion(inputs, turr_ang)
    # tell npc ship to move
    second_ship.motion([1, 0, 1, 0, 0, 0, 0], 90)
    
    """ end of loop work """
    # update sprite statuses
    #allsprites.update()
    
    # redraw screen to clear up previous iterations of the square
    window.fill((50, 50, 50)) # grey background

    # testing
    # window.blit(get_image('station right half large.png'), (30, 30))
    
    # draw all sprites
    #allsprites.draw(window)
    da_shipTest.render(window, pygame.mouse.get_pressed()[0])
    # draw npc ship
    second_ship.render(window, 0)
    
    #if firing, render lasers
    # if pygame.mouse.get_pressed()[0]:
        # draw_laser(t1pos, turr_ang, window)
        # draw_laser(t2pos, turr_ang, window)
        # draw_laser(t3pos, turr_ang, window)
        # draw_laser(t4pos, turr_ang, window)
        # draw_laser(t5pos, turr_ang, window)
        # draw_laser(t6pos, turr_ang, window)
        
    # change mouse to crosshairs
    pygame.mouse.set_visible(0)
    
    # draw crosshairs
    window.blit(crosshairs, (mouse_x - xc, mouse_y - yc))

    # update game window
    pygame.display.flip()
    
    # wait until 1/60 of a second has passed
    clock.tick(60)