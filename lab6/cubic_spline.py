#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt


def cubic_spline(data):
    np1 = len(data)
    n = np1 - 1
    X, Y = zip(*data)
    X = [float(x) for x in X]
    Y = [float(y) for y in Y]
    a = Y[:]
    b = [0.0] * n
    d = [0.0] * n
    h = [X[i + 1] - X[i] for i in range(n)]
    alpha = [0.0] * n
    for i in range(1, n):
        alpha[i] = 3 / h[i] * (a[i + 1] - a[i]) - 3 / h[i - 1] * (a[i] - a[i - 1])
    c = [0.0] * np1
    L = [0.0] * np1
    u = [0.0] * np1
    z = [0.0] * np1
    L[0] = 1.0
    u[0] = z[0] = 0.0
    for i in range(1, n):
        L[i] = 2 * (X[i + 1] - X[i - 1]) - h[i - 1] * u[i - 1]
        u[i] = h[i] / L[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / L[i]
    L[n] = 1.0
    z[n] = c[n] = 0.0
    for j in range(n - 1, -1, -1):
        c[j] = z[j] - u[j] * c[j + 1]
        b[j] = (a[j + 1] - a[j]) / h[j] - (h[j] * (c[j + 1] + 2 * c[j])) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])
    spline = []
    for i in range(n):
        spline.append((a[i], b[i], c[i], d[i], X[i]))
    return spline, X[n]


def splines_to_plot(spline, xn, grid_res):
    n = len(spline)
    per_spline = int(grid_res / n)
    if per_spline < 3:
        per_spline = 3
    X = []
    Y = []
    for i in range(n - 1):
        S = spline[i]
        x0 = S[4]
        x1 = spline[i + 1][4]
        x = np.linspace(x0, x1, per_spline)
        for xi in x:
            X.append(xi)
            h = (xi - S[4])
            Y.append(S[0] + S[1] * h + S[2] * h ** 2 + S[3] * h ** 3)
    S = spline[n - 1]
    x = np.linspace(S[4], xn, per_spline)
    for xi in x:
        X.append(xi)
        h = (xi - S[4])
        Y.append(S[0] + S[1] * h + S[2] * h ** 2 + S[3] * h ** 3)

    return X, Y


if __name__ == '__main__':
    data = [(0.452, 1.252), (0.967, 2.015), (2.255, 4.342), (4.013, 5.752), (5.432, 6.911)]

    lstX = [x[0] for x in data]
    lstY = [x[1] for x in data]
    spline, xn = cubic_spline(data)
    X, Y = splines_to_plot(spline, xn, grid_res=1000)
    print(spline, xn)

    plt.title('Cubic Spline')
    plt.grid(True)
    plt.plot(X, Y, 'r-')
    plt.plot(lstX, lstY, 'ko')

    plt.show()
