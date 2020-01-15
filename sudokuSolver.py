# print grid
def printBoard(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end=" ")
        print("\n")

# look for empty board spots
def searchForEmptyPosition(board, emptyCell):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if(board[row][col] == 0):
                emptyCell[0] = row
                emptyCell[1] = col
                return True
    return False

# check if number is already in the row
def isInRow(board, row, num):
    for i in range(len(board)):
        if(board[row][i] == num):
            return True
    return False

# check if number is already in the column
def isInColumn(board, col, num):
    for i in range(len(board)):
        if(board[i][col] == num):
            return True
    return False

# check if number is already in box
def isInBox(board, row, col, num):
    for i in range(int(len(board) / 3)):
        for j in range(int(len(board[i]) / 3)):
            if(board[i + row][j + col] == num):
                return True
    return False

# check if location of number is valid
def isValidPosition(board, row, col, num):
    return not isInRow(board, row, num) and not isInColumn(board, col, num) and not isInBox(board, row - row % 3, col - col % 3, num)

# recursively solve the sudoku board
def sudokuSolver(board):
    emptySpot = [0, 0]
    if(not searchForEmptyPosition(board, emptySpot)):
        return True
    row = emptySpot[0]
    col = emptySpot[1]
    for i in range(1, 10):
        if isValidPosition(board, row, col, i):
            board[row][col] = i
            if sudokuSolver(board):
                return True
            board[row][col] = 0
    return False


# unsolved sudoku board
board =[[3,0,6,5,0,8,4,0,0], 
        [5,2,0,0,0,0,0,0,0], 
        [0,8,7,0,0,0,0,3,1], 
        [0,0,3,0,1,0,0,8,0], 
        [9,0,0,8,6,3,0,0,5], 
        [0,5,0,0,9,0,6,0,0], 
        [1,3,0,0,0,0,2,5,0], 
        [0,0,0,0,0,0,0,7,4], 
        [0,0,5,2,0,6,3,0,0]] 

sudokuSolver(board)
printBoard(board)