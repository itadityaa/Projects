import sys
import os
import pygame

"""Project inspired from the book: Python Crash Course: A Hands-On, Project-Based
Introduction to Programming"""


class AlienInvasion:
    """Main Class to control the game"""

    def __init__(self):
        """Initialize the game, and build game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color. (RGB) - (128, 128, 128) Grey color
        self.bg_color = (128, 128, 128)

    def run_game(self):
        """Keeps the game running until a quit event is requested"""

        while True:
            # Checks for every event(activity) occurring on the keyboard or on the mouse.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the while loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn/updated screen visible
            pygame.display.flip()


if __name__ == '__main__':
    alien_inv = AlienInvasion()
    alien_inv.run_game()
