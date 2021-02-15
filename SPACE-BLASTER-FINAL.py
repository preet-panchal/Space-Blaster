# PREET PANCHAL
# FINAL SPACE BLASTER GAME
# MULTIPLAYER SPLIT SCREEN GAME
# MAY 2018

"""
 Animating multiple objects using a list.
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 Process each snow flake in the list:
 http: // programarcadegames.com / python_examples / show_file.php?file = animating_snow.py
 Explanation video: http://youtu.be/Gkhz3FuhGoI
"""

# Import a library of functions called 'pygame'
import pygame
import random

# Initialize the game engine
pygame.init()

# Import colours
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
YELLOW = [255, 255, 0]

# Set the height and width of the screen
SCREEN_SIZE = [1200, 900]

# Empty lists for moving objects
meteor_list_blue = []
meteor_list_red = []
star_list = []

# Initialize the game clock
clock = pygame.time.Clock()

# Displaying Screen size
screen = pygame.display.set_mode(SCREEN_SIZE)

# Displays window title
pygame.display.set_caption("Split Screen")

# Importing all images
blue_spaceship = pygame.image.load('Spaceship1.png').convert_alpha()
red_spaceship = pygame.image.load('Spaceship2.png').convert_alpha()
meteor_image =  pygame.image.load('Meteor.png').convert_alpha()
start_screen = pygame.image.load('SpaceBlaster.png')

# For-loop appending coordinates for the meteors
# on blue spaceship side
for i in range(50):
    x_meteor_blue = random.randrange(15, 550)
    y_meteor_blue = 0
    meteor_list_blue.append([x_meteor_blue, y_meteor_blue])

# Function for displaying blue spaceship
def BLUE(x_change_blue, y_change_blue):
    screen.blit(blue_spaceship, (x_change_blue, y_change_blue))

# Variables controlling blue spaceship
x_coord_blue = 0
y_coord_blue = 775

# For-loop appending coordinates for the meteors
# on red spaceship side
for i in range(50):
    x_meteor_red = random.randrange(620, 1155)
    y_meteor_red = 0
    meteor_list_red.append([x_meteor_red, y_meteor_red])

# Function for displaying red spaceship
def RED(x_change_red, y_change_red):
    screen.blit(red_spaceship, (x_change_red, y_change_red))

# Variables controlling red spaceship
x_coord_red = 1110
y_coord_red = 775

# For-loop appending coordinates for the white stars
# on game screen
for i in range(50):
    x_star = random.randrange(0, 1200)
    y_star = random.randrange(0, 900)
    star_list.append([x_star, y_star])

# Variables for bullets on blue side
startX_blue = 45
startY_blue = 773
Xchange_bullet_blue = 0
bullets_blue = [[startX_blue, startY_blue]]

# Variables for bullets on red side
startX_red = 1155
startY_red = 773
Xchange_bullet_red = 0
bullets_red = [[startX_red, startY_red]]


# --- Title Game Screen ---
done = False
title_screen = False
while not done and not title_screen:
    for event in pygame.event.get():
        # To quit game
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE :
                title_screen = True

    # Fills the background screen with Black
    screen.fill(BLACK)

    # Displays title screen when program starts
    screen.blit(start_screen, [0, 0])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


