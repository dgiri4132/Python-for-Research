import pygame
from pygame.sprite import Sprite,Group

class Shield(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('brick.bmp')
        self.rect = self.image.get_rect()
        self.height = self.rect.height
        self.width = self.rect.width
        self.y = self.rect.top
        self.y1 = self.rect.bottom
        self.screen_rect = screen.get_rect()
