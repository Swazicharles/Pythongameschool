import pygame

#Telling pygame to start and come alive
pygame.init()

#creating a screen with 800 pixels accross and 600 pixel deep
window = (800,600)

#telling the computer to show the screen
screen = pygame.display.set_mode(window)

#Add title and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

#add image for use with the player
playerImg = pygame.image.load('arcade-game.png')
running = True
while running:
    #we search through a list of events and look for when we want to quit.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # add the image to the screen
    screen.blit(playerImg,(370,480))
    pygame.display.update()

#tells pygame to quit
pygame.quit()