# --- Main Event Loop ---
done = False
while not done:
    for event in pygame.event.get():
        # To quit game
        if event.type == pygame.QUIT:
            done = True
            # If the following keys are pressed,
            # it will control the red or blue spaceship
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Xchange_bullet_red = -5
            elif event.key == pygame.K_RIGHT:
                Xchange_bullet_red = 5
            if event.key == pygame.K_a:
                Xchange_bullet_blue = -5
            elif event.key == pygame.K_d:
                Xchange_bullet_blue = 5
        # If no keys are pressed, then nothing will happen
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Xchange_bullet_red = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                Xchange_bullet_blue = 0

    # Fills the background screen with Black
    screen.fill(BLACK)

    # Draws a solid green line in the middle of game screen
    # to split red and blue player side {multiplayer}
    pygame.draw.line(screen, GREEN, [595, 0], [595, 900], 10)

    # For-loop that constantly draws white dots (stars)
    # and animates it on the game screen
    for i in range(len(star_list)):
        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, star_list[i], 2)
        # Move the snow flake down one pixel
        star_list[i][1] += 1
        # If the snow flake has moved off the bottom of the screen
        if star_list[i][1] > 900:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            star_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 1200)
            star_list[i][0] = x


    # Displays meteors on blue player side
    for meteors in meteor_list_blue:
        meteors[1] += 3

    # Displays meteors on red player side
    for meteors in meteor_list_red:
        meteors[1] += 3

    # Animates meteors falling one at a time on blue side
    for i in range(100):
        if y_meteor_blue >= 900:
        # Reset it just above the top
            x_meteor_blue = random.randrange(15, 550)
            y_meteor_blue = random.randrange(-50, -10)
        screen.blit(meteor_image, [x_meteor_blue, y_meteor_blue])

    # Animates meteors falling one at a time on red side
    for i in range(100):
        if y_meteor_red >= 900:
        # Reset it just above the top
            x_meteor_red = random.randrange(620, 1155)
            y_meteor_red = random.randrange(-50, -10)
        screen.blit(meteor_image, [x_meteor_red, y_meteor_red])


    # Restrictions for bullets on blue side
    if startX_blue <= 45:
        startX_blue += 2
        startX_blue += 2
        startX_blue += 2

    if startX_blue >= 550:
        startX_blue -= 2
        startX_blue -= 2
        startX_blue -= 2

    # Synchronizes Blue spaceship with bullets
    x_coord_blue += Xchange_bullet_blue
    BLUE(x_coord_blue, y_coord_blue)

    # Controls movement of bullets on blue side
    startX_blue += Xchange_bullet_blue

    # Move all bullets 3px
    for bullet in bullets_blue:
        bullet[1] = bullet[1] - 3

    # If the last bullet is off the screen, remove it
    if bullets_blue[len(bullets_blue) - 1][1] < 0:
        bullets_blue.remove(bullets_blue[len(bullets_blue) - 1])

    # If the first bullet is more than 50px from the initial location, add another
    if bullets_blue[0][1] + 50 < startY_blue:
        bullets_blue.insert(0, [startX_blue, startY_blue])

    # Blue spaceship restrictions on game screen
    if x_coord_blue <= 0:
        x_coord_blue += 2
        x_coord_blue += 2
        x_coord_blue += 2
    if x_coord_blue >= 504:
        x_coord_blue -= 2
        x_coord_blue -= 2
        x_coord_blue -= 2

    # Displays bullets on blue side
    for bullet in bullets_blue:
        pygame.draw.line(screen, YELLOW, bullet, [bullet[0], bullet[1] + 10], 3)


    # Restrictions for bullets on red side
    if startX_red <= 649:
        startX_red += 2
        startX_red += 2
        startX_red += 2

    if startX_red >= 1155:
        startX_red -= 2
        startX_red -= 2
        startX_red -= 2

    # Synchronizes Red spaceship with bullets
    x_coord_red += Xchange_bullet_red
    RED(x_coord_red, y_coord_red)

    # Controls movement of bullets on red side
    startX_red += Xchange_bullet_red

    # Move all bullets 3px
    for bullet in bullets_red:
        bullet[1] = bullet[1] - 3

    # If the last bullet is off the screen, remove it
    if bullets_red[len(bullets_red) - 1][1] < 0:
        bullets_red.remove(bullets_red[len(bullets_red) - 1])

    # If the first bullet is more than 50px from the initial location, add another
    if bullets_red[0][1] + 50 < startY_red:
        bullets_red.insert(0, [startX_red, startY_red])

    # Rlue spaceship restrictions on game screen
    if x_coord_red <= 605:
        x_coord_red += 2
        x_coord_red += 2
        x_coord_red += 2
    if x_coord_red >= 1110:
        x_coord_red -= 2
        x_coord_red -= 2
        x_coord_red -= 2

    # Displays bullets on red side
    for bullet in bullets_red:
        pygame.draw.line(screen, YELLOW, bullet, [bullet[0], bullet[1] + 10], 3)


# Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Controls the speed of the meteors falling
    y_meteor_blue += 5
    y_meteor_red += 5

    # Game clock tick set to 60 to run game
    clock.tick(60)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
