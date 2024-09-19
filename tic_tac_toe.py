"""A Tic Tac Toe game written in python"""

from random import randint
def display_board(board):
    """Display the board"""

    print(f'| {board[6]} | {board[7]} |  {board[8]} |')
    print("-"*13)
    print(f'| {board[3]} | {board[4]} |  {board[5]} |')
    print("-"*13)
    print(f'| {board[0]} | {board[1]} |  {board[2]} |')
    print("_"*13)

def pawn_choices():
    """Player 1 should choose his pawn """

    pawn = ''

    while pawn not in ['X', 'O']:
        pawn = input('Player1: choose  X or O : ').upper()

    if pawn == 'X':
        return {'player_1': 'X', 'player_2': 'O'}

    return {'player_1': 'O', 'player_2': 'X'}


def space_check(board, position):
    """Check if choosed position is free """

    return board[position] == ' '

def full_board_checked(board):
    """Check if all postions are already played """

    for index in range(0,9):
        if space_check(board, index):
            return False
    return True


def player_choice(board):
    """The player enter his choice"""

    position = 9

    while position not in range(0,9) or not space_check(board, position):
        position = int(input('Choose a position: (0-8) '))

    return position

def play_again():
    """Ask players if the want to play again"""

    choice = ''

    while choice.capitalize() not in ['Yes', 'No']:
        choice = input('Want to play again? : Yes or No \n')
    return choice

def define_turn():
    """Define randomly who is going to play first"""

    turn = randint(0,1)

    if turn == 0:
        return 'player_1'
    return 'player_2'

def  win_check(board):
    """Check if the player has win or not"""
    patterns = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

    for x,y,z in patterns:
        data = ''.join([board[x],board[y],board[z]])
        if data in ['XXX', 'OOO']:
            return (True, f'{board[x]} win!')
    return (False, '')



def main_game():
    """Main Game"""

    print('Welcome to Tic Tac Toe game')
    play = 'Yes'

    while play == 'Yes':
    # Set EveryThing up
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        choices = pawn_choices()
        # Choose who is gone first
        player_turn=define_turn()
        #Game play
        game_on = True
        display_board(board)
        while game_on:
            # current player place his pawn
            print(f'current_player : {player_turn}')
            position = player_choice(board)
            if  player_turn == 'player_1':
                board[position] = choices['player_1']
                player_turn = 'player_2'
            else:
                board[position] = choices['player_2']
                player_turn = 'player_1'
            # decide if the game should continue or not
            display_board(board)
            (win, msg) = win_check(board)
            if win:
                print(f'congrats! {msg}')
                game_on = False
            else:
                if full_board_checked(board):
                    print('Game Tie!')
                    game_on = False

    # ASK if gamers want to reply
        if play_again() == 'No':
            break


if __name__ == "__main__":
    main_game()
else:
    print("this app use tic_tac_toe packages")
