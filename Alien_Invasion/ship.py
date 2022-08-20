import pygame


class Ship:
    """A class to manage the battle ship"""

    def __init__(self, alien_invasion):
        """Initialize the ship and its starting position"""
        self.screen = alien_invasion.screen
        self.screen_rect = alien_invasion.screen.get_rect()

        # Load the ship and get its boundaries
        self.image = pygame.image.load("images/ship.bmp")
        self.image_rect = self.image.get_rect()

        # Create each ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
