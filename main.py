# tic-tac-toe game which can be played on terminal/console.

import random


def display_board(board):
    print(f'''
             |     |
          {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}
             |     |    
        `````|`````|`````
          {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}
             |     |    
        `````|`````|`````
          {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}
             |     |

''')


def select_symbol(symbols):
    while True:
        s = input(f"Choose a symbol from {[symbol for symbol in symbols]} : ")
        if s in symbols:
            break
        else:
            print("\n!!!  Invalid symbol  !!!\n")
    symbols.remove(s)
    return s


def get_move(list_of_moves):
    valid = False
    while not valid:
        move = input("Give valid move: ")
        if move in list_of_moves:
            valid = True
            list_of_moves.remove(move)
        else:
            print("Give valid move")
    return move


def get_cpu_move(list_of_moves):
    if len(list_of_moves) != 0:
        move = random.choice(list_of_moves)
        list_of_moves.remove(move)
    else:
        move = None
    return move


def check_winning_condition(board, player):
    flag = True
    for row in board:
        if (row[0] == row[1] == row[2] == player):
            flag = False
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i] == player):
            flag = False
    if (board[0][0] == board[1][1] == board[2][2] == player):
        flag = False
    if (board[2][0] == board[1][1] == board[0][2] == player):
        flag = False

    if not flag:
        print(f"\n***  Player {player} won!!  **\n")
    return flag


def make_move(board, player, move):
    if move != None:
        i, j = map(int, move)
        board[i][j] = player
    else:
        print("\n*** No moves left ***\n")


if __name__ == "__main__":

    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    list_of_moves = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    list_of_symbols = ['x', 'o']

    print("\n**  Welcome to tic-tac-toe game  **\n")
    print(''' 
    Rules:
    ``````
        1. Give position of the move as '01', where, 1st digit is row and 2nd is column
        2. Top-left corner is '00'
''')

    player_1 = select_symbol(list_of_symbols)
    player_2 = list_of_symbols.pop()

    runs = True
    turn = 0

    display_board(board)

    while runs:
        if turn % 2 == 0:
            player = player_1
        else:
            player = player_2

        if player == player_1:
            move = get_move(list_of_moves)
            make_move(board, player, move)
            runs = check_winning_condition(board, player)
            display_board(board)

        if player == player_2:
            print("CPU makes a move...")
            move = get_cpu_move(list_of_moves)
            make_move(board, player, move)
            runs = check_winning_condition(board, player)
            display_board(board)

        turn = turn + 1
