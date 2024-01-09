import pygame
import random


#initialize pygame

pygame.init()

#create the screen (x,y)
screen = pygame.display.set_mode((800,600))

#title and Icon
pygame.display.set_caption("Space invaders")
icon =  pygame.image.load('rocket.png')
pygame.display.set_icon(icon)


#player image

playerImg = pygame.image.load('arcade-game.png')
playerX = 370
playerY = 480
playerX_change = 0

#enemy Image
enemyImg = pygame.image.load('space-ship.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40


#Bullet Image
#bullet state ready/you cant see it ready/ bullet is moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    # We want to center the bullet on the spacehsip
    screen.blit(bulletImg,(x+16 , y+5))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

#This is the game loop
running = True
while running:


    #Here you give color to the screen
    screen.fill((0,0,0))

    #go through events to see what to do 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)
                  

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0 

    #bullet movement
    
    if bulletY<=0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change

    playerX+=playerX_change

    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    #move enermy and check for boundaries. Enemy movement.
    enemyX+=enemyX_change

    if enemyX <=0:
        enemyX_change = 0.2
        enemyY +=enemyY_change
    elif enemyX >=736:
        enemyX_change = -0.2
        enemyY +=enemyY_change
    player(playerX,playerY)
    enemy(enemyX,enemyY) 

    #this line updates the screen
    pygame.display.update()


pygame.quit()


