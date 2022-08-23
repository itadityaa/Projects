class GameStats:
    """Track Statistics for Alien Invasion"""

    def __init__(self, alien_game):
        """Initialize statistics"""
        self.ships_left = None
        self.settings = alien_game.settings
        self.reset_stats()

        # Start Alien Invasion in active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit

