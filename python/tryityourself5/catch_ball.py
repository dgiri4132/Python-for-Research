from ball import Ball
from character import Glove
from pygame.sprite import Sprite
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
import pygame

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    glove = Glove(ai_settings, screen)
    balls = Group()
    
    gf.create_ball(ai_settings, screen, balls)
    while True:
        gf.check_events(glove)
        glove.update()
        balls.update()
        if gf.check_contact(balls, glove):
            gf.create_ball(ai_settings, screen, balls)
        gf.pass_through(balls, ai_settings, screen)
        screen.fill(ai_settings.bg_color)
        glove.blitme()
        balls.draw(screen)
        pygame.display.flip()





