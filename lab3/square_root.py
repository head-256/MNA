#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt
from copy import deepcopy
from gauss import gauss


def cholesky(A):
    n = len(A)
    U = [[.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = sum(U[i][k] * U[j][k] for k in range(j))
            try:
                if i == j:
                    U[i][j] = sqrt(A[i][i] - s)
                else:
                    U[i][j] = 1.0 / U[j][j] * (A[i][j] - s)
            except ValueError:
                print("Non-positive expression under sqrt!")
                raise SystemExit(0)
            except ZeroDivisionError:
                print("Zero Division!")
                raise SystemExit(0)
    return U


def transpose(A):
    A = deepcopy(A)
    n = len(A)
    for i in range(n):
        for j in range(n):
            if i < j:
                A[i][j], A[j][i] = A[j][i], A[i][j]
    return A


def square_root(A, b):
    U = cholesky(A)
    y = gauss(U, b)
    x = gauss(transpose(U), y)
    return x


if __name__ == "__main__":
    A1 = [[2, 1, 4],
          [1, 1, 3],
          [4, 3, 14]]
    B1 = [16, 12, 52]

    A2 = [[2.979, 0.273, 0.318, 0.219],
          [0.273, 3.951, 0.197, 0.231],
          [0.318, 0.197, 2.875, 0.187],
          [0.219, 0.231, 0.187, 3.276]]
    B2 = [0.341, 0.844, 0.131, 0.381]

    A3 = [[2.979, 0.427, 0.406, 0.348],
          [0.427, 3.951, 0.217, 0.327],
          [0.406, 0.217, 2.875, 0.166],
          [0.348, 0.327, 0.166, 3.276]]
    B3 = [0.341, 0.844, 0.131, 0.381]

    print("Result: {roots}".format(roots=square_root(A1, B1)))
    print("Result: {roots}".format(roots=square_root(A2, B2)))
    print("Result: {roots}".format(roots=square_root(A3, B3)))
