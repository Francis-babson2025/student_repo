"""
Tic-Tac-Toe Game
---------------
This program implements a two-player Tic-Tac-Toe game where the player competes 
against an AI opponent.

Board Representation:
    The board is a list of 9 integers:
        - 10   ? First Player's move (X)
        - -10  ? Second Player's move (O)
        - 1-9  ? Unclaimed squares (used for display and input)

Scoring:
    - First Player win  ? +30
    - Second Player win ? -30
    - Tie               ? 0

Imported Functions:
    - print_board(board): Displays the board in a human-friendly format.
    - game_over(board): Returns True if the game has a winner or no moves remain.
    - calc_score(board): Returns 30 if first player wins, -30 if second player wins, else 0.
    - player_move(board, score): Prompts the player for a move and updates the board.
    - ai_move(board): Chooses a random available move (used in easy mode).
    - find_move(board, playerTurn): Uses minimax to find the best AI move (hard mode).
    - clear_screen(): Clears the terminal for a cleaner display.
"""
import sys
import time
from utils import clear_screen
import importlib.util
from pathlib import Path


def import_module(name):
    """
    Imports a module from student_code/*.py if it exists,
    otherwise loads default_code/*.pyc directly.
    """
    base_dir = Path(__file__).parent.resolve()
    student_py = base_dir / f"{name}.py"
    default_pyc = base_dir.parent / "default_code" / f"{name}.pyc"

    if student_py.exists():
        spec = importlib.util.spec_from_file_location(name, student_py)
    elif default_pyc.exists():
        spec = importlib.util.spec_from_file_location(name, default_pyc)
    else:
        raise ImportError(
            f"Module '{name}' not found in student_code or default_code.")

    module = importlib.util.module_from_spec(spec)

    import sys
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


print_board = import_module("display_board").print_board
game_over = import_module("game_over").game_over
calc_score = import_module("calc_score").calc_score
player_move = import_module("player_move").player_move
ai_move = import_module("ai_move").ai_move
find_move = import_module("find_move").find_move
mini_max = import_module("find_move").mini_max
clear_screen = import_module("utils").clear_screen


def play_game():
    """
    Runs a full game of Tic-Tac-Toe between the player and the AI.
    """

    # Mapping used to mark player and AI moves on the board.
    # First Player uses +10, Second Player uses -10.
    score = {'player': 10, 'ai': -10}  # defualt human goes first

    # Tracks whose turn it is. True = player's turn, False = AI's turn.
    playerTurn = True  # default

    # Initialize an empty board: numbers 1-9 represent available spaces.
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # The "player_win" variable stores the winning score used for comparisons later.
    # By default, 30 means the player wins.
    player_win = 30

    # Set difficulty: False = easy (random AI), True = hard (minimax AI).
    play_hard = False  # TODO: Change to False once ai_move.py is ready.

    # Clear the screen to start fresh.
    clear_screen()

    # Get player name and assign AI name.
    ai_name = 'Big Mean Machine'
    player_name = input('Please enter your name: ')

    sys.stdout.flush()

    # Ask who plays first: 1 = player, 2 = computer.
    txt = 'Who plays first (1/you, 2/computer)? '
    while True:
        try:
            first_to_play = int(input(txt))
            # Input must be 1 or 2 only.
            if first_to_play not in (1, 2):
                raise ValueError
            break
        except ValueError:
            # If invalid input, ask again.
            txt = 'Please enter 1 or 2 '

    # If the AI plays first, swap scoring roles and set playerTurn to False.
    if first_to_play == 2:
        score['player'], score['ai'] = score['ai'], score['player']
        playerTurn = False
        player_win = -30  # Winning score reversed if AI goes first.

    # Main game loop: continues until game_over(board) returns True.
    while not game_over(board):
        # Show the current board.
        print_board(board)

        if playerTurn:
            # Player's turn: prompt for move.
            print(f"{player_name} moves")
            player_move(board, score)
        else:
            # AI's turn.
            print(f"{ai_name} moves")
            time.sleep(2)  # Add delay for dramatic effect.

            # Choose AI move: hard mode uses minimax, easy mode uses random.
            if play_hard:
                move = find_move(board, playerTurn)
            else:
                move = ai_move(board)

            # Mark AI's move on the board.
            board[move] = score['ai']

        # Switch turns.
        playerTurn = not playerTurn

    # Game over: display final board state.
    print_board(board)

    # Calculate final score.
    score = calc_score(board)

    # Display result.
    if score == player_win:
        print(f"Congratulations {player_name}, you beat me. Big Deal!\n")
    elif score == -player_win:
        print(f"I WON! I WON! The {ai_name} WON!!\n")
    else:
        print("It's a tie!\n")
