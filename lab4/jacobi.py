#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt
from copy import deepcopy
from numpy import array, identity, diagonal


def max_elem(A):  # Нахождение максимального элемента в верхнем треугольнике матрицы A: A[k, l]
    n = len(A)
    a_max = 0.0
    k = l = 0.0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(A[i, j]) >= a_max:
                a_max = abs(A[i, j])
                k = i
                l = j
    return a_max, k, l


def rotate(A, P, k, l):  # t - tan, s - sin, c - cos
    n = len(A)
    a_diff = A[l, l] - A[k, k]

    if abs(A[k, l]) < abs(a_diff) * 1.0e-36:  # если A[k,l] очень мало
        t = A[k, l] / a_diff
    else:
        phi = a_diff / (2.0 * A[k, l])
        t = 1.0 / (abs(phi) + sqrt(phi ** 2 + 1.0))
        if phi < 0.0:
            t = -t
    c = 1.0 / sqrt(t ** 2 + 1.0)
    s = t * c
    tau = s / (1.0 + c)
    temp = A[k, l]
    A[k, l] = 0.0
    A[k, k] = A[k, k] - t * temp
    A[l, l] = A[l, l] + t * temp
    for i in range(k):  # Если i < k
        temp = A[i, k]
        A[i, k] = temp - s * (A[i, l] + tau * temp)
        A[i, l] = A[i, l] + s * (temp - tau * A[i, l])
    for i in range(k + 1, l):  # Если k < i < l
        temp = A[k, i]
        A[k, i] = temp - s * (A[i, l] + tau * A[k, i])
        A[i, l] = A[i, l] + s * (temp - tau * A[i, l])
    for i in range(l + 1, n):  # Если i > l
        temp = A[k, i]
        A[k, i] = temp - s * (A[l, i] + tau * temp)
        A[l, i] = A[l, i] + s * (temp - tau * A[l, i])
    for i in range(n):
        temp = P[i, k]
        P[i, k] = temp - s * (P[i, l] + tau * P[i, k])
        P[i, l] = P[i, l] + s * (temp - tau * P[i, l])


def jacobi(A, eps):
    A = deepcopy(A)
    n = len(A)
    max_rot = 5 * (n ** 2)
    P = identity(n)  # Матрица вращений

    for i in range(max_rot):
        a_max, k, l = max_elem(A)
        if a_max < eps:
            return diagonal(A), P
        rotate(A, P, k, l)
    return None


def transpose(A):
    n = len(A)
    T = deepcopy(A)
    for i in range(n):
        for j in range(n):
            if i > j:
                T[i][j], T[j][i] = T[j][i], T[i][j]
    return T


if __name__ == "__main__":
    A = array([[2.0, 1.0],
               [1.0, 3.0]])
    B = array([[5.0, 1.0, 2.0],
               [1.0, 4.0, 1.0],
               [2.0, 1.0, 3.0]])
    C = array([[2.979, 0.273, 0.318, 0.219],
               [0.273, 3.951, 0.197, 0.231],
               [0.318, 0.197, 2.875, 0.187],
               [0.219, 0.231, 0.187, 3.276]])

    D = array([[2.923, 0.220, 0.318, 0.159],
               [0.363, 4.123, 0.268, 0.327],
               [0.169, 0.271, 3.906, 0.295],
               [0.241, 0.319, 0.257, 3.862]])

    res_a = jacobi(A, 0.01)
    res_b = jacobi(B, 0.01)
    res_c = jacobi(C, 0.01)
    res_d = jacobi(D, 0.01)

    print("Eigenvalues: {}\nEigenvectors:\n{}".format(res_a[0], transpose(res_a[1])))
    print("Eigenvalues: {}\nEigenvectors:\n{}".format(res_b[0], transpose(res_b[1])))
    print("Eigenvalues: {}\nEigenvectors:\n{}".format(res_c[0], transpose(res_c[1])))
    print("Eigenvalues: {}\nEigenvectors:\n{}".format(res_d[0], transpose(res_d[1])))
