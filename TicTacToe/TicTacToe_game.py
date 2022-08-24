import time
from Player import HumanPlayer, ComputerPlayer


class TicTacToe:
    """Represents the definitions and the necessary functions to play the game"""

    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None

    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    # Is not related to the game. Prints a general board
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [move for move, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return " " in self.board

    def number_empty_squares(self):
        return len(self.available_moves())
        # Can also return the count of empty spaces on the board

    def make_a_move(self, spot, letter):
        if self.board[spot] != " ":
            return False
        else:
            self.board[spot] = letter
            if self.check_winner(spot, letter):
                self.winner = letter
            return True

    def check_winner(self, spot, letter):
        # Checking rows
        row_index = spot // 3
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([spot_r == letter for spot_r in row]):
            return True

        # Checking columns
        col_index = spot % 3
        column = [self.board[col_index + row * 3] for row in range(3)]
        if all([spot_c == letter for spot_c in column]):
            return True

        # Checking diagonals
        if all([self.board[spot_d1] == letter for spot_d1 in [0, 4, 8]]):
            return True
        if all([self.board[spot_d2] == letter for spot_d2 in [2, 4, 6]]):
            return True

        return False


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
                print(f'{letter} makes a move to the spot {spot}')
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