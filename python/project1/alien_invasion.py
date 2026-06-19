import sys
import pygame

def run_game():
    #Initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    bg_color=(230,230,230)
    #Start the main loop for the game.

    while True:

        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #Make the most recetnly drawn screen visible.
        pygame.display.flip()

        """
We start by importing the two libraries that we need right.
The sys module is for when we want to quit just to confirm
After we're done with importing we start by fdefining the function
run_game() after which we set the display or the pixel size of the game
The game is controlled by a while loop that contains event loop and code that manages screen updates.
The for loop also known as the event loop will "listen" for an event
and also perform activities accordingly as well. To access the events 
detected by Pygame, we'll use the pygame.event.get() method. Here we will
write a series of if  statements to detect and respond to specific events.

"""  
        screen.fill(bg_color)
        

run_game()

