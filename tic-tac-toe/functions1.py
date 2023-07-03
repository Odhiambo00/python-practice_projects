#!/usr/bin/python3

import random
from functions2 import *

'''Initialize game board with a list'''

board = [' '] * 10


def board_display(board):
    '''Displays the board where the game will be played'''
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')


def player_turn():
    '''Determines whose turn it is to play'''

    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'


def choose_marker():
    '''Determines players' markers either X or O'''

    marker = ''

    while not (marker == 'X' or marker == 'O'):
        print("You have two choices: X or O")
        marker = (input("Player 1: Do you want to be X or O? ")).upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print(f"player1 you'll be {player1} and player2 you'll be {player2}")
    return (player1, player2)


def player_choice(board):
    '''Determines position a player wants to place their marker'''

    position = 0
    position_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while position not in position_list or not space_check(board, position):
        position = int(input("Choose position to place your marker:(1-9) "))

        if position < 0:
            position = position * (-1)

    return position


def board_marker(board, position, marker):
    '''updates player's choice with their marker on the board'''

    board[position] = marker
