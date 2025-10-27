from utils import clear_screen

def print_board(board: list[int]) -> None:
    """
    Display the Tic-Tac-Toe board.
    Args:
        board: List of 9 integers (10 for X, -10 for O, 1–9 for open).
    """
    def cell(value: int) -> str:
        if value == 10: return 'X'
        elif value == -10: return 'O'
        else: return str(value)

    clear_screen()
    print()

    for row in range(3):
        row_values = [cell(board[row * 3 + col]) for col in range(3)]
        print('   |   |   ')
        print(f' {row_values[0]} | {row_values[1]} | {row_values[2]} ')
        print('   |   |   ')
        if row < 2:
            print('-----------')
    print()
    
from utils import clear_screen
def print_board(board: list[int]):
    """
        Display the Tic-Tac-Toe board with human-friendly layout.
        Remember the board may look like:
        [10, 2, 3, 4, -10, 6, 7, 8, 10] after 3 moves and print_board
        
        X | 2 | 3
        ---------
        4 | O | 6
        ---------
        7 | 8 | X
    """
    
    def cell(value: int) -> str:
        # TODO: Return 'X' if value == 10
        # TODO: Return 'O' if value == -10
        # TODO: Otherwise, return str(value)  -> if not 10 or -10 return idx 1-9 as a string
        pass
        
    clear_screen()
    # TODO: Loop through rows
    # TODO: For each row, print formatted board row using cell()
    # HINT: For each row create a list of what should be printed
    #       row_values = [ 'X', '2', '3' ] call cell() each time to get each value
    #       add the board layout:
    
    #                  |   |          
    #                X | 2 | 3 
    #                  |   |   
    #               -----------
    #                  |   |   
    #                4 | O | 6 
    #                  |   |   
    #               -----------
    #                  |   |   
    #                7 | 8 | X 
    #                  |   |   
    pass
