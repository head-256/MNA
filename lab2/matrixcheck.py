def is_diagonally_dominant(matrix):
    size = len(matrix)
    for i in range(0, size):
        for j in range(0, size):
            if i != j and matrix[i][i] < matrix[i][j]:
                    return False
    return True
