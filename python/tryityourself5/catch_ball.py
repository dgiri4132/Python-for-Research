from ball import Ball
from character import Glove
from pygame.sprite import Sprite
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
import pygame

def run_game():
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_height, ai_settings.screen_width))
    glove = Glove(ai_settings, screen)
    ball = Ball(ai_settings, screen)
    balls = Group()
    
    while True:
        

