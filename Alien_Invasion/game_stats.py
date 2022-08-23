class GameStats:
    """Track Statistics for Alien Invasion"""

    def __init__(self, alien_game):
        """Initialize statistics"""
        self.settings = alien_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships.left = self.settings.ship_limit
