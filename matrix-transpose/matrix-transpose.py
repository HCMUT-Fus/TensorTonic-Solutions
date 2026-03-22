import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    nrow = len(A[0])
    ncol = len(A)
    AT = [[0 for j in range(ncol)] for i in range(nrow)]
    for i in range(nrow):
        for j in range(ncol):
            AT[i][j] = A[j][i]
    return np.array(AT)