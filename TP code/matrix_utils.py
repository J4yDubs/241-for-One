import math

def mean(x,y):
    return (x+y)/2

def create2DList(rows, cols):
    return [([0]*cols) for row in range(rows)]

def roundOff(entry):
    return float("%.2f" % entry)

def roundOffEntries(M):
    # if 2D
    if isinstance(M[0], list):
        rows, cols = len(M), len(M[0])
        for row in range(rows):
            for col in range(cols):
                M[row][col] = float("%.2f" % M[row][col])
    else: # if 1D
        cols = len(M)
        for col in range(cols):
            M[col] = float("%.2f" % M[col])
    return M

# to convert list into str (to display each row on a separate line)
def matToStr(inputM):
    outputStr = ''
    rows = len(inputM)
    for row in range(rows):
        outputStr += str(inputM[row])+'\n'
    return outputStr[:-1]

# to concatenate a list of steps into a single string and separating each step with a new line
def concatSteps(steps):
    stepsConcat = ''
    for step in steps:
        stepsConcat += step + '\n\n'
    return stepsConcat

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
    
    return roundOffEntries(prodM)

def matMulWithStepsHelper(M1, M2, row, col):
    cols = len(M1[0])
    entry = 0
    products = []
    for k in range(cols):
        entry += M1[row][k] * M2[k][col]
        products.append((M1[row][k], M2[k][col]))
    return (entry, products)

def matMulWithSteps(M1, M2):
    rows1, cols1 = len(M1), len(M1[0])
    rows2, cols2 = len(M2), len(M2[0])
    if cols1 != rows2:
        return "Matrix dimension mismatch!"
    
    stepCount = 1
    
    prodM = create2DList(rows1, cols2)
    steps = []
    for row in range(rows1):
        for col in range(cols2):
            productStr = ''
            prodM[row][col] += matMulWithStepsHelper(M1, M2, row, col)[0]
            products = matMulWithStepsHelper(M1, M2, row, col)[1]
            for product in products:
                productStr += str("%.2f" % product[0])+'×'+str("%.2f" % product[1])+' + '
            steps.append(f'Step {stepCount}:\n({row+1}, {col+1}) entry = {productStr[:-2]}\n= {prodM[row][col]}')
            # print(steps[-1])
            stepCount += 1
    steps.append(f'Matrix Product:\n{matToStr(roundOffEntries(prodM))}')
    return roundOffEntries(prodM), steps

def matTpose(inputM):
    rows = len(inputM)
    cols =  len(inputM[0])
    tposeM = create2DList(cols, rows)
    for row in range(rows):
        for col in range(cols):
            tposeM[col][row] = inputM[row][col]
    return tposeM


# testing functions below

# M1 = [[1, 7, 4, 2], [2, 3, 3, 3], [2, 8, 5, 3]]
# M2 = [[1, 3, 0], [4, 2, 1], [3, 7, 5], [2, 4, 4]]
# print(matMul(M1, M2))
# print(matMulWithSteps(M1, M2))

# print(matTpose(M1))
# print(matTpose(M2))