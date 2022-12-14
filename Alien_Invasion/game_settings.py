class Settings:

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = 0.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (128, 128, 128)
        self.allowed_bullets = 3

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # fleet direction: 1 represents right, fleet direction: -1 represents left
        self.fleet_direction = 1
