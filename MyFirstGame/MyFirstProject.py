# Simple pygame program
import random
import pygame
import math
from pygame import mixer

# Import and initialize the pygame library
pygame.init()
# Set the background image
# create the display surface object
# of specific dimension..e(900, 750).
win = pygame.display.set_mode((900, 750))
# set my background
background = pygame.image.load('pub.png')
# set my background music
mixer.music.load('very-busy-bar.mp3')
mixer.music.play(-1)
# set the pygame window name
pygame.display.set_caption("Beer Drinking")
# load my drunk boy png
drunkImg = pygame.image.load('drunkboy.png')
x_Player = 300
y_Player = 425
x_Player_Change = 0
# velocity / speed of movement
vel = 5

beerImg = []
x_Beer = []
y_Beer = []
x_Beer_Change = []
y_Beer_Change = []
number_of_beers = 2

# load my beers
for i in range(number_of_beers):
    beerImg.append(pygame.image.load('beer-can.png'))
    x_Beer.append(random.randint(0, 700))
    y_Beer.append(0)
    x_Beer_Change.append(0)
    y_Beer_Change.append(2)

# Score
score = 0
font = pygame.font.Font('Reach Story.ttf', 50)
textX = 10
textY = 20

def show_score(x,y):
    score_value = font.render("Score: " + str(score), True, (255,255,255))
    win.blit(score_value, (x, y))


def drunk(x, y):
    win.blit(drunkImg, (x, y))


def beers(x, y, i):
    global beer_state
    win.blit(beerImg[i], (x, y))


def isCollision(x_Beer, y_Beer, x_Player, y_Player):
    distance = math.sqrt((math.pow(x_Beer - x_Player, 2)) + (math.pow(y_Beer - y_Player, 2)))
    if distance < 80:
        return True
    return False


# Run until the user asks to quit
running = True
while running:
    win.fill([255, 255, 255])
    win.blit(background, (0, 0))
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # stores keys pressed
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_Player_Change = -5
            elif event.key == pygame.K_RIGHT:
                x_Player_Change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_Player_Change = 0
    x_Player += x_Player_Change
    # Checking for boundaries of spaceship so it doesn't go out of bounds
    if x_Player < 0:
        x_Player = 0
    elif x_Player > 725:
        x_Player = 725

    # Beer Movements
    for i in range(number_of_beers):
        y_Beer[i] += y_Beer_Change[i]
        if y_Beer[i] > 750:
            glass_broke = mixer.Sound('glass-breaking.mp3')
            glass_broke.play()
            y_Beer[i] = 0
            x_Beer[i] = random.randint(0, 700)
        # Collisions
        collision = isCollision(x_Beer[i], y_Beer[i], x_Player, y_Player)
        if collision:
            drinking = mixer.Sound('heavy_swallowwav.mp3')
            drinking.play()
            y_Beer[i] = 0
            x_Beer[i] = random.randint(0, 700)
            score += 1
        beers(x_Beer[i], y_Beer[i], i)
    drunk(x_Player, y_Player)
    show_score(textX,textY)
    pygame.display.update()

# Done! Time to quit.
pygame.quit()