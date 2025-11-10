class GameBoard:
    def __init__(self, rows, cols, default_value='.'):
        """
        Initializes a game board of specified dimensions.
        """
        self.rows = rows
        self.cols = cols
        self.board = []
        for _ in range(rows):
            row = [default_value] * cols  # Create a row with default values
            self.board.append(row)

    def display_board(self):
        """
        Prints the current state of the board.
        """
        for row in self.board:
            print(" ".join(row))

# Create a 3x3 Tic-Tac-Toe board
tic_tac_toe_board = GameBoard(3, 3, default_value='-')
tic_tac_toe_board.display_board()

# Create a 8x8 Chess board
chess_board = GameBoard(8, 8, default_value='.')
# (Further logic to place chess pieces would go here)