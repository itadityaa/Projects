import random


class Player:
    """Creates the parent class to represent the players."""
    """A Human Player and A Computer Player."""

    # Letters X and O will represent the two players

    def __init__(self, letter):
        self.letter = letter  # Either X or O


class ComputerPlayer(Player):
    """Represents the Computer"""

    def __init__(self, letter):
        super().__init__(letter)

    def get_moves(self, game):
        # Get a random valid spot from the game
        empty_spot = random.choice(game.available_moves())
        return empty_spot


class HumanPlayer(Player):
    """Represents the Human"""

    def __init__(self, letter):
        super().__init__(letter)

    def get_moves(self, game):
        valid_square = False
        value = None
        while not valid_square:
            spot = int(input(self.letter + '\'s turn. Input move (0 - 8): '))
            try:
                value = spot
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True

            except ValueError:
                print("\nInvalid Spot! Please try again.\n")

        return value
