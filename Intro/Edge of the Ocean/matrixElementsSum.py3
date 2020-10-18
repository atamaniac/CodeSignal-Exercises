import numpy as np

def matrixElementsSum(matrix):
    idxs = []
    columns = len(matrix[0])
    rows = len(matrix)
    for j in range(rows-1):
        for k in range(columns):
            if matrix[j][k]==0:
                matrix[j+1][k]=0
    A=np.array(matrix).flatten()
    counter = 0
    for k in range(len(A)):
        if A[k] != 0:
            counter += A[k]
    return counter
