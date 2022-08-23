import pygame


class Ship:
    """A class to manage the battle ship"""

    def __init__(self, alien_invasion):
        """Initialize the ship and its starting position"""
        self.screen = alien_invasion.screen
        self.screen_rect = alien_invasion.screen.get_rect()
        self.settings = alien_invasion.settings

        # Load the ship and get its boundaries
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Create each ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_left = False

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on movement flag."""
        # Update the ship's x value, not the rectangle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
