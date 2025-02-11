class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_turn = 'X'

    def display_board(self):
        return (f"{self.board[0]} | {self.board[1]} | {self.board[2]}\n"
                f"---------\n"
                f"{self.board[3]} | {self.board[4]} | {self.board[5]}\n"
                f"---------\n"
                f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def make_move(self, player, position):
        if self.board[position - 1] == ' ':
            self.board[position - 1] = player
            return True
        return False

    def check_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def is_draw(self):
        return ' ' not in self.board

    def switch_turn(self):
        self.current_turn = 'O' if self.current_turn == 'X' else 'X'
