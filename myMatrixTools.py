def diagonal(a):
    diag = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[i])):
            print(a[i][j])
            if i == j:
                row.append(a[i][j])
            else:
                row.append(0)
        diag.append(row)
    return diag


def upper(a):
    upp = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[i])):
            if j > i:
                row.append(a[i][j])
            else:
                row.append(0)
        upp.append(row)
    return upp


def lower(a):
    low = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[i])):
            if i > j:
                row.append(a[i][j])
            else:
                row.append(0)
        low.append(row)
    return low


def add_matrix(a, b):
    if len(a) != len(b):
        return None
    for i in range(len(a)):
        if len(a[i]) != len(b[i]):
            return None

    mat = []
    for i in range(len(a)):
        row = []
        for j in range(len(a)):
            row.append(a[i][j] + b[i][j])
        mat.append(row)
    return mat


def mult_matrix(x, y):
    return [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*y)] for X_row in x]


def is_diagonally_dominant(mat):
    if mat is None:
        return False

    for numb, i in enumerate(mat):
        if abs(mat[numb][numb]) < abs(sum(i) - mat[numb][numb]):
            return False
    return True


def is_matrix_square(mat):
    rows = len(mat)
    for row in mat:
        if len(row) != rows:
            return False
    return True
