from calc_score import calc_score


def game_over(board):
    """
    Returns True if the game has a winner or no remaining moves.
    """
    all_filled = all(abs(cell) == 10 for cell in board)
    return all_filled or calc_score(board) in (30, -30)


'''
all_filled = True
for cell in board:
   if abs(cell) != 10: 
       all_filled = False
       break
return all_filled or check_winner(board) in ('X', 'O')

'''
