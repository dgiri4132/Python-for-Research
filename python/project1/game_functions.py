"""In larger projects, we will often refactor code we've written before adding more code
refactoring helps simplifies the structure of the code you've already written making it easier to build on.
This game functions module will prevent aline_invasion from becoming too lengthy and will make the logicc in alien _invasion easier to follow"""

import sys
import pygame

def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

"""This module imports sys and pygame. After that it is used in many game instances as needed, no need
to write it every time"""