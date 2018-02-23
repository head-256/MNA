#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matrixconvert as mc


def seidel(matrix, free_terms, eps):
    matrix = mc.to_diagonally_dominant(matrix)
    size = len(matrix)
    solutions = [.0] * size
    temp_solutions = [.0] * size

    while True:
        for i in range(0, size):
            temp_solutions[i] = free_terms[i]
            for j in range(0, size):
                if j < i:
                    temp_solutions[i] -= matrix[i][j] * temp_solutions[j]
                if j > i:
                    temp_solutions[i] -= matrix[i][j] * solutions[j]
            try:
                temp_solutions[i] /= matrix[i][i]
            except ZeroDivisionError:
                print("Zero Division Error!")
                return None

        norm = abs(solutions[0] - temp_solutions[0])
        for i in range(0, size):
            if abs(solutions[i] - temp_solutions[i]) > norm:
                norm = abs(solutions[i] - temp_solutions[i])
            solutions[i] = temp_solutions[i]
        if norm <= eps:
            break
    return solutions


if __name__ == "__main__":
    A = [[2.979, 0.427, 0.406, 0.348],
         [0.273, 3.951, 0.217, 0.327],
         [0.318, 0.197, 2.875, 0.166],
         [0.219, 0.231, 0.187, 3.276]]
    B = [0.341, 0.844, 0.131, 0.381]

    A2 = [[2, 1],
          [5, 7]]
    B2 = [11, 13]

    A3 = [[10, -1, 2, 0],
          [-1, 11, -1, 3],
          [2, -1, 10, -1],
          [0, 3, -1, 8]]
    B3 = [6, 25, -11, 15]

    A4 = [[10, -1, 2, 0],
          [-1, 11, -1, 3],
          [2, -1, 10, -1],
          [0, 3, -1, 2]]
    B4 = [6, 25, -11, 15]

    A5 = [[3, 2, -5],
          [2, -1, 3],
          [1, 2, -1]]
    B5 = [-1, 13, 9]

    print("Result: {roots}".format(roots=seidel(A, B, 0.01)))
    print("Result: {roots}".format(roots=seidel(A2, B2, 0.01)))
    print("Result: {roots}".format(roots=seidel(A3, B3, 0.01)))
    print("Result: {roots}".format(roots=seidel(A4, B4, 0.01)))
    print("Result: {roots}".format(roots=seidel(A5, B5, 0.01)))
