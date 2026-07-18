import sys
import pygame
from random import randint
from ball import Ball
from character import Glove
from pygame.sprite import Group

def create_ball(ai_settings, screen, balls):
    ball = Ball(ai_settings, screen)
    random_int_x = randint(0,(1200-2*ball.rect.width))
    random_int_y = randint(0,200)
    ball.x = random_int_x
    ball.y = random_int_y
    ball.rect.x = random_int_x
    ball.rect.y = random_int_y
    balls.add(ball)

def keydown_right_left(event,glove):
    if event.key == pygame.K_RIGHT:
        glove.moving_right = True
    elif event.key == pygame.K_LEFT:
        glove.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def keyup_events(event, glove):
    if event.key == pygame.K_RIGHT:
        glove.moving_right = False
    elif event.key == pygame.K_LEFT:
        glove.moving_left = False

def check_events(glove):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_right_left(event,glove)

        elif event.type == pygame.KEYUP:
            keyup_events(event,glove)  
    
def check_contact(balls, glove):
    happen = bool(pygame.sprite.spritecollide(glove, balls, True))
    if happen:
        return True
    return False

def pass_through(balls, ai_settings, screen):
    for ball in balls.sprites():
        if ball.rect.top> ai_settings.screen_height:
            ball.kill()
            create_ball(ai_settings, screen, balls)
            return True

