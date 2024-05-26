
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
 ''')
    
    board = [['00',' '],['01',' '],['02',' '],['10',' '],['11',' '],['12',' '],['20',' '],['21',' '],['22',' ']]

    runs = True
    turn = 0

    while runs:
      #   print("Give position : ")
        position = input("Give position : ")

        for move in board:
            if position == move[0]:
                if turn%2 == 0:
                    move[1] = "X"
                else:
                  move[1] = "O"
                  
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
 ''')
        runs = False
    pass