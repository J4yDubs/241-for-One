from matrix_utils import *

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

# # testing here
# M = [
#     [1, 2, 3], 
#     [2, 7, 8], 
#     [4, 3, 1]
#     ]
# print(detCofactor(M))

# M = [
#     [1, 7, 4, -2, 5], 
#     [4, -2, 3, -8, 1], 
#     [7, 6, -1, 2, 3], 
#     [2, 1, 3, 4, -5], 
#     [1, 0, 1, -1, 2]
# ]
# print(detCofactor(M))