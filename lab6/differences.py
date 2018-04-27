#!/usr/bin/env python
# -*- coding: utf-8 -*-


def difference_quotient_table(Y, X, list_prev=None, offset=1):
    n = len(Y)

    if list_prev is None:
        list_prev = []
    F = tuple()

    for i in range(n - 1):
        k = (Y[i + 1] - Y[i]) / (X[i + offset] - X[i])
        F = F + (k,)

    offset += 1
    list_prev.append(F[0])
    if n <= 2:
        return list_prev
    else:
        return difference_quotient_table(F, X, list_prev, offset)


def finite_difference_table(Y, list_prev=None, offset=1):
    n = len(Y)

    if list_prev is None:
        list_prev = []
    F = tuple()

    for i in range(n - 1):
        k = (Y[i + 1] - Y[i])
        F = F + (k,)

    offset += 1
    list_prev.append(F[0])
    if n <= 2:
        return list_prev
    else:
        return finite_difference_table(F, list_prev, offset)


if __name__ == '__main__':
    points = [(0.452, 1.252), (0.967, 2.015), (2.255, 4.342), (4.013, 5.752), (5.432, 6.911)]
    X, Y = zip(*points)

    print("Quotient differences: ", difference_quotient_table(Y, X))
    print("Finite differences: ", finite_difference_table(Y))
