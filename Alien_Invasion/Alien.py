import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class that represents a single alien"""

    def __init__(self, alien_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = alien_game.screen

        # Load the alien image and set its rectangle attribute
        self.image = pygame.image.load('C:/Users/14039/PycharmProjects/Projects/Alien_Invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Create new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)