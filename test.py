import pygame
import sys
from math import pi


#Define colors we want to use in RGB format

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE =(0,0,255)
RED =(255,0,0)
GREEN =(0,255,0)

# Set the height and width of the screen and then create the screen
SIZE = [400, 400]
screen = pygame.display.set_mode(SIZE)



#Display the caption of our screen
pygame.display.set_caption("Our Drawing Canvas")

#Loop until user clicks the close button
done = False
clock = pygame.time.Clock()

while not done:
    #We limit while loop to ten times per second
    # If you do not do this, it will use up too much memory

    #pygame.event.get() returns an list of events
    for event in pygame.event.get(): #If the user did something
        if event.type == pygame.QUIT: # User clicked Close
            done = True # Flag that we are done and want to exit loop

    #clear screen and set screen background
    screen.fill(WHITE)
    #Draw a green line on the screen from (0,0) to (50,50)
    pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)


    # Draw on the screen 3 BLACK lines, each 5 pixels wide.
    # The 'False' means the first and last points are not connected.
    pygame.draw.lines(screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)

    # Draw on the screen a GREEN line from (0, 50) to (50, 80) 
    # Because it is an antialiased line, it is 1 pixel wide.
    pygame.draw.aaline(screen, GREEN, [0, 50],[50, 80], True)


    # Draw a rectangle outline
    pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)


    # Draw a solid rectangle
    pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

    # Draw a rectangle with rounded corners
    pygame.draw.rect(screen, GREEN, [115, 210, 70, 40], 10, border_radius=15)
    pygame.draw.rect(screen, RED, [135, 260, 50, 30], 0, border_radius=10, border_top_left_radius=0,
                     border_bottom_right_radius=15)

    # Draw an ellipse outline, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)

    # Draw an solid ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])


    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
  
    # Draw an arc as part of an ellipse. 
    # Use radians to determine what angle to draw.
    pygame.draw.arc(screen, BLACK,[210, 75, 150, 125], 0, pi/2, 2)
    pygame.draw.arc(screen, GREEN,[210, 75, 150, 125], pi/2, pi, 2)
    pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi,3*pi/2, 2)
    pygame.draw.arc(screen, RED,  [210, 75, 150, 125], 3*pi/2, 2*pi, 2)
    
    # Draw a circle
    pygame.draw.circle(screen, BLUE, [60, 250], 40)

    # Draw only one circle quadrant
    pygame.draw.circle(screen, BLUE, [250, 250], 40, 0, draw_top_right=True)
    pygame.draw.circle(screen, RED, [250, 250], 40, 30, draw_top_left=True)
    pygame.draw.circle(screen, GREEN, [250, 250], 40, 20, draw_bottom_left=True)
    pygame.draw.circle(screen, BLACK, [250, 250], 40, 10, draw_bottom_right=True)

    #This will update pygame with what we have drawn on the screen
    pygame.display.flip()



pygame.quit()

