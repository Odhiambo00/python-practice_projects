#!/usr/bin/python3

from functions1 import *
from functions2 import *

print("Welcome to Tic Tac Toe")

while True:
    board = [' '] * 10
    player1_marker, player2_marker = choose_marker()
    turn = player_turn()
    print(turn + " will go first.")

    play_game = input("Are you ready to play? Enter Yes or No: ")

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        #player1's turn
        if turn == 'player1':
            board_display(board)
            position = player_choice(board)
            board_marker(board, position, player1_marker)

            if check_win(board, player1_marker):
                board_display(board)
                print("Congratulations! Player1 won the game!")
                game_on = False
            else:
                if full_board_check(board):
                    board_display(board)
                    print("No winner! The game is a draw!")
                    game_on = False
                else:
                    turn = 'player2'

        else:
            #player2's turn
            board_display(board)
            position = player_choice(board)
            board_marker(board, position, player2_marker)

            if check_win(board, player2_marker):
                board_display(board)
                print("Congratulations! Player2 won the game!")
                game_on = False
            else:
                if full_board_check(board):
                    board_display(board)
                    print("No winner! The game is a draw!")
                    game_on = False
                else:
                    turn = 'player1'

    if not replay():
        break
