import sys
import pygame
from random import randint
from ball import Ball
from character import Glove
from pygame.sprite import Group

def create_ball(ai_settings, screen, balls):
    ball = Ball(ai_settings, screen)
    random_int_x = randint(0,1200)
    random_int_y = randint(0,200)
    ball.rect.x = random_int_x
    ball.rect.y = random_int_y
    balls.add(ball)

def keydown_right_left(event,glove):
    if 
def check_contact(balls, glove):
    happen = bool(pygame.sprite.spritecollide(glove, balls, True))
    if happen:
        return True
    return False

def pass_through(balls, ai_settings):
    for ball in balls.sprites():
        if ball.rect.top> ai_settings.screen_height:
            ball.kill()
            return True
    return False

