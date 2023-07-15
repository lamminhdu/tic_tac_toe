class TicTacToe:
    def __init__(self) -> None:
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        """
            | 1 | 2 | 3 |
            | 4 | 5 | 6 |
            | 7 | 8 | 9 |
        012
        345
        678
        """
        rows = [self.board[3*i:3*i + 3] for i in range(3)]
        for row in rows:
            print(f"| {' | '.join(row)} |")

    @staticmethod
    def print_board_nums():
        rows = [list(range(3*i, 3*i+3)) for i in range(3)]
        for row in rows:
            print(f"| {' | '.join(map(str, row))} |")

    def available_move(self):
        return [index for index, spot in enumerate(self.board) if spot == " "]

    def empty_square(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] != " ":
            return False
        self.board[square] = letter
        if self.winner(square, letter):
            self.current_winner = letter
        return True

    def winner(self, square, letter):
        # Check current column
        col_num = square % 3
        col_values = [self.board[col_num + 3*i] for i in range(3)]
        if all(value == letter for value in col_values):
            return True
        # Check current row
        row_num = square // 3
        row_value = self.board[row_num*3: row_num*3+3]
        if all(value == letter for value in row_value):
            return True
        # Check diagonal
        if all(self.board[i] == letter for i in [0,4,8]) or all(self.board[i] == letter for i in [2,4,6]):
            return True 
