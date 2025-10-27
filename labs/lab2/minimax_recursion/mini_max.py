from copy import copy
from game_over import game_over
from calc_score import calc_score


def mini_max(board, XsTurn, level):
    """
    Recursive minimax function.
    - board: current state of the game (list of 9 squares).
    - XsTurn: True if it's X's turn, False if it's O's turn.
    - level: how deep we are in recursion (used to slightly reward faster wins / slower losses).
    """

    # Start with the worst possible score for this player.
    # X wants to maximize (start -inf). O wants to minimize (start +inf).
    best_score = float('-inf') if XsTurn else float('inf')

    # Pick the right comparison function depending on whose turn it is
    compare = max if XsTurn else min

    # X marks squares with 10, O marks with -10
    points = 10 if XsTurn else -10

    # Loop through all 9 possible squares on the board
    for square in range(9):
        # Work on a copy so we don’t overwrite the real board
        new_board = copy(board)

        # Only play in empty squares (not already 10 or -10)
        if new_board[square] not in (10, -10):
            new_board[square] = points  # Try making this move
            score = calc_score(new_board)  # Check if it makes someone win

            # Base case: if game is over, assign score immediately
            if game_over(new_board):
                # If X wins: score == 30
                # If O wins: score == -30
                # If draw: score == 0
                # Adjust score with 'level' so faster wins = better, slower losses = better
                child_score = (
                    score - level if score == 30 else
                    score + level if score == -30 else
                    0
                )
            else:
                # Recursive case: let the other player make their move
                child_score = mini_max(new_board, not XsTurn, level + 1)

            # Update best_score if this move is better than what we had
            if compare(best_score, child_score) == child_score:
                best_score = child_score

    return best_score
