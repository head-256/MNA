#!/usr/bin/env python
# -*- coding: utf-8 -*-


import differences
import matplotlib.pyplot as plt
import numpy as np


def product_of_diffs(X, index, x):
    mul = 1
    for i in range(index):
        mul *= x - X[i]
    return mul


def newton(points, x):
    n = len(points)
    X, Y = zip(*points)

    diff_table = [Y[0], *differences.difference_quotient_table(Y, X, offset=1)]
    N = 0
    for i in range(n):
        N += diff_table[i] * product_of_diffs(X, i, x)

    return N


if __name__ == '__main__':
    points = [(0.452, 1.252), (0.967, 2.015), (2.255, 4.342), (4.013, 5.752), (5.432, 6.911)]

    x = np.arange(0, 5.432, 0.01)
    y = newton(points, x)

    print("N4(x1 + x2): ", newton(points, 0.967 + 2.255))

    plt.grid(True)
    plt.plot(x, y)
    plt.show()
