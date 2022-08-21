import sys
import pygame

from game_settings import Settings
from ship import Ship

"""Project inspired from the book: Python Crash Course: A Hands-On, Project-Based
Introduction to Programming"""


class AlienInvasion:
    """Main Class to control the game"""

    def __init__(self):
        """Initialize the game, and build game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color. (RGB) - (128, 128, 128) Grey color
        # self.bg_color = (128, 128, 128)

        self.ship = Ship(self)

    def run_game(self):
        """Keeps the game running until a quit event is requested"""

        while True:
            self.check_events()
            self.ship.update()
            self.update_screen()

    def check_events(self):
        """Checks for every event(activity) occurring on the keyboard or on the mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right by 1 unit.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the while loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn/updated screen visible
        pygame.display.flip()


if __name__ == '__main__':
    alien_inv = AlienInvasion()
    alien_inv.run_game()
