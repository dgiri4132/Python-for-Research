import pygame
class Settings():
    def __init__(self, ai_settings, screen, bullets, aliens):
        self.ai_settings = ai_settings
        self.screen = screen
        self.bullets = bullets
        self.aliens = aliens
        self.image = pygame.image.load('brick.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()