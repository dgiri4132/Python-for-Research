import sys
import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien
def run_game():
    #Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

        
    # Make a ship

    ship = Ship(ai_settings, screen)
    #Start the main loop for the game.
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen,ship, aliens)
    while True:
        
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship,aliens, bullets)
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

we added the bullets update thing and another argument as bullets in the checkevents as well
we also copied the bullets as a whole, because you shouldn't use the real thing to check
and then remoed if it reaches the top .
    """


run_game()

""" We import settings file and use its functions, like using screen_width and screen_height attributes
of ai_settings, also when we used the background color as well."""

"""
This is the try-it-yourself part of the chapter

import pygame
import sys

def rungame():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame..display.set_caption("Blue Background: Try it yourself")
    bg_color=(0,230,0)
    
    while True:
        screen.fill(bg_color)
"""