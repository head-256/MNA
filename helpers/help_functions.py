from math import cos, sin, atan

from copy import deepcopy


def rotation_matrix(n, phi, a, b):
    H = [[0.0] * n for _ in range(n)]
    for i in range(n):
        H[i][i] = 1
    H[a - 1][a - 1] = H[b - 1][b - 1] = cos(phi)
    H[a - 1][b - 1] = -sin(phi)
    H[b - 1][a - 1] = sin(phi)
    return H


def mm(A, B):
    return [[sum(x * B[i][col] for i, x in enumerate(row)) for col in range(len(B[0]))] for row in A]


def transpose(A):
    n = len(A)
    T = deepcopy(A)
    for i in range(n):
        for j in range(n):
            if i > j:
                T[i][j], T[j][i] = T[j][i], T[i][j]
    return T


def phi_calc(Aij, Aii, Ajj):
    phi = (atan((2 * Aij) / (Aii - Ajj))) / 2
    return phi


def print_m(A):
    for i in range(len(A)):
        print(A[i])


A_prev = [[2.979, 0.273, 0.318, 0.219],
          [0.273, 3.951, 0.197, 0.231],
          [0.318, 0.197, 2.875, 0.187],
          [0.219, 0.231, 0.187, 3.276]]
H = rotation_matrix(4, 0.704, 1, 3)
A_cur = mm(mm(transpose(H), A_prev), H)

A1 = mm(mm(transpose(H), A_prev), H)
phi1 = phi_calc(0.336, 3.249, 3.951)
H1 = rotation_matrix(4, phi1, 1, 2)

A2 = mm(mm(transpose(H1), A1), H1)
phi2 = phi_calc(0.322, 4.0857, 3.276)
H2 = rotation_matrix(4, phi2, 2, 4)

A3 = mm(mm(transpose(H2), A2), H2)
phi3 = phi_calc(0.171, 3.115, 3.164)
H3 = rotation_matrix(4, phi3, 1, 4)

A4 = mm(mm(transpose(H3), A3), H3)
phi4 = phi_calc(0.0451, 2.966, 4.198)
H4 = rotation_matrix(4, phi4, 1, 2)

A5 = mm(mm(transpose(H4), A4), H4)
phi5 = phi_calc(0.0388, 4.199, 3.312)
H5 = rotation_matrix(4, phi5, 2, 4)

A6 = mm(mm(transpose(H5), A5), H5)
phi6 = phi_calc(-0.0222, 4.201, 2.605)
H6 = rotation_matrix(4, phi6, 2, 3)

A7 = mm(mm(transpose(H6), A6), H6)
phi7 = phi_calc(0.0143, 2.604, 3.31)
H7 = rotation_matrix(4, phi7, 3, 4)

A8 = mm(mm(transpose(H7), A7), H7)
print_m(A8)