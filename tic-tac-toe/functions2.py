#!/usr/bin/python3

def space_check(board, position):
    '''checks if there's empty space in the board'''

    return board[position] == ' '


def full_board_check(board):
    '''checks if board is full'''

    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def check_win(board, marker):
    '''checks if there's a winning combination on the board'''

    return ((board[7] == marker and board[8] == marker and board[9] == marker)
            or (board[4] == marker and board[5] == marker and board[6] ==
                marker) or (board[1] == marker and board[2] == marker and
            board[3] == marker) or (board[7] == marker and board[4] ==
            marker and board[1] == marker) or (board[8] == marker
            and board[5] == marker and board[2] == marker) or
            (board[9] == marker and board[6] == marker and
            board[3] == marker) or (board[7] == marker and
            board[5] == marker and board[3] == marker) or
            (board[9] == marker and board[5] == marker and board[1] == marker))


def replay():
    choice = ''

    while choice not in ['yes', 'no']:
        print("Pick Yes or No")
        choice = (input("Do you want to play again? Enter Yes or No: ")).lower()

    if choice.lower()[0] == 'y':
        return True
    else:
        return False
