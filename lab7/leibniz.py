#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sympy as sym


x = sym.Symbol('x')
f = sym.lambdify(x, sym.integrate(x * 2 ** (-x), x))


def leibniz_integrate(f, a, b):
    return f(b) - f(a)


if __name__ == '__main__':
    a = 0
    b = 2
    print("Exact value: {result}".format(result=leibniz_integrate(f, a, b)))
