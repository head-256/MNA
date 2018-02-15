#!/usr/bin/env python
# -*- coding: utf-8 -*-


def gauss(matrix):
    n = len(matrix)

    for i in range(0, n):
        max_el = abs(matrix[i][i])
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > max_el:
                max_el = abs(matrix[j][i])
                max_row = j

        for j in range(i, n + 1):
            matrix[max_row][j], matrix[i][j] = matrix[i][j], matrix[max_row][j]

        for j in range(i + 1, n):
            c = -matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                if i == k:
                    matrix[j][k] = 0
                else:
                    matrix[j][k] += c * matrix[i][k]

    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n] / matrix[i][i]
        for j in range(i - 1, -1, -1):
            matrix[j][n] -= matrix[j][i] * x[i]
    return x


if __name__ == "__main__":
    A = [[3, 2, -5, -1], [2, -1, 3, 13], [1, 2, -1, 9]]

    print(gauss(A))
