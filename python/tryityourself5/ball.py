import pygame
from pygame.sprite import Sprite
class Ball(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('ball.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        self.y +=self.ai_settings.ball_speed_factor
        self.rect.y = self.y
