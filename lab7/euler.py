#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def euler(f, y0, a, b, n):
    X = [0] * (n + 1)
    Y = [0] * (n + 1)
    h = (b - a) / float(n)
    print(h)
    X[0] = x = a
    Y[0] = y = y0
    for i in range(1, n + 1):
        y += h * f(x, y)
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
    # n = 15872 (10^-4)
    # n = 1579 (10^-3)
    # n = 157 (10^-2)
    # n = 15 (10^-1)
    n = 15
    X, Y = euler(fd, y0, a, b, n)
    print(len(X))
    for x, y in list(zip(X, Y)):
        print("x: {x:.6f}   y: {y:.6f}  error: {error:.6f}".format(x=x, y=y, error=abs(y - f(x))))
