#board = [   [0,5,0,3,1,4,0,6,0],
  #          [8,7,0,0,0,9,4,0,3],
   #         [6,4,3,5,0,7,1,9,2],
    #        [0,0,7,8,0,5,2,1,0],
     #       [4,1,0,9,0,0,0,0,0],
      #      [0,2,5,0,6,1,9,0,7],
       #     [7,9,0,2,5,0,8,4,0],
        #    [0,0,4,0,9,6,0,0,5],
         #   [0,3,0,1,0,8,6,7,0]
        #]
#Function to print the board
def print_board(bo):
    for i in range(len(bo)):
        if i%3==0:
            print(" - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if(j%3==0):
                print("|",end="")
            
            print(bo[i][j],end = " ")
        print("")
#function to find empty values in the board
def empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if(bo[i][j]==0):
                return (i,j)
    
    return (-1,-1)

def valid(bo,row,col,value):
    print_board(bo)
    #checking row
    for j in range(len(bo[0])):
        if(bo[row][j] == value):
            return False
    
    #checking column

    for i in range(len(bo)):
        if(bo[i][col] == value):
            return False
    
    #check box

    box_x = row//3
    box_y = col//3

    for i in range(3):
        for j in range(3):
            if(bo[box_x*3+i][box_y*3+j]==value):
                return False

    return True
#Verifying valid function
#if(valid(board,7,2,9)):
#   print("Valid")
#else:    
#    print("Not valid")
    
    
def solve(bo):
    tup = empty(bo)
    if(tup==(-1,-1)):
        print("Sudoku completed")
        return True
    else:
        for i in range(1,10):
            if(valid(bo,tup[0],tup[1],i)):
                bo[tup[0]][tup[1]] = i
        
                if(solve(bo)):
                    return True

        bo[tup[0]][tup[1]] = 0
        return False    
def finished(bo):
    for i in range(9):
        for j in range(9):
            if(bo[i][j]==0):
                return False
    return True
#main function for function call
#if __name__=="__main__":
#    print_board(board)
#   solve(board)
#   print_board(board)