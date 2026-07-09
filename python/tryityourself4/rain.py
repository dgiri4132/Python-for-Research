import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('raindrop.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
