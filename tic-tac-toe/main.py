#!/usr/bin/python3

from functions1 import *
from functions2 import *


while True:
    board = [' '] * 10
    player1_marker, player2_marker = choose_marker()
    turn = player_turn()
    print(turn + " will go first")

    choice = ''
    while choice not in ['yes', 'no']:
        choice = input("Are you ready to play? Enter Yes or No: ")
    if choice.lower() == 'yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player1':
            board_display(board)
            position = player_choice(board)
            board_marker(board, player1_marker, position)

            if check_win(board, player1_marker):
                board_display(board)
                print("Congratulations! Player1 wins")
                game_on = False
            else:
                if full_board_check(board):
                    board_display(board)
                    print("The game is tied between player1 and player2")
                    game_on = False
                else:
                    turn = 'player2'

        else:
            turn = 'player2'
            board_display(board)
            position = player_choice(board)
            board_marker(board, player2_marker, position)

            if check_win(board, player2_marker):
                board_display(board)
                print("Congratulations! Player2 wins")
                game_on = False
            else:
                if full_board_check(board):
                    board_display(board)
                    print("The game is tied between player1 and player2")
                    game_on = False
                else:
                    turn = 'player1'

    if not replay():
        break
