#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sympy as sym
from functools import partial

x = sym.symbols('x0 x1')
F0 = sym.tan(x[0] * x[1] + 0.5) - x[0] ** 2
F1 = x[0] ** 2 + x[1] ** 2 - 1
J1 = sym.lambdify(x, sym.diff(F0, x[0]))
J2 = sym.lambdify(x, sym.diff(F0, x[1]))
J3 = sym.lambdify(x, sym.diff(F1, x[0]))
J4 = sym.lambdify(x, sym.diff(F1, x[1]))


def newton_method(f, J, x, eps):
    f_value = f(x)
    f_norm = np.linalg.norm(f_value, ord=2)
    while abs(f_norm) > eps:
        delta = np.linalg.solve(J(x), -f_value)
        x += delta
        f_value = f(x)
        f_norm = np.linalg.norm(f_value, ord=2)
    return x


def newton_method_mod(f, J, x, eps):
    f_value = f(x)
    f_norm = np.linalg.norm(f_value, ord=2)
    jacobian = J(x)
    while abs(f_norm) > eps:
        delta = np.linalg.solve(jacobian, -f_value)
        x += delta
        f_value = f(x)
        f_norm = np.linalg.norm(f_value, ord=2)
    return x


def f(x):
    return np.array(
        [np.tan(x[0] * x[1] + 0.5) - x[0] ** 2,
         x[0] ** 2 + x[1] ** 2 - 1])


def J(x):
    return np.array(
        [[J1(x[0], x[1]), J2(x[0], x[1])],
         [J3(x[0], x[1]), J4(x[0], x[1])]])


if __name__ == "__main__":
    newton = partial(newton_method, f, J, eps=0.001)
    result_1 = newton(np.array([0.9, 0.3]))
    result_2 = newton(np.array([-0.9, -0.3]))
    result_3 = newton(np.array([0.4, -1]))
    result_4 = newton(np.array([-0.4, 1]))

    print('Result (Newton Method):')
    print(result_1, result_2, result_3, result_4, sep='\n')

    newton_mod = partial(newton_method_mod, f, J, eps=0.001)
    result_5 = newton_mod(np.array([0.9, 0.3]))
    result_6 = newton_mod(np.array([-0.9, -0.3]))
    result_7 = newton_mod(np.array([0.4, -1]))
    result_8 = newton_mod(np.array([-0.4, 1]))

    print('Result (Mod Newton Method):')
    print(result_5, result_6, result_7, result_8, sep='\n')
