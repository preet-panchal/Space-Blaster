# PREET PANCHAL & TIRTH PATEL
# ICS3U1-01
# MRS. RUBINI-LAFOREST
# WOBURN COLLEGIATE INSTITUTE
# JUNE 9th, 2017

"""
WORKS CITED: 

 - ALL screens(Start, instructions, credits, & game over screens) are designed 
    and created on https://www.canva.com/
 - Star Background animation help:  
    http: // programarcadegames.com / python_examples / show_file.php?file = animating_snow.py
 - Meteor Image: http://falloutequestria.wikia.com/wiki/File:CM_-_Midnight_Shower.png
 - Instrumental Music: https://www.youtube.com/watch?v=plXGctq9OXo
 - checkCollision function used from Mrs. Rubini

"""

"""
This program is a game called 'Space Blaster'. This game is a multiplayer game that consists
of two spaceships; one blue and the other red. There is a solid green line in the middle 
splitting the two player sides respectively. The game's objectively is to simply dodge as many 
meteors as you can by shooting at it. The shooting is automatic and all the users have to do is 
move 'left' or 'right' using the appropriate keys. For every meteor hit, you earn 10pts. Once
the 90 second timer comes to an end, a winner is selected based on the final score.
"""

# Import a library of functions called 'pygame', 'random' & 'sys'
import pygame, random, sys

stdout = sys.__stdout__
stderr = sys.__stderr__

# Initialize the game engine
pygame.init()

# Frames Per Second (FPS)
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
pygame.display.set_caption("SPACE BLASTER")

# Importing all images
blue_spaceship = pygame.image.load('Spaceship1.png')
red_spaceship = pygame.image.load('Spaceship2.png')
meteor_image = pygame.image.load('Meteor.png')
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

# Blue meteor width & height values
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
for i in range(10):
    x_meteor_red = random.randrange(620, 1155)
    y_meteor_red = 0
    meteor_list_red.append([x_meteor_red, y_meteor_red])

# Red meteor width & height values
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
for stars in range(50):
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

# Variables for bullets on red side
startX_red = 1155
startY_red = 773
Xchange_bullet_red = 0
bullets_red = [[startX_red, startY_red]]
red_bulletw = 3
red_bulleth = 10


# COLLISION DETECTION Function
def checkCollision(obj1x, obj1y, obj1w, obj1h, obj2x, obj2y, obj2w, obj2h):
    # check bounding box
    if obj1x + obj1w >= obj2x and obj1x <= obj2x + obj2w:
        if obj1y + obj1h >= obj2y and obj1y <= obj2y + obj2h:
            return True

    return False


# Blue Player scoring function
score_blue = 0


def blue_player(score_blue):
    font_blue_score = pygame.font.SysFont('monospace', 25, True, False)
    score_blue_text = font_blue_score.render("SCORE :" + str(int(score_blue)), True, BLUE_FADE)
    screen.blit(score_blue_text, [215, 10])
    return score_blue


# Red Player scoring function
score_red = 0


def red_player(score_red):
    font_red_score = pygame.font.SysFont('monospace', 25, True, False)
    score_red_text = font_red_score.render("SCORE :" + str(int(score_red)), True, RED_FADE)
    screen.blit(score_red_text, [865, 10])
    return score_red


# Importing & loading music file
background_music = pygame.mixer.music.load("Instrumental Music.mp3")
# Music timer set at zero before loop
music_timer = 0

# Initializing game timer (set to zero)
game_timer = 90

# --- Main Game Title Screen ---
start = False
done = False
while not start and not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = True
    screen.blit(start_screen, [0, 0])

    pygame.display.flip()

    clock.tick(FPS)

