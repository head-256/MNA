#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sympy as sym

x = sym.symbols('x')
f_expr = x - 1 / (3 + sym.sin(3.6 * x))
dfdx_expr = sym.diff(f_expr, x)

dfdx = sym.lambdify([x], dfdx_expr)


def tangents_method(f, dfdx, x, eps):
    f_value = f(x)
    while abs(f_value) > eps:
        try:
            x -= float(f_value) / dfdx(x)
        except ZeroDivisionError:
            raise SystemExit('Zero division')
        f_value = f(x)
    return x


def f(x):
    return x - 1 / (3 + math.sin(3.6 * x))


if __name__ == "__main__":
    solution = tangents_method(f, dfdx, x=1, eps=0.00001)

    print("Result: {root}".format(root=solution))
