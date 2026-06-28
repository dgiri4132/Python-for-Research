"""In larger projects, we will often refactor code we've written before adding more code
refactoring helps simplifies the structure of the code you've already written making it easier to build on.
This game functions module will prevent aline_invasion from becoming too lengthy and will make the logicc in alien _invasion easier to follow"""

import sys
import pygame
from bullet import Bullet

"""This module imports sys and pygame. After that it is used in many game instances as needed, no need
to write it every time"""

"""Now, we move the code for updating the screen to a function update_screen() to simplify run_game()"""

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

""" Now we're gonna start on dealing with keypresses.
    So every time a key is pressed, it goes as an event in the pygame and
    is picked up by pygame.event.get(). 
    Each keypress is registered as a KEYDOWN event. I thought we needed if clauses for which key pressed and
    that seems to be right as well. Also we need to assign what we need to given that the certain key is pressed as well"""


"""The check events function will grow as the project grows so it is better if we separate them for key up and down as well"""

def check_keydown_events(event, ship, ai_settings, screen, bullets):
    if event.key==pygame.K_RIGHT:
    #Move the ship to the right.
        ship.moving_right=True
    elif event.key == pygame.K_LEFT:
        ship.moving_left=True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
            
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, bullets, ship):
    """Respond to keypresses ."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship, ai_settings,bullets, screen)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
