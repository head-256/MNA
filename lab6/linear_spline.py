#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def linear_spline(data):
    np1 = len(data)
    n = np1 - 1
    X, Y = zip(*data)
    X = [float(x) for x in X]
    Y = [float(y) for y in Y]
    a = [0.0] * n
    b = [0.0] * n

    for i in range(1, n + 1):
        a[i - 1] = (Y[i] - Y[i - 1]) / (X[i] - X[i - 1])
        b[i - 1] = Y[i - 1] - a[i - 1] * X[i - 1]

    spline = []
    for i in range(n):
        spline.append((a[i], b[i], X[i]))
    return spline, X[n]


def splines_to_plot(spline, xn, grid_res):
    n = len(spline)
    per_spline = int(grid_res / n)
    if per_spline < 1:
        per_spline = 1
    X = []
    Y = []
    for i in range(n - 1):
        S = spline[i]
        x0 = S[2]
        x1 = spline[i + 1][2]
        x = np.linspace(x0, x1, per_spline)
        for xi in x:
            X.append(xi)
            Y.append(S[1] + S[0] * xi)
    S = spline[n - 1]
    x = np.linspace(S[2], xn, per_spline)
    for xi in x:
        X.append(xi)
        Y.append(S[1] + S[0] * xi)

    return X, Y


if __name__ == '__main__':
    data = [(0.452, 1.252), (0.967, 2.015), (2.255, 4.342), (4.013, 5.752), (5.432, 6.911)]

    lstX = [x[0] for x in data]
    lstY = [x[1] for x in data]
    spline, xn = linear_spline(data)
    X, Y = splines_to_plot(spline, xn, grid_res=1000)

    plt.title('Linear Spline')
    plt.grid(True)
    plt.plot(X, Y, 'r-')
    plt.plot(lstX, lstY, 'ko')

    plt.show()
