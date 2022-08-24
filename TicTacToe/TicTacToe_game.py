import time
from Player import HumanPlayer, ComputerPlayer


class TicTacToe:
    """Represent the definitions and the necessary functions to play the game"""

    def __init__(self):
        """Initialize the board."""
        self.board = [' ' for _ in range(9)]
        self.winner = None

    def print_board(self):
        # Function to print the board.
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:  # 0-2, 3-5, 6-8
            print("| " + " | ".join(row) + " |")

    @staticmethod
    # Is not related to the game. Print a general board for a quick reference.
    def print_board_nums():
        number_board = [[str(num) for num in range(row * 3, (row + 1) * 3)] for row in range(3)]  # Join works on
        # strings.
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        """Create a list of all the available moves for a player."""
        return [move for move, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        """Check if the board is empty or not. Return true if not empty."""
        return " " in self.board

    # def number_empty_squares(self):
    # """Not using in this code."""
    #     return len(self.available_moves())
    #     # Can also return the count of empty spaces on the board

    def check_winner(self, spot, letter):
        # Checking rows
        row_index = spot // 3  # Spot = 3 is in the second row. 3 // 3 = 1.0 which is the second row if we have 3 rows.
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([spot_r == letter for spot_r in row]):
            return True

        # Checking columns
        col_index = spot % 3  # Spot = 3 must be the first column of the second row. We must check the first column of
        # all the rows.
        column = [self.board[col_index + row * 3] for row in range(3)]
        if all([spot_c == letter for spot_c in column]):
            return True

        # Checking diagonals
        if all([self.board[spot_d1] == letter for spot_d1 in [0, 4, 8]]):
            return True
        if all([self.board[spot_d2] == letter for spot_d2 in [2, 4, 6]]):
            return True

        return False

    def make_a_move(self, spot, letter):
        """Make a move to an empty space."""
        if self.board[spot] != " ":
            return False
        else:
            self.board[spot] = letter
            if self.check_winner(spot, letter):
                self.winner = letter
            return True


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X"

    while game.empty_squares():
        if letter == "O":
            spot = o_player.get_moves(game)
        else:
            spot = x_player.get_moves(game)

        if game.make_a_move(spot, letter):
            if print_game:
                print(f'\n{letter} makes a move to the spot {spot}')
                game.print_board()
                print("-------------")

            if game.winner:
                if print_game:
                    print(f"{letter} wins the game!")
                    return letter

            letter = "O" if letter == "X" else "X"

        time.sleep(1)

    if print_game:
        print("It is a draw.")


if __name__ == '__main__':
    x_player = HumanPlayer("X")
    o_player = ComputerPlayer("O")
    ttt_game = TicTacToe()
    play(ttt_game, x_player, o_player)
