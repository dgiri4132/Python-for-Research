from settings import Settings
from rain import Rain
import pygame
import sys
from pygame.sprite import Group

def get_number_rows(ai_settings, rain_height):
    available_space_y = ai_settings.screen_height 
    number_rows = int(available_space_y/rain_height)
    return number_rows

def number_rain_x(ai_settings, rain_width):
    available_space_x = ai_settings.screen_width - (2*rain_width)
    number_rain = int(available_space_x/rain_width)
    return number_rain

def make_rain_drops(ai_settings, screen, rains, rain_number, row_number):
    rain = Rain(ai_settings, screen)
    rain_width = rain.rect.width
    rain.x = rain_width + (2*rain_width*rain_number)
    rain.rect.x = rain.x
    rain_height = rain.rect.height
    rain.y = rain_height + (2*rain_height*row_number)
    rain.rect.y = rain.y
    rains.add(rain)

def create_raindrops(ai_settings, screen,rains):
    rain = Rain(ai_settings, screen)
    number_of_rows = get_number_rows(ai_settings, rain.rect.height)
    number_of_raindrops = number_rain_x(ai_settings, rain.rect.width)
    for row_number in range(number_of_rows):
        for rain_number in range(number_of_raindrops):
            make_rain_drops(ai_settings, screen, rains, rain_number, row_number)
 

def adding_rains(ai_settings, screen, rains, ):
    rain = Rain(ai_settings, screen)
    number_of_rows = get_number_rows(ai_settings, rain.rect.height)
    for row in range(number_of_rows):
        make_rain_drops(ai_settings, screen, rains, row,0)

def moving_down(ai_settings,screen, rains):
    for rain in rains.sprites():
        rain.rect.y+=ai_settings.rain_drop_speed
    adding_rains(ai_settings, screen, rains)

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("RainDrops Moving down")

    rains = Group()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        create_raindrops(ai_settings, screen, rains)
        moving_down(ai_settings, screen,rains)
        screen.fill(ai_settings.bg_color)
        rains.draw(screen)
        pygame.display.flip()

run_game()
