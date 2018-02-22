#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy


def simple_iterations(A, B, eps):
    A = deepcopy(A)
    B = deepcopy(B)
    N = len(A)
    X = [0.0] * N

    matrix = [None] * N
    while True:
        for i in range(0, N):
            matrix[i] = B[i]
            for j in range(0, N):
                if i != j:
                    matrix[i] -= A[i][j] * X[j]
            matrix[i] /= A[i][i]
        norm = abs(X[0] - matrix[0])
        for k in range(0, N):
            if abs(X[k] - matrix[k] > norm):
                norm = abs(X[k] - matrix[k])
            X[k] = matrix[k]
        if norm <= eps:
            break
    return X


if __name__ == "__main__":
    A = [[2.979, 0.427, 0.406, 0.348],
         [0.273, 3.951, 0.217, 0.327],
         [0.318, 0.197, 2.875, 0.166],
         [0.219, 0.231, 0.187, 3.276]]
    B = [0.341, 0.844, 0.131, 0.381]

    print(simple_iterations(A, B, 0.001))
