#12-3

import pygame
import sys
import game_functions as gf
from settings import Settings
from ship import Ship

def rungame():
    pygame.init()

    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Rocket Moving")
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_length))
    bg_color = (230,230,230)

    ship = Ship(ai_settings, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


rungame()