import math

def create2DList(rows, cols):
    return [([0]*cols) for row in range(rows)]

def rowExchange(inputM, R1, R2):
    temp = inputM[R2]
    inputM[R2] = inputM[R1]
    inputM[R1] = temp
    return inputM

def matAdd(M1, M2):
    rows, cols = len(M1), len(M1[0])
    if rows != len(M2) or cols != len(M2[0]):
        return "Matrix dimension mismatch!"

    sum = create2DList(rows, cols)
    for row in range(rows):
        for col in range(cols):
            sum[row][col] = M1[row][col] + M2[row][col]
    return sum

def matAddWithSteps(M1, M2):
    pass

def matMulHelper(M1, M2, row, col):
    cols = len(M1[0])
    entry = 0
    for k in range(cols):
        entry += M1[row][k] * M2[k][col]
    return entry

def matMul(M1, M2):
    rows1, cols1 = len(M1), len(M1[0])
    rows2, cols2 = len(M2), len(M2[0])
    if cols1 != rows2:
        return "Matrix dimension mismatch!"
    
    prodM = create2DList(rows1, cols2)
    for row in range(rows1):
        for col in range(cols2):
            prodM[row][col] += matMulHelper(M1, M2, row, col)
    
    return prodM

def matMulWithSteps(M1, M2):
    pass

# testing if matMul works
M1 = [[1, 7, 4, 2], [2, 3, 3, 3], [2, 8, 5, 3]]
M2 = [[1, 3, 0], [4, 2, 1], [3, 7, 5], [2, 4, 4]]
print(matMul(M1, M2))