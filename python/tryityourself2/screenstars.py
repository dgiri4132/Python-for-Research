from stars import Stars
import pygame
import sys
from pygame.sprite import Group
from settings import Settings

def get_numberof_rows(ai_settings, star_height):
    available_space_y = (ai_settings.screen_height)
    number_rows = int(available_space_y/star_height)
    return number_rows

def get_number_of_stars(ai_settings, star_width):
    available_space_x = ai_settings.screen_width - 2*star_width
    number_of_stars = int(available_space_x/star_width)
    return number_of_stars

def makingstars(ai_settings, screen,stars, star_number, row_number):
    star = Stars(ai_settings, screen)
    star_width = star.rect.width
    star.x = star_width + 2* star_width*star_number
    star.rect.x = star.x
    star_height = star.rect.height
    star.rect.y = star_width + 2*star_height * row_number
    stars.add(star)

def create_stars(ai_settings, screen, stars):
    star = Stars(ai_settings, screen)
    number_of_stars=get_number_of_stars(ai_settings, star.rect.width)
    number_of_rows = get_numberof_rows(ai_settings, star.rect.height)
    for row in range(number_of_rows):
        for star_number in range(number_of_stars):
            makingstars(ai_settings,screen, stars, star_number, row)


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Starry Night")

    stars= Group()
    create_stars(ai_settings, screen, stars)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        stars.draw(screen)
        pygame.display.flip()
run_game()
