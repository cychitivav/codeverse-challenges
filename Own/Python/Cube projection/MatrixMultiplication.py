def matmul(a, b):
    rowsA, colsA = len(a), len(a[0])
    rowsB, colsB = len(b), len(b[0])
    if colsA != rowsB:
        raise ValueError("Columns of A must match rows of B")

    return [[sum(a[i][k] * b[k][j] for k in range(colsA))
             for j in range(colsB)] for i in range(rowsA)]


def logMatrix(m):
    rows = len(m)
    for i in range(rows):
        print(m[i])

def matsum(a, b):
    rowsA, colsA = len(a), len(a[0])
    rowsB, colsB = len(b), len(b[0])
    if rowsA != rowsB or colsA != colsB:
        raise ValueError("A and B must be of the same dimension")

    return [[a[i][k] + b[i][k] for k in range(colsA)] for i in range(rowsA)]


def vecToMatriz(v):
    matrix = []
    for i in range(len(v)):
        matrix.append([v[i]])
    return matrix


def matrixToVec(m):
    vector = []
    vector.extend(m[0])
    vector.extend(m[1])
    vector.append(0)
    
    return vector

