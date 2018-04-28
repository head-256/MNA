#!/usr/bin/env python
# -*- coding: utf-8 -*-


def trapezoid_method(f, a, b, n):
    h = (b - a) / float(n)
    print(h)
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return h * s


def f(x):
    return x * 2**(-x)


if __name__ == '__main__':
    a = 0
    b = 2
    n = 20
    result_h = trapezoid_method(f, a, b, n)
    result_2h = trapezoid_method(f, a, b, n // 2)
    print("Result with h steps: {result}".format(result=result_h))
    print("Result with 2h steps: {result}".format(result=result_2h))
