import math


# Helper function for GE contingent on is number of cols to iterate through 
# based on input matrix geometry (m>n, m<n, m=n); smallest dim is the smallest
# of the two (limiting factor of how many columns to iterate through for elim)

def create2dList(rows, cols):
    return [([0]*cols) for row in range(rows)]

def GEHelper(inputM, smallestDim):    
    pass

def rowExchange(inputM, R1, R2):
    temp = inputM[R2]
    inputM[R2] = inputM[R1]
    inputM[R1] = temp
    return inputM

def pivotIndex(inputM, row):
    count = 0
    for elem in inputM[row]:
        while elem == 0:
            count += 1
    return count-1

# checks if specific column has pivots
def hasPivots(inputM, startRow, col):
    rows = len(inputM)
    for row in range(startRow, rows):
        if inputM[row][col] != 0:
            return True
    return False

def GE(inputM):
    rows = len(inputM)
    cols = len(inputM[0])
    # if rows > cols:
    
    # elif rows < cols:

    # else:
    for col in range(cols-1):   # iterate through all but last col
        if not hasPivots(inputM, col, col): # checks for pivots
            continue
        
        for row in range(col+1, rows):   # iterate through all but first row
            pivot = inputM[col][col]
            if pivot == 0:
                pass
            else:
                pivotRatio = inputM[row][col]/pivot
                for colElim in range(col, cols):
                    # print(inputM)
                    if pivotRatio > 0:  # if both have the same sign
                        inputM[row][colElim] =\
                        inputM[row][colElim] - pivotRatio*inputM[col][colElim]
                    elif pivotRatio < 0:    # if both have different signs
                        inputM[row][colElim] =\
                        inputM[row][colElim] + pivotRatio*inputM[col][colElim]
    return inputM

def doGE():
    rows, cols = None, None
    while not isinstance(rows, int):
        print("Enter the number of rows")
        rows = int(input())
    
    while not isinstance(cols, int):
        print("Enter the number of columns")
        cols = int(input())

    print("Enter your matrix in the format of a list")
    inputM = create2dList(rows, cols)
    for row in range(rows):
        for col in range(cols):
            print(f"Enter the ({row}, {col}) entry")
            inputM[row][col] = int(input())
    
    print(f"Matrix in REF:\n{GE(inputM)}")

    

# issues: what if first row pivot value is 0

M = [[1, 5, 3], [7, 0, 9], [1, 0, 3]]
# print(rowExchange(M, 1, 0))
# print(GE(M))

doGE()