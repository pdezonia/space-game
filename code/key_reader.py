"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
key_reader.py defines a function for reading the keyboard presses and
converting them into a list of flags for the game to use.
I guess I should say that this is part of the space game project.
"""

import pygame

pygame.init()

def get_key_inputs():
    """Returns a list of flags describing which keys have been pressed.
    Inputs correspond to [w, s, d, a, shift, ctrl, space].
    """
    inputs = [0, 0, 0, 0, 0, 0, 0]
    if pygame.key.get_pressed()[pygame.K_w]: inputs[0] = 1
    if pygame.key.get_pressed()[pygame.K_s]: inputs[1] = 1
    if pygame.key.get_pressed()[pygame.K_a]: inputs[3] = 1
    if pygame.key.get_pressed()[pygame.K_d]: inputs[2] = 1
    if pygame.key.get_pressed()[pygame.K_LSHIFT]: inputs[4] = 1
    if pygame.key.get_pressed()[pygame.K_LCTRL]: inputs[5] = 1
    if pygame.key.get_pressed()[pygame.K_SPACE]: inputs[6] = 1
    return inputs