# --- Switching of screens Event Loop ---
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()

        # screens set to zero initially
        screens = 0

        # If mouse button is clicked in a certain area, a certain screen will open up
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if 261 < mx < 334 and 850 < my < 900:
                screens = 1
            elif 395 < mx < 605 and 850 < my < 900:
                screens = 2
            elif 660 < mx < 794 and 850 < my < 900:
                screens = 3
            elif 846 < mx < 919 and 850 < my < 900:
                screens = 4

            # Screen bliting of different in-game screens
            if screens == 1:
                done = True
            if screens == 2:
                screen.blit(instruction_screen, [0, 0])
            if screens == 3:
                screen.blit(credits_screen, [0, 0])
            if screens == 4:
                screen.blit(start_screen, [0, 0])

    pygame.display.flip()

    clock.tick(FPS)

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
                Xchange_bullet_red = -7
            elif event.key == pygame.K_RIGHT:
                Xchange_bullet_red = 7
            if event.key == pygame.K_a:
                Xchange_bullet_blue = -7
            elif event.key == pygame.K_d:
                Xchange_bullet_blue = 7
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
    pygame.draw.line(screen, GREEN, [595, 45], [595, 900], 10)

    # If statement to pla music file, music timer now = 1
    if music_timer == 0 or music_timer == 11700:
        pygame.mixer.music.play(-1, 0.0)
        music_timer = 1

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
        # Insert new meteor once one is done one cycle
        meteor_list_blue.insert(0, [x_meteor_blue, 0])

    screen.blit(meteor_image, [x_meteor_blue, meteor_list_blue[0][1]])

    # Animates meteors falling one at a time on red side
    if meteor_list_red[0][1] >= 900:
        # Reset it just above the top
        x_meteor_red = random.randrange(620, 1155)
        meteor_list_red.remove(meteor_list_red[0])
        # Insert new meteor once one is done one cycle
        meteor_list_red.insert(0, [x_meteor_red, 0])

    screen.blit(meteor_image, [x_meteor_red, meteor_list_red[0][1]])

    # Restrictions for bullets on blue side
    if startX_blue <= 45:
        startX_blue += 3
        startX_blue += 3
        startX_blue += 3

    if startX_blue >= 550:
        startX_blue -= 3
        startX_blue -= 3
        startX_blue -= 3

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
        x_coord_blue += 3
        x_coord_blue += 3
        x_coord_blue += 3
    if x_coord_blue >= 502:
        x_coord_blue -= 3
        x_coord_blue -= 3
        x_coord_blue -= 3

    # Displays bullets on blue side and draws it as Yellow rectangles
    for bullet in bullets_blue:
        pygame.draw.rect(screen, YELLOW, [bullet[0], bullet[1], 3, 10], 3)

    # Calling out the scoring function for blue player
    blue_player(score_blue)

    # Collision detection for bullets and meteors on blue side
    for bullet in bullets_blue:
        if checkCollision(bullet[0], bullet[1], blue_bulletw, blue_meteorh, meteor_list_blue[0][0],
                          meteor_list_blue[0][1], blue_meteorw, blue_meteorh):
            meteor_list_blue.remove(meteor_list_blue[0])
            score_blue += 10

            if meteor_list_blue != 0:
                x_meteor_blue = random.randrange(15, 550)
                meteor_list_blue.insert(0, [x_meteor_blue, 0])

    # Restrictions for bullets on red side
    if startX_red <= 646:
        startX_red += 3
        startX_red += 3
        startX_red += 3

    if startX_red >= 1157:
        startX_red -= 3
        startX_red -= 3
        startX_red -= 3

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
    if x_coord_red <= 602:
        x_coord_red += 3
        x_coord_red += 3
        x_coord_red += 3
    if x_coord_red >= 1112:
        x_coord_red -= 3
        x_coord_red -= 3
        x_coord_red -= 3

    # Displays bullets on red side and draws it as Yellow rectangles
    for bullet in bullets_red:
        pygame.draw.rect(screen, YELLOW, [bullet[0], bullet[1], 3, 10], 3)

    # Calling out the scoring function for red player
    red_player(score_red)

    # Collision detection for bullets and meteors on red side
    for bullet in bullets_red:
        if checkCollision(bullet[0], bullet[1], red_bulletw, red_meteorh, meteor_list_red[0][0], meteor_list_red[0][1],
                          red_meteorw, red_meteorh):
            meteor_list_red.remove(meteor_list_red[0])
            score_red += 10

            if meteor_list_red != 0:
                x_meteor_red = random.randrange(620, 1155)
                meteor_list_red.insert(0, [x_meteor_red, 0])

    # Game timer countdown from 90
    game_timer -= 0.020
    if game_timer < 0:
        game = True
        print "GAME OVER."
        print ""

    # Displaying game timer on game screen
    font_game_timer = pygame.font.SysFont('monospace', 35, True, False)
    game_timer_text = font_game_timer.render(str(int(game_timer)), True, WHITE)
    screen.blit(game_timer_text, [575, 10])

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Music timer increment by 1
    music_timer += 1

    # Controls the speed of the meteors falling
    meteor_list_blue[0][1] += 7
    meteor_list_red[0][1] += 7

    # Game clock tick set to 60 to run game
    clock.tick(FPS)

# --- Game Over Event Loop---
game_over_timer = 3
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()
            sys.exit()

    # Once game over timer reaches 0, display the following:
    game_over_timer -= 0.5
    if game_over_timer == 0:
        # Depending on the final game score, a winner is chosen and score + result is printed
        if score_red > score_blue:
            screen.blit(red_wins, [0, 0])
            print "RED SCORE: " + str(score_red)
            print "BLUE SCORE: " + str(score_blue)
            print "Result: RED WINS!"
            print "*-" * 100
        if score_blue > score_red:
            screen.blit(blue_wins, [0, 0])
            print "RED SCORE: " + str(score_red)
            print "BLUE SCORE: " + str(score_blue)
            print "Result: BLUE WINS!"
            print "*-" * 100
        if score_red == score_blue:
            screen.blit(tie_game, [0, 0])
            print "RED SCORE: " + str(score_red)
            print "BLUE SCORE: " + str(score_blue)
            print "Result: TIE GAME!"
            print "*-" * 100

    # Flip pygame screen to display everything
    pygame.display.flip()

    # Game Clock set to 60 Frames per second
    clock.tick(FPS)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
# Complete exit and end of game code
sys.exit()

# Thank you for playing our game! Hope you enjoyed it!