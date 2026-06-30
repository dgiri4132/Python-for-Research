import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0,0) and then set corret position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
                        ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color= ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
        """
        Let's explain what has happened above. We use sprite because you can group 
        related elements and act upon them all at once. The weird syntax with the super is
        python syntax for that specific library extension. The rectangle for the bullet
        is not from an image so we create it from scratch. We initialize at top left but we move it 
        to the correct location in the next two lines to the ship's position because it is dependent 
        on that.
        """

    def update(self):
        """Move the bullet up the screen. """
        #Update the decimal position of the bullet.
        self.y -=self.speed_factor
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

        
