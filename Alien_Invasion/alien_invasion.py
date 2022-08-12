import sys
import os
import pygame

"""Project inspired from the book: Python Crash Course: A Hands-On, Project-Based
Introduction to Programming"""


class AlienInvasion:
    """Main Class to control the game"""

    def __int__(self):
        """Initialize the game, and build game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Keeps the game running until a quit event is requested"""

        while True:
            # Checks for every event(activity) occurring on the keyboard or on the mouse.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn/updated screen visible
            pygame.display.flip()


if __name__ == '__main__':
    alien_inv = AlienInvasion()
    alien_inv.run_game()
