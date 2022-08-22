import sys
import pygame

from game_settings import Settings
from ship import Ship
from Bullet import Bullet
from Alien import Alien

"""Project inspired from the book: Python Crash Course: A Hands-On, Project-Based
Introduction to Programming"""


class AlienInvasion:
    """Main Class to control the game"""

    def __init__(self):
        """Initialize the game, and build game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Set the background color. (RGB) - (128, 128, 128) Grey color
        # self.bg_color = (128, 128, 128)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Keeps the game running until a quit event is requested"""

        while True:
            self.check_events()
            self.ship.update()
            self._update_bullets()
            self.update_screen()

    def _update_bullets(self):
        """Update position of bullets and get rid of the old bullets."""
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Make an alien
        alien = Alien(self)
        alien_width, alien.height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Create the first row of aliens.

        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)

    def _create_alien(self, alien_number):
        # Create an alien and place it in the row.
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

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
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.allowed_bullets:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the while loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Make the most recently drawn/updated screen visible
        pygame.display.flip()


if __name__ == '__main__':
    alien_inv = AlienInvasion()
    alien_inv.run_game()
