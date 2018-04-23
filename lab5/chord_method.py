#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def secant(f, x0, x1, eps):
    f_x0 = f(x0)
    f_x1 = f(x1)
    x = 0
    while abs(f_x1) > eps:
        try:
            denominator = float(f_x1 - f_x0) / (x1 - x0)
            x = x1 - float(f_x1) / denominator
        except ZeroDivisionError:
            raise SystemError("Zero Division")
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(x1)

    return x


def f(x):
    return x - 1 / (3 + math.sin(3.6 * x))


if __name__ == "__main__":
    x0 = -1
    x1 = 1

    solution = secant(f, x0, x1, eps=0.00001)

    print("Result: {root}".format(root=solution))
