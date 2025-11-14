import globals
from get_adjacent_cells import get_adjacent_cells

'''
First we want to initialize the board. Things to be aware of here are that we need a 3D board. 
We need the 2D rows and columns that the player sees, but we need to have a level deeper, that indicates number,
bomb or blank. We do this by making a row into a list that's as long as the ROWS input, and this list consists of
tuples/sets that will contain the contents of each layer. Layer 0 will be the displayed level, and layer 1 will 
be the hidden one, containing either a number, a bomb or nothing (blank). This list gets repeated for COLS input
amount of times. 

We want to verify the input for the board for certain characteristics. Rows and cols we wanted at least 2, so the 
game can actually be played, and we didn't want more than a 10*10 board, so we put that as max.

For the MINES, the rules were that we wanted at least 1 mine, so it's not just a win on first move, and the amount
of mines couldn't be more than the product of the ROWS and COLS, as it would make the game unplayable.
'''

def initialize_board():
    # ROWS - for all these variables it's important to adapt the global variables.
    prompt_rows = 'Please define number of rows (min. 2 and max. 10): '
    while True:
        try:
            globals.ROWS = int(input(prompt_rows))
            if globals.ROWS < 2 or globals.ROWS > 10:
                raise ValueError
            break
        except ValueError:
            prompt_rows = 'Invalid. Try again (min. 2 and max. 10): '
    
    # COLS
    prompt_cols = 'Please define number of columns (min. 2 and max. 10): '
    while True:
        try:
            globals.COLS = int(input(prompt_cols))
            if globals.COLS < 2 or globals.COLS > 10:
                raise ValueError
            break
        except ValueError:
            prompt_cols = 'Invalid. Try again (min. 2 and max. 10): '
    
    # MINES
    prompt_mines = f'Please define number of mines (1–{globals.ROWS * globals.COLS - 1}): '
    while True:
        try:
            globals.MINES = int(input(prompt_mines))
            if globals.MINES >= globals.ROWS * globals.COLS or globals.MINES < 1:
                raise ValueError
            break
        except ValueError:
            prompt_mines = f'Invalid. Try again (1–{globals.ROWS * globals.COLS - 1}): '

    # Create empty board
    board = [
        [(' ♦', '   ') for _ in range(globals.COLS)] 
        for _ in range(globals.ROWS) #level 0 is the diamond and level 1 is waiting for blank, bomb or number
    ]

    return board #board ready to use for place_random_mines.py 



def is_mine_at(board, row: int, col: int) -> bool:
    """
    Return True iff the hidden/base layer at (row, col) is a mine.
    """
    return board[row][col][1] == '💣'


# ============================
# count_adjacent_mines.py
# ============================

_BLANK = '   '   # 3-space blank to match team formatting

def count_adjacent_mines(board):
    """
    For every NON-mine cell, count the number of adjacent mines and
    write that count into the BASE layer:
      - if count == 0  -> base becomes BLANK ('   ')
      - if count > 0   -> base becomes a 3-wide string like ' 2 '

    Does NOT touch the DISPLAY layer and does NOT modify mine cells.
    Returns the same board object for convenience.
    """
    rows, cols = globals.ROWS, globals.COLS

    for r in range(rows):
        for c in range(cols):
            if is_mine_at(board, r, c):
                continue  # leave mines alone

            # count neighboring mines
            count = sum(1 for nr, nc in get_adjacent_cells(r, c)
                        if is_mine_at(board, nr, nc))

            # update BASE layer with number or blank
            display, _ = board[r][c]
            if count == 0:
                board[r][c] = (display, _BLANK)
            else:
                board[r][c] = (display, f' {count} ')
    return board


# game_won.py


_DIAMOND = ' ♦'  # unrevealed marker on the DISPLAY layer

def game_won(board) -> bool:
    """
    Return True when ALL safe cells have been revealed.
    A cell is "safe" if its BASE is not a mine. We consider the game won
    when there are no unrevealed diamonds over safe cells.

    In other words: for every cell,
      - if base == '💣'  -> ignore
      - else             -> display must NOT be the diamond
    """
    for row in board:
        for display, base in row:
            if base != '💣' and display == _DIAMOND:
                return False
    return True


# get_validated_input.py

HIDDEN_SYMBOL = ' ♦'

def get_validated_input(board):
    """
    Ask the player for a row and column.
    Keep asking until:
    - both are integers
    - inside the board
    - the chosen cell is still hidden
    """
    while True:
        raw = input("Enter row and column (e.g. 1 2): ")
        parts = raw.split()

        # must be exactly two parts
        if len(parts) != 2:
            print("Please enter exactly two numbers.")
            continue

        # both parts must be integers
        try:
            row = int(parts[0])
            col = int(parts[1])
        except ValueError:
            print("Both row and column must be numbers.")
            continue

        # inside board bounds
        if not (0 <= row < globals.ROWS and 0 <= col < globals.COLS):
            print("Out of bounds. Try again.")
            continue

        display, base = board[row][col]

        # must still be hidden
        if display != HIDDEN_SYMBOL:
            print("That cell is already revealed. Pick another.")
            continue

        # valid move
        return row, col
    

# update_board.py
# get_adjacent_cells already imported at the top

HIDDEN_SYMBOL = ' ♦'
BLANK_SYMBOL = '   '   # matches your team's blank base

def update_board(board, start_row, start_col):
    """
    Reveal the chosen cell.
    - If base is a number (like ' 2 '), reveal just that cell.
    - If base is blank ('   '), reveal that blank and
      automatically reveal all connected blanks and bordering numbers.
    Uses a stack (list) instead of recursion.
    """

    stack = [(start_row, start_col)]

    while stack:
        r, c = stack.pop()

        display, base = board[r][c]

        # if already revealed, skip
        if display != HIDDEN_SYMBOL:
            continue

        # if this cell is a number (and not a mine)
        if base != BLANK_SYMBOL and base != '💣':
            # show the number by copying base into display
            board[r][c] = (base, base)
            continue

        # if this cell is blank
        if base == BLANK_SYMBOL:
            # reveal this blank
            board[r][c] = (BLANK_SYMBOL, base)

            # look at neighbors
            for nr, nc in get_adjacent_cells(r, c):
                n_display, n_base = board[nr][nc]

                # only consider hidden, non-mine neighbors
                if n_display == HIDDEN_SYMBOL and n_base != '💣':
                    if n_base == BLANK_SYMBOL:
                        # blank neighbor: push to stack to expand further
                        stack.append((nr, nc))
                    else:
                        # number neighbor: reveal it, but don't expand from it
                        board[nr][nc] = (n_base, n_base)

    return board


# play_minesweeper.py
from place_random_mines import place_random_mines
from print_board import print_board

def reveal_all_mines(board):
    """
    Helper: show all mines when the player loses.
    """
    for r in range(len(board)):
        for c in range(len(board[0])):
            display, base = board[r][c]
            if base == '💣':
                board[r][c] = ('💣', base)

def play_minesweeper():
    # 1. Setup the board
    board = initialize_board()
    place_random_mines(board)
    count_adjacent_mines(board)

    # 2. Main game loop
    while True:
        print_board(board)

        row, col = get_validated_input(board)

        # check if player hit a mine
        if is_mine_at(board, row, col):
            reveal_all_mines(board)
            print_board(board)
            print("You hit a mine. Game over.")
            break

        # reveal safe cells
        update_board(board, row, col)

        # check if player has won
        if game_won(board):
            print_board(board)
            print("You cleared all safe cells. You win.")
            break

if __name__ == "__main__":
    play_minesweeper()