import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class that represents a single alien"""

    def __init__(self, alien_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = alien_game.screen
        self.settings = alien_game.settings

        # Load the alien image and set its rectangle attribute
        self.image = pygame.image.load('C:/Users/14039/PycharmProjects/Projects/Alien_Invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Create new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right or left."""

        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

