"""In larger projects, we will often refactor code we've written before adding more code
refactoring helps simplifies the structure of the code you've already written making it easier to build on.
This game functions module will prevent aline_invasion from becoming too lengthy and will make the logicc in alien _invasion easier to follow"""

import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
"""This module imports sys and pygame. After that it is used in many game instances as needed, no need
to write it every time"""

"""Now, we move the code for updating the screen to a function update_screen() to simplify run_game()"""

def update_screen(ai_settings, screen, ship, aliens,bullets):
    """Update images on the screen and flip to the new screen"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()

""" Now we're gonna start on dealing with keypresses.
    So every time a key is pressed, it goes as an event in the pygame and
    is picked up by pygame.event.get(). 
    Each keypress is registered as a KEYDOWN event. I thought we needed if clauses for which key pressed and
    that seems to be right as well. Also we need to assign what we need to given that the certain key is pressed as well"""

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    stats.ship_left-=1
    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    sleep(0.5)
"""The check events function will grow as the project grows so it is better if we separate them for key up and down as well"""
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keydown_events(event, ship, ai_settings, screen, bullets):
    if event.key==pygame.K_RIGHT:
    #Move the ship to the right.
        ship.moving_right=True
    elif event.key == pygame.K_LEFT:
        ship.moving_left=True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
            
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses ."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship, ai_settings, screen, bullets)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
   collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
   if len(aliens)==0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
    
def update_bullets(ai_settings, screen, ship, aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
""" The latest updates:
    The group bullets is passed to check_keydown_events(). When the player presses the spacebar,
    we create a new bullet and adds it to the group as well. we also add it to the checkdown events as well
     we also added a new function update bullets in the screen and another function specifically focused on firing bullets."""

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3*alien_height)-ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/ (2*alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2* alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen,ship, aliens):
    #create an alien and find the number of aliens in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y+= ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1
def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

