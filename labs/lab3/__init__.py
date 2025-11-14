
# get_validated_input.py
import globals

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
from get_adjacent_cells import get_adjacent_cells

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

    return 

# play_minesweeper.py
from initialize_board import initialize_board
from place_random_mines import place_random_mines
from count_adjacent_mines import count_adjacent_mines
from get_validated_input import get_validated_input
from update_board import update_board
from is_mine_at import is_mine_at
from game_won import game_won
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

if _name_ == "_main_":
    play_minesweeper()

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














# These functions prepare the board before gameplay starts. 
# They don’t reveal cells or handle user input, those tasks are handled in other files. 
# Together they help build the structure the main game loop relies on.
def is_mine_at(board, row: int, col: int) -> bool:
    """
    Return True if the hidden/base layer at (row, col) is a mine.
    """
return board[row][col][1] == '💣'


# count_adjacent_mines.py

_BLANK = '   '   # 3-space blank to match team formatting

def count_adjacent_mines(board):
    """
    For every NON-mine cell, count the number of adjacent mines and
    write that count into the BASE layer:
      - if count == 0  -> base becomes BLANK ('   ')
      - if count > 0   -> base becomes a 3-wide string like ' 2 '

    Doesn’t touch the display layer and doesn’t modify mine cells.
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
_DIAMOND = ' ♦'   # symbol used on the DISPLAY layer for unrevealed cells

def game_won(board) -> bool:
    """
    Return True when ALL safe cells have been revealed.
    A cell is considered safe if its BASE layer is not a mine.
    
    The game is won when there are no diamonds (' ♦') covering safe cells.

    Logic:
      - if base == '💣'  -> ignore (mines do not need to be revealed)
      - else             -> display must NOT still be the diamond symbol
    """
    for row in board:
        for display, base in row:
            # If the BASE layer is safe AND the DISPLAY layer still shows
            # the diamond marker, then this safe cell has not been revealed yet.
            # In this case, the game is not won.
            if base != '💣' and display == _DIAMOND:
                return False

    # If no safe cells are still hidden, the player has won.
    return True



# game_won.py: function looks at every cell on the board and verifies that all safe cells  have been revealed. provides a clear, reusable way to determine when the game should end.

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
