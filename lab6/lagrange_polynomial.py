#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def lagrange(points, x):
    n = len(points)
    X, Y = zip(*points)

    L = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i == j:
                continue
            p *= (x - X[j]) / (X[i] - X[j])

        L += p * Y[i]

    return L


if '__main__' in __name__:
    points = [(0.452, 1.252), (0.967, 2.015), (2.255, 4.342), (4.013, 5.752), (5.432, 6.911)]

    x = np.arange(0, 5.432, 0.01)
    y = lagrange(points, x)

    print("L4(x1 + x2) = ", lagrange(points, 0.967 + 2.255))

    plt.grid(True)
    plt.plot(x, y)
    plt.show()
