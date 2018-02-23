from copy import deepcopy


def to_diagonally_dominant(matrix):
    dd_matrix = deepcopy(matrix)
    size = len(dd_matrix)
    for i in range(0, size):
        for j in range(0, size):
            if i != j and abs(dd_matrix[i][i]) < abs(dd_matrix[i][j]):
                    dd_matrix[i][i], dd_matrix[i][j] = dd_matrix[i][j], dd_matrix[i][i]
    return dd_matrix
