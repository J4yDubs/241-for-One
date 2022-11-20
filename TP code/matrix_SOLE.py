import math

from matrix_GE import *

# SOLE = System of Linear Equations
# takes in an augmented matrix (with last col being the constants)
# Calls on matrix_GE for REF

def SOLE(inputM):
    rows, cols = len(inputM), len(inputM[0])
    smallestDim = min(rows, cols)
    x = [0]*(cols-1)
    refM = GE(inputM)
    print(refM)
    
    ### Solving here ###
    # check if rows up to smallestDim has pivots
    # store pivot variable and free variable col indices as keys; coefficients
    # as values in dict
    pivots, free = dict(), dict()
    for col in range(smallestDim-1):
        if refM[col][col] != 0:
            pivots[col] = refM[col][col]
        else: free.add(col)
    
    # solving for matrices with no free variables,
    if len(free) == 0:
        x[cols-2]=refM[cols-2][cols-1]/refM[cols-2][cols-2]
        for col in range(cols-3,-1,-1):
            constant = refM[col][cols-1]
            for xCol in range(cols-2, col,-1):
                constant -= x[xCol]*refM[col][xCol]
            x[col] = constant/refM[col][col]
    # create equations automatically
    # create variables that correspond to columns immediately
        
    return x

# def SOLEWithSteps(inputM):

### Testing here ###
M = [[1, -5, 3, -4], [7, 0, -9, 3], [-1, 0, 3, -2]]
print(SOLE(M))
# print(SOLEWithSteps(M))
# M = [[2, 7, 5, 3, 4], [1, 2, 4, 2, 4], [1, 2, 2, 8, 4]]
# # print(rowExchange(M, 1, 0))
# print(GEWithSteps(M))

# M = [[0, 7, 5, 3, 4], [1, 2, 4, 2, 4], [1, 2, 2, 8, 4]]
# print(GEWithSteps(M))

'''
Proposed Improvements:
- Call on GE instead and then store row operations in there to apply to constant
'''