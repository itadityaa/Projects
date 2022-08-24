import random


class Player:
    """Creates the parent class to represent the players."""
    """A Human Player and A Computer Player."""
    # Letters X and O will represent the two players

    def __init__(self, letter):
        self.letter = letter    # Either X or O

    def get_moves(self, game):
        pass


class ComputerPlayer(Player):
    """Represents the Computer"""
    def __init__(self, letter):
        super().__init__(letter)

    def get_moves(self, game):
        pass


class HumanPlayer(Player):
    """Represents the Human"""
    def __init__(self, letter):
        super().__init__(letter)

    def get_moves(self, game):
        pass
