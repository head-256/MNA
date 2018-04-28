#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import matplotlib.pyplot as plt


def rk4(f, y0, a, b, n):
    X = [0] * (n + 1)
    Y = [0] * (n + 1)
    h = (b - a) / float(n)
    print(h)
    X[0] = x = a
    Y[0] = y = y0
    for i in range(1, n + 1):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        X[i] = x = a + i * h
        Y[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
    return X, Y


def fd(x, y):
    return (x * y**2 - 2 * y) / (2 * x)


def f(x):
    return 2 / (x - x * math.log(x))


if __name__ == '__main__':
    y0 = 2
    a = 1
    b = 1.8
    n = 4
    X, Y = rk4(fd, y0, a, b, n)
    for x, y in list(zip(X, Y)):
        print("x: {x:.1f}   y: {y:.6f}  error: {error:.6f}".format(x=x, y=y, error=abs(y - f(x))))

    plt.grid(True)
    plt.plot(X, Y)
    plt.show()
