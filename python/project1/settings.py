""" Each time a new functionality comes out, we'll typically introduce some new settings as well
Hence the necessity of having setting class as well."""

class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        #Ship settings
        """Below we will be changing the pixel speed so that the ship can travel faster"""
        self.ship_speed_factor = 1.5
