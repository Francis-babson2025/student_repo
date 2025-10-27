from display_board import print_board

from game_over import game_over
from calc_score import calc_score

from player_move import player_move
from ai_move import ai_move

from utils import clear_screen
import time


def play_game():
    score = {'player': 10, 'ai': -10}
    playerTurn = True
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player_win = 30

    clear_screen()

    ai_name = 'Big Mean Machine'
    player_name = input('Please enter your name: ')

    txt = 'Who plays first (1/you, 2/computer)? '
    while True:
        try:
            first_to_play = int(input(txt))
            if first_to_play not in (1, 2):
                raise ValueError
            break
        except ValueError:
            txt = 'Please enter 1 or 2 '

    if first_to_play == 2:
        score['player'], score['ai'] = score['ai'], score['player']
        playerTurn = True
        player_win = -30

    while not game_over(board):

        print_board(board)

        if playerTurn:

            print(f'{player_name} moves')

            player_move(board, score)
        else:
            print(f'{ai_name} moves')
            time.sleep(2)

            # move = find_move(board, playerTurn)
            move = ai_move(board)
            board[move] = score['ai']

        playerTurn = not playerTurn

    print_board(board)
    score = calc_score(board)

    if score == player_win:
        print(f'Congratulations {player_name}, you beat me. Big Deal \n')
    elif score == -player_win:
        print(f'I WON! I WON! the {ai_name} WON!! \n')
    else:
        print("It's a tie", '\n')


play_game()
