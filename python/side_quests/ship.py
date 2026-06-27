import pygame

class Ship():
    def __init__(self, ai_setting, screen):
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.centerx=float(self.rect.centerx)
        self.centery=float(self.rect.centery)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx+=1
        if self.moving_left and self.rect.left > 0:
            self.centerx-=1
        
        if self.moving_up and self.rect.top>0:
            self.centery-=1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery+=1

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)

