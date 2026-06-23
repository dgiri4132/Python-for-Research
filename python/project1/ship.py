"""To add the ship image, we have to load an image and then use the Pygame method blit()
we will be using bitmap for the image of ship that we will be using.

"""
import pygame

class Ship():
    
    def __init__(self, screen):
        """Initializing the ship and setting its starting position."""
        self.screen=screen
    
        self.image=pygame.game.load()
        self.rect=self.image.get_rect()
        self.screen_rect= screen.get_rect()
        self.rect.centerx= self.screen_rect.centrex
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

""" So the self.image returns a surface representing the ship. The second thing does the work of making it a rectangle.
The next two attributes help to make the starting point of the ship and the final method draws the image to the 
screen at the position specifed by self.react"""