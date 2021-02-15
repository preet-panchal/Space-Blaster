# PREET & TIRTH
# FINAL SPLIT SCREEN
# - MULTIPLAYER SHOOTING DONE

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
import pygame, random, sys, os, time

stdout = sys.__stdout__
stderr = sys.__stderr__

# Initialize the game engine
pygame.init()

FPS = 60

# Import colours
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED_FADE = [250, 219, 216]
GREEN = [0, 255, 0]
BLUE_FADE = [214, 234, 248]
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
blue_spaceship = pygame.image.load('Spaceship1.png')
red_spaceship = pygame.image.load('Spaceship2.png')
meteor_image =  pygame.image.load('Meteor.png')
#start_screen = pygame.image.load('SpaceBlaster.png')

start_screen = pygame.image.load("Start Screen.png")
instruction_screen = pygame.image.load("Instructions Screen.png")
credits_screen = pygame.image.load("Credits Screen.png")
blue_wins = pygame.image.load("Blue Wins.png")
red_wins = pygame.image.load("Red Wins.png")
tie_game = pygame.image.load("Tie Game.png")
# For-loop appending coordinates for the meteors
# on blue spaceship side

x_meteor_blue = random.randrange(15, 550)
meteor_list_blue.append([x_meteor_blue, 0])

blue_meteorw = 30
blue_meteorh = 30

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

red_meteorw = 30
red_meteorh = 30

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
blue_bulletw = 3
blue_bulleth = 10

score_blue = 0

# Variables for bullets on red side
startX_red = 1155
startY_red = 773
Xchange_bullet_red = 0
bullets_red = [[startX_red, startY_red]]
red_bulletw = 3
red_bulleth = 10

score_red = 0


# COLLISION DETECTION
def checkCollision(obj1x, obj1y, obj1w, obj1h, obj2x, obj2y, obj2w, obj2h):

    # check bounding box
    if obj1x + obj1w >= obj2x and obj1x <= obj2x + obj2w:
        if obj1y + obj1h >= obj2y and obj1y <= obj2y + obj2h:
            return True

    return False

game_timer = 2

# --- Title Game Screen ---
done = False
start = False


while not start:
    screen.blit(start_screen, [0, 0])
    for event in pygame.event.get():   # User did something
        if event.type == pygame.MOUSEBUTTONDOWN:  # If user clicked space
             start = True   # Flag that we are done so we exit this loop

while not done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
            pygame.quit()

        screens = 0

        if e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if 261<mx<334 and 850<my<900:
                screens=1
            elif 395<mx<605 and 850<my<900:

                screens=2
            elif 660<mx<794 and 850<my<900:
                screens=3

            elif 846<mx<919 and 850<my<900:
                screens=4


            if screens == 1:
                done = True
            if screens == 2:
                screen.blit(instruction_screen, [0, 0])
            if screens == 3:
                screen.blit(credits_screen, [0, 0])
            if screens == 4:
                screen.blit(start_screen, [0,0])

    pygame.display.flip()

    clock.tick(60)

# --- Main Event Loop ---
game = False

while not game:
    for event in pygame.event.get():
        # To quit game
        if event.type == pygame.QUIT:
            game = True
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
    pygame.draw.line(screen, GREEN, [595, 35], [595, 900], 10)

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

    if meteor_list_blue[0][1] >= 900:
    # Reset it just above the top
        x_meteor_blue = random.randrange(15, 550)
        meteor_list_blue.remove(meteor_list_blue[0])
        meteor_list_blue.insert(0, [x_meteor_blue, 0])

    screen.blit(meteor_image, [x_meteor_blue, meteor_list_blue[0][1]])

    # Animates meteors falling one at a time on red side

    if meteor_list_red[0][1] >= 900:
    # Reset it just above the top
        x_meteor_red = random.randrange(620, 1155)
        meteor_list_red.remove(meteor_list_red[0])
        meteor_list_red.insert(0, [x_meteor_red, 0])

    screen.blit(meteor_image, [x_meteor_red, meteor_list_red[0][1]])



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

    # If the first bullet is more than 10px from the initial location, add another
    if bullets_blue[0][1] + 70 < startY_blue:
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
        pygame.draw.rect(screen, YELLOW, [bullet[0], bullet[1], 3, 10], 3)


    for bullet in bullets_blue:
         if checkCollision(bullet[0], bullet[1], blue_bulletw, blue_meteorh, meteor_list_blue[0][0], meteor_list_blue[0][1], blue_meteorw, blue_meteorh):
             meteor_list_blue.remove(meteor_list_blue[0])
             score_blue += 10

             if meteor_list_blue != 0:
                 x_meteor_blue = random.randrange(15, 550)
                 meteor_list_blue.insert(0, [x_meteor_blue, 0])

    font_blue_score = pygame.font.SysFont('monospace', 25, True, False)
    score_blue_text = font_blue_score.render("SCORE :" + str(int(score_blue)), True, BLUE_FADE)
    screen.blit(score_blue_text, [215, 10])


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

    # If the first bullet is more than 10px from the initial location, add another
    if bullets_red[0][1] + 70 < startY_red:
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
        pygame.draw.rect(screen, YELLOW, [bullet[0], bullet[1], 3, 10], 3)


    for bullet in bullets_red:
         if checkCollision(bullet[0], bullet[1], red_bulletw, red_meteorh, meteor_list_red[0][0], meteor_list_red[0][1], red_meteorw, red_meteorh):
             meteor_list_red.remove(meteor_list_red[0])
             score_red += 10

             if meteor_list_red != 0:
                 x_meteor_red = random.randrange(620, 1155)
                 meteor_list_red.insert(0, [x_meteor_red, 0])

    font_red_score = pygame.font.SysFont('monospace', 25, True, False)
    score_red_text = font_red_score.render("SCORE :" + str(int(score_red)), True, RED_FADE)
    screen.blit(score_red_text, [865, 10])

    game_timer -= 0.020
    if game_timer == 0:
        game = True


    font_game_timer = pygame.font.SysFont('monospace', 25, True, False)
    game_timer_text = font_game_timer.render(str(int(game_timer)), True, WHITE)
    screen.blit(game_timer_text, [575, 10])

         # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Controls the speed of the meteors falling
    meteor_list_blue[0][1] += 6
    meteor_list_red[0][1] += 6

    # Game clock tick set to 60 to run game
    clock.tick(FPS)

game_over = False
while not game_over:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_over = True
            pygame.quit()
        if score_red > score_blue:
            screen.blit(red_wins, [0, 0])
        if score_blue > score_red:
            screen.blit(blue_wins, [0, 0])
        if score_red == score_blue:
         screen.blit(tie_game, [0, 0])


    pygame.display.flip()

    clock.tick(FPS)
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()