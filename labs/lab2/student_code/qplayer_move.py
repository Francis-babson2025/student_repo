    
def player_move(board: list[int], score: dict[str, int]):
    """
        Prompts the player to choose a valid move.
        Remember score is a dictionary from play_game()
        It has two keys 'player' and 'ai' associated values
        are 10 and -10 depending on who goes first.
    """
    
    prompt = "Select an empty cell (1-9): "
    while True:
        try:
            # TODO: Convert input to integer
            # TODO: Validate move is in range and not taken
            pass
        except ValueError:
            prompt = "Invalid input. Try again (1-9): "
            
    # TODO: Assign score['player'] to the selected cell on the board
    # HINT: remember the board moves are 1 - 9 but the board indices are
    # 0 - 8
pass
