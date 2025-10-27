def calc_score(board):
    """
    Determines if there's a winner on the board.
    Returns 'X', 'O', or 'Tied Game' if all cells are filled.
    """
    def line_sum(a, b, c):
        s = board[a] + board[b] + board[c]
        if s == 30: return 30
        elif s == -30: return -30
        return 0

    # Check rows and columns
    for i in range(3):
        score = line_sum(i*3, i*3+1, i*3+2)  # Rows
        if score in(30, -30): return score

        score = line_sum(i, i+3, i+6)        # Columns
        if score in(30, -30): return score

    # Check diagonals
    for indices in [(0, 4, 8), (2, 4, 6)]:
        score = line_sum(*indices)
        if score in(30, -30): return score

    return 0

