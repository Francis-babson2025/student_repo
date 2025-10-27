from copy import copy
from mini_max import mini_max
from game_over import game_over


def find_move(board, XsTurn):
    """
    Finds the best move for the current player using minimax.
    - board: current state of the game (list of 9 squares).
    - XsTurn: True if it's X's turn, False if it's O's turn.
    Returns: the index (0-8) of the best move.
    """

    # Start with worst possible score for this player
    best_score = float('-inf') if XsTurn else float('inf')
    best_move = None

    # X maximizes, O minimizes
    compare = max if XsTurn else min

    # X marks with 10, O marks with -10
    points = 10 if XsTurn else -10

    # Try every square
    for square in range(9):
        new_board = copy(board)

        if new_board[square] not in (10, -10):  # Only empty squares
            new_board[square] = points  # Try this move

            # If the game ends right away, return this winning move
            if game_over(new_board):
                return square

            # Otherwise, use minimax to evaluate how good this move is
            score = mini_max(new_board, not XsTurn, 0)

            # If this score is better (for X: higher, for O: lower), update best_move
            if compare(best_score, score) == score:
                best_score = score
                best_move = square

    return best_move
