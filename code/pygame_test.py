"""
pygame_test.py - a graphical calculator and an excercise in Pygame and Python
by Philip deZonia
last modified: 2017-02-01
"""

# import required modules
import pygame
import os
import math

# start modules required by pygame
pygame.init()

# create game window
window = pygame.display.set_mode((1200, 900))

# create clock timer to limit frame rate
clock = pygame.time.Clock()

# initialize status
is_done = False
square_is_blue = True
x_pos = 30
y_pos = 30
heading = 0 # angle of ship

# get fonts ready
ourFont = pygame.font.Font(None, 36)

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
        
        # check if user exited window
        if event.type == pygame.QUIT:
            is_done = True
        if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE)):
            square_is_blue = not square_is_blue
            
    # update position of square
    if pygame.key.get_pressed()[pygame.K_UP]: y_pos -= 1
    if pygame.key.get_pressed()[pygame.K_DOWN]: y_pos += 1
    if pygame.key.get_pressed()[pygame.K_LEFT]: x_pos -= 1
    if pygame.key.get_pressed()[pygame.K_RIGHT]: x_pos += 1
    if pygame.key.get_pressed()[pygame.K_z]: heading += 1
    if pygame.key.get_pressed()[pygame.K_x]: heading -= 1
    
    # determine color of square
    if square_is_blue:
        color = (0, 100, 255)
    else:
        color = (255, 100, 0)

    # redraw screen to clear up previous iterations of the square
    window.fill((0, 0, 0)) # black background
    
    # redraw the square that is blue-green with upper corner at 30, 30
    # on screen with side length 60
    # pygame.draw.rect(window, color, pygame.Rect(30, 30, 64, 64))
    window.blit(get_image('testBackSquare.png'), (30, 30))
    
    # get image object
    ship = pygame.transform.rotate(get_image('apple_cat small.png'), heading)
    
    # get center offset
    xc = ship.get_size()[0]/2
    yc = ship.get_size()[1]/2

    # draw spaceship
    window.blit(ship, (x_pos - xc, y_pos - yc))
    # + 13*(math.cos(4*heading*math.pi/180))
    
    # update game window
    pygame.display.flip()
    
    # wait until 1/60 of a second has passed
    clock.tick(60)
    