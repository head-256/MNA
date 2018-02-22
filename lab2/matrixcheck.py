def is_diagonally_dominant(matrix):
    n = len(matrix)
    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                if matrix[i][i] < matrix[i][j]:
                    return False
    return True
