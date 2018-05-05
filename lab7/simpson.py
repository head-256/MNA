#!/usr/bin/env python
# -*- coding: utf-8 -*-


def simpson(f, a, b, n):
    if n % 2:
        raise ValueError("n must be even")

    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)

    return s * h / 3


def f(x):
    return x * 2**(-x)


if __name__ == '__main__':
    a = 0
    b = 2
    n = 20
    result_h = simpson(f, a, b, n)
    result_2h = simpson(f, a, b, n // 2)
    print("Result with h steps: {result}".format(result=result_h))
    print("Result with 2h steps: {result}".format(result=result_2h))
