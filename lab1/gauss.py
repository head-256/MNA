#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import deepcopy


def gauss(matrix):
    matrix = deepcopy(matrix)
    n = len(matrix)

    for i in range(0, n):

        # Поиск максимума в столбце
        max_el = abs(matrix[i][i])
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > max_el:
                max_el = abs(matrix[j][i])
                max_row = j

        # Поменять местами текущую и максимальную строки
        for j in range(i, n + 1):
            matrix[max_row][j], matrix[i][j] = matrix[i][j], matrix[max_row][j]

        # Приведение к треугольному виду
        for j in range(i + 1, n):
            try:
                c = -matrix[j][i] / matrix[i][i]
            except ZeroDivisionError:
                print("Zero Division Error!")
                return None
            for k in range(i, n + 1):
                if i == k:
                    matrix[j][k] = 0
                else:
                    matrix[j][k] += c * matrix[i][k]

    # Проверка на совместность и определенность
    for i in range(0, n):
        zero_row = True
        for j in range(0, n):
            if matrix[i][j] != 0:
                zero_row = False
        if zero_row and matrix[i][n] != 0:
            return "No solutions!"
        elif zero_row and matrix[i][n] == 0:
            return "Infinite solutions!"

    # Решение системы для верхней треугольной матрицы
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        try:
            x[i] = matrix[i][n] / matrix[i][i]
        except ZeroDivisionError:
            print("Zero Division Error!")
            return None
        for j in range(i - 1, -1, -1):
            matrix[j][n] -= matrix[j][i] * x[i]
    return x


if __name__ == "__main__":
    A = [[3, 2, -5, -1],
         [2, -1, 3, 13],
         [1, 2, -1, 9]]

    B = [[2.979, 0.427, 0.406, 0.348, 0.341],
         [0.273, 3.951, 0.217, 0.327, 0.844],
         [0.318, 0.197, 2.875, 0.166, 0.131],
         [0.219, 0.231, 0.187, 3.276, 0.381]]

    C = [[3, 2, -5, -1],
         [3, 2, -5, -1],
         [1, 2, -1, 9]]

    D = [[1, 1, -1, -4],
         [1, 2, -3, 0],
         [-2, 0, -2, 3]]

    print("Result: {roots}".format(roots=gauss(B)))
    print("Result: {roots}".format(roots=gauss(A)))
    print("Result: {roots}".format(roots=gauss(C)))
    print("Result: {roots}".format(roots=gauss(D)))