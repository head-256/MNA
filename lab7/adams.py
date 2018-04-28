#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import matplotlib.pyplot as plt


def ab2(f, y0, a, b, n):
    X = [0] * (n + 1)
    Y = [0] * (n + 1)
    h = (b - a) / float(n)
    print(h)
    X[0] = x = a
    Y[0] = y = y0
    _y = y + (3 * f(x, y) - f(x, y)) * h / 2
    y = y + (f(x, y) + f(x + h, _y)) * h / 2
    x += h
    X[1] = x
    Y[1] = y
    for i in range(2, n + 1):
        yf = y
        yf += (3 * f(X[i - 1], Y[i - 1])) * h / 2
        yf -= f(X[i - 2], Y[i - 2]) * h / 2
        y = y + (f(X[i - 1], Y[i - 1]) + f(x + h, yf)) * h / 2
        x += h
        X[i] = x
        Y[i] = y
    return X, Y


def fd(x, y):
    return (x * y**2 - 2 * y) / (2 * x)


def f(x):
    return 2 / (x - x * math.log(x))


if __name__ == '__main__':
    y0 = 2
    a = 1
    b = 1.8
    n = 46
    X, Y = ab2(fd, y0, a, b, n)
    for x, y in list(zip(X, Y)):
        print("x: {x:.6f}   y: {y:.6f}  error: {error:.6f}".format(x=x, y=y, error=abs(y - f(x))))

    plt.grid(True)
    plt.plot(X, Y)
    plt.show()
