import time
from Players import HumanPlayer, ComputerPlayer


class TicTacToe:

    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None

    def print_board(self):
        for row in [self.board[row_index * 3: (row_index + 1) * 3] for row_index in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    # Is not related to the game. Print a general board for a quick reference.
    def print_board_nums():
        number_board = [[str(num) for num in range(row * 3, (row + 1) * 3)] for row in range(3)]  # Join works on
        # strings.
        for row in number_board:
            print("| " + " | ".join(row) + " |")
        print("-------------")

    def available_moves(self):
        return [move for move, spot in enumerate(self.board) if spot == ' ']

    def check_if_empty(self):
        return ' ' in self.board

    def _number_of_empty_square(self):
        return self.board.count(" ")

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

    while game.check_if_empty():
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
                    # play_a = game.play_again()
                    # return play_a
                    return letter

            letter = "O" if letter == "X" else "X"

        time.sleep(0.5)

    if print_game:
        print("It is a draw. '___' ")
        # play_a = game.play_again()
        # return play_a


if __name__ == '__main__':
    # play_again = True
    # while play_again:
    x_player = HumanPlayer("X")
    o_player = ComputerPlayer("O")
    ttt_game = TicTacToe()
    # play_again = play(ttt_game, x_player, o_player)
    play(ttt_game, x_player, o_player)