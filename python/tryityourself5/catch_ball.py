from ball import Ball
from character import Glove
from pygame.sprite import Sprite
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
import pygame
from game_stats import GameStats
import sys
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    glove = Glove(ai_settings, screen)
    balls = Group()
    stats = GameStats(ai_settings)
    gf.create_ball(ai_settings, screen, balls)
    while True:
        gf.check_events(glove)
        if stats.game_active:
            glove.update()
            balls.update()
            if gf.check_contact(balls, glove):
                gf.create_ball(ai_settings, screen, balls)
            if gf.pass_through(balls, ai_settings, screen):
                stats.lives_left-=1
            if stats.lives_left == 0:
                stats.game_active = False
        screen.fill(ai_settings.bg_color)
        glove.blitme()
        balls.draw(screen)
        pygame.display.flip()





