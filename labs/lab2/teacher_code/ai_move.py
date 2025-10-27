def ai_move(board: list[int]):
    """
    Simple AI that selects the first available cell.
    """
    for move, cell in enumerate(board):
        if abs(cell) != 10:
            return move
           

'''
for cell in board:
    if abs(cell) != 10: boardreturn mark
return None
'''
