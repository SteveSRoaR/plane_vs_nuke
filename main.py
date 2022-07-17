# snake game
import random
import pygame
from pygame import *
from pygame import mixer
import math

# init
pygame.init()

# display
icon = pygame.image.load("nuclear-bomb.png")
pygame.display.set_caption("plane vs nuke")
pygame.display.set_icon(icon)
surface = pygame.display.set_mode((800, 600))
mixer.music.load("Ethir-Neechal.mp3")
mixer.music.play(-1)

surface.fill((255, 255, 255))
pygame.display.update()

# font
font = pygame.font.Font("freesansbold.ttf", 30)
rules_font = pygame.font.Font("font.ttf", 1)

# background
layer_1 = pygame.image.load("background_2.jpg")
layer = pygame.image.load("blackground.png")
# enemy----------------------------------------------------------------------------------------------------------------

enemy_spite = []
enemyX = []
enemyY = []
enemy_speed_Y = []
number_of_enemy = 6
for i in range(number_of_enemy):
    enemy_spite.append(pygame.image.load("nuclear-bomb.png"))
    enemyX.append(random.randint(60, 650))
    enemyY.append(random.randint(60, 450))
    enemy_speed_Y.append(0.9)

# end of enemy ---------------------------------------------------------------------------------------------------------

# heart-----------------------------------------------------------------------------------------------------------------

heart_sprite = []
heartX = []
heartY = []
speed_heart_Y = []
number_of_heart = 2
for l in range(number_of_heart):
    heart_sprite.append(pygame.image.load("heart.png"))
    heartX.append(random.randint(60, 650))
    heartY.append(random.randint(60, 450))
    speed_heart_Y.append(0.9)

# end of heart----------------------------------------------------------------------------------------------------------

# coin------------------------------------------------------------------------------------------------------------------
coin_sprite = []
coinX = []
coinY = []
speed_coin_Y = []
number_of_coins = 5
for k in range(number_of_coins):
    coin_sprite.append(pygame.image.load("dollar.png"))
    coinX.append(random.randint(60, 650))
    coinY.append(random.randint(60, 450))
    speed_coin_Y.append(0.7)

# end of coin-----------------------------------------------------------------------------------------------------------

# plane-----------------------------------------------------------------------------------------------------------------

blockX = 375
blockY = 450

# end of plane----------------------------------------------------------------------------------------------------------

# functions
def enemy(ex, ey, es):
    surface.blit(es, (ex, ey))

def display_life():
    life_score = font.render("LIFE: " + " " + str(life), True, (0, 0, 0))
    surface.blit(life_score, (5, 10))

def heart(hx, hy, hs):
    surface.blit(hs, (hx, hy))

def coin(cx, cy, cs):
    surface.blit(cs, (cx, cy))

def display_score():
    score_font = font.render("SCORE = " + " " + str(score), True, (0, 0, 0))
    surface.blit(score_font, (600, 10))

def display_rules():
    rules_display = font.render("hit on boundaries = lose 1 heart, hit on bullet = defeat", True, (0, 0, 0))
    surface.blit(rules_display, (10, 550))

def plane(px, py):
    plane_sprite = pygame.image.load("aircraft.png")
    surface.blit(plane_sprite, (px, py))

def game_over():
    over = pygame.image.load("gameover.jpg")
    surface.blit(over, (0, 0))

# enemy collusion-------------------------------------------------------------------------------------------------------
def collusion_enemy(ex, ey):
    distance_collusion = math.sqrt(pow((blockX - ex), 2) + pow((blockY - ey), 2))
    if distance_collusion < 26:
        return True
    else:
        return False
# heart collusion-------------------------------------------------------------------------------------------------------
def collusion_heart(hx, hy):
    distance_collusion = math.sqrt(pow((blockX - hx), 2) + pow((blockY - hy), 2))
    if distance_collusion < 26:
        return True
    else:
        return False
# coin collusion--------------------------------------------------------------------------------------------------------
def collusion_coin(cx, cy):
    distance_collusion = math.sqrt(pow((blockX - cx), 2) + pow((blockY - cy), 2))
    if distance_collusion < 26:
        return True
    else:
        return False


# variable declaration
running = True
life = 5
score = 0
speed = 0

# mainloop
while running:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_RIGHT:
                speed = 4
            if event.key == K_LEFT:
                speed = -4

        if event.type == KEYUP:
            speed = 0
        elif event.type == QUIT:
            running = False
    surface.fill((255, 255, 255))
    surface.blit(layer_1, (0, 0))
    surface.blit(layer, (50, 50))
    display_life()
    display_score()
    display_rules()

    # enemy mode start ------------------------------------------------------------------------------------------------E
    for i in range(number_of_enemy):
        enemyY[i] += enemy_speed_Y[i]
        enemy(enemyX[i], enemyY[i], enemy_spite[i])
        co = collusion_enemy(enemyX[i], enemyY[i])
        if co:
            life -= 1
        if life < 0:
            for j in range(number_of_enemy):
                enemyY[j] = 1000
                blockY = 1000
                game_over()
                break

        if enemyY[i] > 500:
            enemyY[i] = 60
        # end of enemy mode -----------------------------------------------------------------------------------------(E)

    # heart mode start------------------------------------------------------------------------------------------------H
    for i in range(number_of_heart):
        heartY[i] += speed_heart_Y[i]
        heart(heartX[i], heartY[i], heart_sprite[i])
        Hco = collusion_heart(heartX[i], heartY[i])
        if Hco:
            life += 1
            heartX[i] = 60
        if life < 0:
            for j in range(number_of_heart):
                heartY[j] = 1000
        if heartY[i] > 500:
            heartY[i] = 60

        # end of heart mode -----------------------------------------------------------------------------------------(H)

    # coin mode start--------------------------------------------------------------------------------------------------C
    for i in range(number_of_coins):
        coinY[i] += speed_coin_Y[i]
        coin(coinX[i], coinY[i], coin_sprite[i])
        Cco = collusion_coin(coinX[i], coinY[i])
        if Cco:
            score += 1
            coinX[i] = random.randint(60, 650)
            coinY[i] = random.randint(60, 65)
        if life < 0:
            for j in range(number_of_coins):
                coinY[j] = 1000
        if coinY[i] > 500:
            coinY[i] = 60

    blockX += speed
    plane(blockX, blockY)

    display.update()

    # plane
    if blockX > 700:
        blockX = 375
        life -= 1
    if blockX < 60:
        blockX = 375
        life -= 1
pygame.display.update()
