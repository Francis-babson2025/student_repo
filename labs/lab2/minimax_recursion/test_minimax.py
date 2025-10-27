from copy import copy
from find_move import find_move
from calc_score import calc_score
from game_over import game_over

def play_sequence(board, XsTurn):
    """Play out the game sequence: X moves freely, O uses AI."""
    if game_over(board):
        return calc_score(board)

    if XsTurn:
        results = []
        for square in range(9):
            if board[square] not in (10, -10):
                new_board = copy(board)
                new_board[square] = 10
                results.append(play_sequence(new_board, False))
        # If X can ever force a win, return that
        if 30 in results: return 30
        # If not, but draws exist, return 0
        if 0 in results: return 0
        # Otherwise, X loses
        return -30
    else:
        # O moves optimally using minimax
        move = find_move(board, False)
        if move is None:
            return calc_score(board)
        new_board = copy(board)
        new_board[move] = -10
        return play_sequence(new_board, True)


def exhaustive_test():
    board = [i for i in range(9)]  # empty board
    
    # Case 1: X goes first
    result = play_sequence(board, True)
    if result == 30:
        print("BUG: X can beat the AI (X first)")
    elif result == -30:
        print("BUG: AI beats perfect X (X first, shouldn’t happen)")
    else:
        print("X first: always a draw with perfect play.")

    # Case 2: O goes first
    move = find_move(board, False)  # AI makes the opening move
    new_board = copy(board)
    new_board[move] = -10
    result = play_sequence(new_board, True)
    if result == 30:
        print("BUG: X can beat the AI (O first)")
    elif result == -30:
        print("BUG: AI beats perfect X (O first, shouldn’t happen)")
    else:
        print("O first: always a draw with perfect play.")


if __name__ == "__main__":
    exhaustive_test()
