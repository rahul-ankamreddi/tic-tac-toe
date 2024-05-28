# tic-tac-toe game which can be played on terminal/console.

def check_winner(moves):

    
    
    pass

if __name__=="__main__":
    print("Welcome to Tic-Tac-Toe game:")
    print(''' 
         |     |
         |     |      
         |     |
    `````|`````|`````
         |     |    
         |     |
    `````|`````|`````
         |     |    
         |     | 
 ''',''' 
      02    12    22   

      01    11    21 

      00    10    20 
 ''')
    
    board = [['00',' '],['10',' '],['20',' '],['01',' '],['11',' '],['21',' '],['02',' '],['12',' '],['22',' ']]

    runs = True
    turn = 0

    while runs:
        if turn== 9:
            print("Game ended!!!")
            break

        if turn%2 == 0:
            position = input("Player 'X' Give position : ")
        else:
            position = input("Player 'O' Give position : ")

        if position == 'end':
            break

        for square in board:
            if position == square[0]:
                if square[1] == ' ':
                    if turn%2 == 0:
                        square[1] = "X"
                    else:
                        square[1] = "O"
                    turn = turn + 1
                else:
                    print("\n** Position already filled give another **\n")
                    break
            
                print(f''' 
         |     |
      {board[6][1]}  |  {board[7][1]}  |  {board[8][1]}  
         |     |
    `````|`````|`````
      {board[3][1]}  |  {board[4][1]}  |  {board[5][1]}
         |     |
    `````|`````|`````
      {board[0][1]}  |  {board[1][1]}  |  {board[2][1]}
         |     | 
 ''',''' 
      02    12    22   

      01    11    21 

      00    10    20 
 ''') 
      
        # runs = False

    pass