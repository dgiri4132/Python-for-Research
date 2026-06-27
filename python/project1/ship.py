"""To add the ship image, we have to load an image and then use the Pygame method blit()
we will be using bitmap for the image of ship that we will be using.

"""
import pygame

class Ship():
    
    def __init__(self,ai_settings, screen):
        """Initializing the ship and setting its starting position."""
        self.screen=screen
        self.ai_settings = ai_settings
        self.image=pygame.game.load('ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect= screen.get_rect()
        self.rect.centerx= self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.center= float(self.rect.centerx)

        self.moving_right=False
        self.moving_left=False
    """Now we need to know when the ship is in motion and when motionless,
    we will start by setting moving_right to False and then when the key is pressed
    it turns to true and again turning to false when key is relieved."""
    def update(self):
        if self.moving_right:
            self.rect.centerx+=self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.rect.centerx-=self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

""" So the self.image returns a surface representing the ship. The second thing does the work of making it a rectangle.
The next two attributes help to make the starting point of the ship and the final method draws the image to the 
screen at the position specifed by self.react"""

"""We firstly add self.center to be decimal or float so that the 1.5 is actually working.
Then, we add parameter ai_settings, which is actually settings and also aim to update the right and left
to the ship by the shipp factor rather than per pixel, I think it is more maneagable as well because we can access it in 
settings as well and also feels more professional"""