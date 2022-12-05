from matrix_utils import *

# for outputting matrix with | | (notation for determinant)
def matToDetStr(inputM):
    outputStr = ''
    rows = len(inputM)
    for row in range(rows):
        outputStr += '| ' + str(inputM[row]) + ' |'+'\n'
    return outputStr[:-1]

# determinant via cofactor method; row-wise and choosing (0, 0)th entry
def detCofactor(M):
    rows, cols = len(M), len(M[0])
    det = 0
    # Base case: when a 2x2 matrix is reached
    if len(M) == 2:
        return M[0][0]*M[-1][-1] - M[1][0]*M[0][1]  # ad-bc formula
    # Recursive case
    for j in range(1, cols+1):
        newM = create2DList(rows-1, cols-1)
        for i in range(1, rows):
            for jLeft in range(j-1):
                newM[i-1][jLeft] = M[i][jLeft]
            for jRight in range(j, cols):
                newM[i-1][jRight-1] = M[i][jRight]
        det += M[0][j-1]*detCofactor(newM)*((-1)**(1+j))
    return det

def detCofacWithSteps(M):
    steps = []
    if len(M) == 1: # for 1x1 matrices
        return M[0][0], ['The determinant of 1x1 matrix is the single entry within']
    det = detCofacWithStepsHelper(M, steps)
    steps.append(f'Back-substitute values across every depth to obtain the final value of {det}')
    for i in range(len(steps)):
        if '+' in steps[i]:
            steps[i] = steps[i][:-2]
    print(concatSteps(steps))
    return (det, concatSteps(steps))

def detCofacWithStepsHelper(M, steps, depth=0):
    # stepCount += 1
    rows, cols = len(M), len(M[0])
    det = 0
    # Base case: when a 2x2 matrix is reached
    if len(M) == 2:
        val = M[0][0]*M[-1][-1] - M[1][0]*M[0][1]
        steps.append(f'Depth {depth}:\n{matToDetStr(M)}\n= {M[0][0]}×{M[-1][-1]} - {M[1][0]}×{M[0][1]} = {val}')
        return val  # ad-bc formula
    # Recursive case
    steps.append(f'Depth {depth}:\n{matToDetStr(M)}\n= ')
    for j in range(1, cols+1):
        steps[-1] += (f'(-1)^({1+j})×({M[0][j-1]})×|M{1}{j}|+\n')
    for j in range(1, cols+1):
        newM = create2DList(rows-1, cols-1)
        for i in range(1, rows):
            for jLeft in range(j-1):
                newM[i-1][jLeft] = M[i][jLeft]
            for jRight in range(j, cols):
                newM[i-1][jRight-1] = M[i][jRight]
        # stepCount += 1
        det += M[0][j-1]*detCofacWithStepsHelper(newM, steps, depth+1)*((-1)**(1+j))
    return det

# # testing here
# M = [
#     [1, 2, 3], 
#     [2, 7, 8], 
#     [4, 3, 1]
#     ]
# print(detCofacWithSteps(M))
# print(detCofactor(M))
# print(matToDetStr(M))

# M = [
#     [1, 7, 4, -2, 5], 
#     [4, -2, 3, -8, 1], 
#     [7, 6, -1, 2, 3], 
#     [2, 1, 3, 4, -5], 
#     [1, 0, 1, -1, 2]
# ]
# print(detCofacWithSteps(M))
# print(detCofactor(M))