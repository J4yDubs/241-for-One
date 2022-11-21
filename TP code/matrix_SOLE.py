import math

from matrix_GE import *

# SOLE = System of Linear Equations
# takes in an augmented matrix (with last col being the constants)
# Calls on matrix_GE for REF

def isConsistent(refM):
    rows, cols = len(refM), len(refM[0])
    if refM[rows-1][cols-1] == 0:
        return True
    for col in range(cols-1):
        if refM[rows-1][col] != 0:
            return True
    return False

def SOLE(inputM):
    rows, cols = len(inputM), len(inputM[0])
    smallestDim = min(rows, cols-1)
    refM = GE(inputM)
    # print(refM)     #*

    # Case 1: No solutions (checks last row if all 0s but has non-zero constant term)
    if not isConsistent(refM):
        return f"Reduced system {refM} is inconsistent! \n{inputM} has no solutions!"
    
    ### Solving here ###
    # check if rows up to smallestDim has pivots
    # store pivot variable and free variable col indices
    pivots, freeVars = [], []
    for col in range(cols-1):
        if col < rows and refM[col][col] != 0:
                pivots.append(col)
    for col in range(cols-1):
        if col not in pivots:
            freeVars.append(col)

    # print(pivots, freeVars) #*
    
    # Case 2: Unique solution; no free variables (freeVars)
    if len(freeVars) == 0:
        x = [0]*(cols-1)
        x[cols-2]=refM[cols-2][cols-1]/refM[cols-2][cols-2]
        for col in range(cols-3,-1,-1):
            constant = refM[col][cols-1]
            for xCol in range(cols-2, col,-1):
                constant -= x[xCol]*refM[col][xCol]
            x[col] = constant/refM[col][col]
        return x
    
    # Case 3: Special solutions
    x = create2DList(len(freeVars), cols-1)
    for solNum in range(len(freeVars)):
        for freeV in freeVars:
            x[solNum][freeV] = 1    # setting one of the free variables to one
            freeVars.remove(freeV)
            break
        xRow = x[solNum]
        for pivotIndex in range(len(pivots)-1, -1, -1):
            constant = refM[pivots[pivotIndex]][cols-1]
            for xCol in range(cols-2, pivots[pivotIndex],-1):
                constant -= xRow[xCol]*refM[pivots[pivotIndex]][xCol]
            xRow[pivots[pivotIndex]] = constant/refM[pivots[pivotIndex]][pivots[pivotIndex]]
    return x

# def SOLEWithSteps(inputM):

### Testing here ###

# # unique solution
# M = [[1, -5, 3, -4], [7, 0, -9, 3], [-1, 0, 3, -2]]
# print(SOLE(M))

# # infinite solutions (dim(N(M)) = 1)
# M = [[1, 2, 3, 0], [4, 5, 6, 0], [7, 8, 9, 0]]
# print(SOLE(M))

# # infinite solutions (dim(N(M)) = 3)
# M = [[1, 2, 3, 4, 2, 2], [1, 3, 2, 6, 4, 7], [1, 2, 2, 3, 2, 4]]
# print(SOLE(M))

# # infinite solutions (dim(N(M)) = 
# M = \
# [[3, 2, 3, 4, 2, 2, 7, 2],
# [1, 2, 7, 6, 4, 5, 2, 3],
# [4, 2, 2, 3, 2, 4, 6, 1],
# [4, 5, 6, 2, 3, 1, 4, 0]]
# print(SOLE(M))

M = [[2, 3, -2, 6, 0], [0, 0, 3, -6, 0], [1, 0, 2, -3, 0]]
print(SOLE(M))

# print(SOLEWithSteps(M))
# M = [[2, 7, 5, 3, 4], [1, 2, 4, 2, 4], [1, 2, 2, 8, 4]]
# # print(rowExchange(M, 1, 0))
# print(GEWithSteps(M))

# M = [[0, 7, 5, 3, 4], [1, 2, 4, 2, 4], [1, 2, 2, 8, 4]]
# print(GEWithSteps(M))

'''
Proposed Improvements:
- Store row operations in there to apply to constant on right?
- Detect is system is inconsistent (no solutions)
'''