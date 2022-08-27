import math
import random


class Player:
    """Creates the parent class to represent the players."""
    """A Human Player, a Dumb Computer Player, and a Smart Computer Player."""

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


class SmartComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_moves(self, game):
        if len(game.available_moves()) == 9:
            spot = random.choice(game.available_moves())
        else:
            spot = self.minimax(game, self.letter)['position']

        return spot

    def minimax(self, state, player):  # State: Game, Player: Letter
        max_player = self.letter  # The player whose utilization we will maximize.
        other_player = 'O' if player == 'X' else 'X'  # Player who will try to minimize the utilization of other player.

        # Check if the last move resulted in a win.
        if state.winner == other_player:
            return {'position': None, 'score': 1 * (state.number_of_empty_square() + 1) if other_player == max_player
                else -1 * (state.number_of_empty_square() + 1)}
        elif not state.check_if_empty():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_a_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # Simulate the game after making the move

            # After we have the score, we have to undo the changes we made
            state.board[possible_move] = ' '
            state.winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
