import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('aliem.bmp')
        self.image = pygame.transform.rotate(self.image, -180)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect = self.rect.height

        self.x = float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)