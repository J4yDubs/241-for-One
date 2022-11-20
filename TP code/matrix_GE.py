import math

from matrix_utils import *

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

# does Gaussian elimination and works for square and non-square matrices
# this is a helper function for other math functions
def GE(inputM):
    rows = len(inputM)
    cols = len(inputM[0])
    smallestDim = min(rows, cols)   # iterates n-1 times; where n is the 
    # smallest dimension

    for col in range(smallestDim-1):   # iterate through all but last col
        if not hasPivots(inputM, col, col): # checks for pivots
            continue
        for row in range(col+1, rows):   # iterate through all but first row
            pivot = inputM[col][col]

            # row exchange implemented below if pivot found to be 0
            if pivot == 0:
                for pivotRow in range(col+1, rows): # searches for next non-zero pivot
                    if inputM[pivotRow][col] != 0:
                        rowExchange(inputM, col, pivotRow)
                pivot = inputM[col][col]    # reassigns new pivot value
            
            pivotRatio = inputM[row][col]/pivot
            for colElim in range(col, cols):
                if pivotRatio > 0:  # if both have the same sign
                    inputM[row][colElim] =\
                    inputM[row][colElim] - pivotRatio*inputM[col][colElim]
                else:    # if both have different signs
                    inputM[row][colElim] =\
                    inputM[row][colElim] + abs(pivotRatio)*inputM[col][colElim]
    return inputM

# Same as GE function above but displays steps
def GEWithSteps(inputM):
    rows = len(inputM)
    cols = len(inputM[0])
    smallestDim = min(rows, cols)   # iterates n-1 times; where n is the 
    # smallest dimension
    stepCount = 1

    for col in range(smallestDim-1):   # iterate through all but last col
        if not hasPivots(inputM, col, col): # checks for pivots in the col
            continue
        for row in range(col+1, rows):   # iterate through all but first row
            pivot = inputM[col][col]

            # row exchange implemented below if pivot found to be 0
            if pivot == 0:
                for pivotRow in range(col+1, rows): # searches for next non-zero pivot
                    if inputM[pivotRow][col] != 0:
                        rowExchange(inputM, col, pivotRow)
                print(f"***Step {stepCount}*** R{col+1} <-> R {pivotRow+1}")
                print(f"Intermediate output: {inputM}\n")
                stepCount += 1
                pivot = inputM[col][col]    # reassigns new pivot value

            pivotRatio = inputM[row][col]/pivot
            for colElim in range(col, cols):
                if pivotRatio > 0:  # if both have the same sign
                    inputM[row][colElim] =\
                    inputM[row][colElim] - pivotRatio*inputM[col][colElim]
                else:    # if both have different signs
                    inputM[row][colElim] =\
                    inputM[row][colElim] + abs(pivotRatio)*inputM[col][colElim]
            if pivotRatio > 0:
                print(f"***Step {stepCount}*** \nR{row+1} -> R{row+1} - {pivotRatio}×R{col+1}")
            else:
                print(f"***Step {stepCount}*** \nR{row+1} -> R{row+1} + {abs(pivotRatio)}×R{col+1}")     
            print(f"Intermediate output: {inputM}\n")
            stepCount += 1
    return f"------------------\n***FINAL RESULT*** {inputM}\n------------------\n"

def RREF(inputM):
    refM = GE(inputM)
    rows = len(inputM)
    cols = len(inputM[0])
    smallestDim = min(rows, cols)

    for row in range(rows):
        for col in range(cols):
            if refM[row][col] != 0:
                pivot = refM[row][col]
                break
        for col in range(cols):
            refM[row][col] /= pivot
    return refM

# function that calls GE with terminal interface
def doGE():
    rows, cols = None, None
    while not isinstance(rows, int):
        print("Enter the number of rows")
        rows = int(input())
    
    while not isinstance(cols, int):
        print("Enter the number of columns")
        cols = int(input())

    print("***Enter the matrix entries below***")
    inputM = create2DList(rows, cols)
    for row in range(rows):
        for col in range(cols):
            print(f"Enter the ({row}, {col}) entry")
            inputM[row][col] = int(input())
    
    print(f"Matrix in REF:\n{GE(inputM)}")


# test matrices below

# M = [[1, -5, 3], [7, 0, -9], [-1, 0, 3]]    # tricky, requires row exchange
# print(GEWithSteps(M))
# M = [[2, 7, 5, 3, 4], [1, 2, 4, 2, 4], [1, 2, 2, 8, 4]]
# print(GEWithSteps(M))

# M = [[0, 7, 5, 3, 4], [1, 2, 4, 2, 4], [1, 2, 2, 8, 4]]
# print(GEWithSteps(M))
# print(GE(M))

# M = \
# [[3, 2, 3, 4, 2, 2, 7, 2],
# [1, 2, 7, 6, 4, 5, 2, 3],
# [4, 2, 2, 3, 2, 4, 6, 1],
# [4, 5, 6, 2, 3, 1, 4, 0]]
# print(GEWithSteps(M))
# print(RREF(M))

# # doGE()    # run this if you want to enter matrices dynamically

'''
Proposed improvements:
- Display fractions instead of ints (detect fraction based on modulo of 1)
- If fractions not possible, then use rounding
'''