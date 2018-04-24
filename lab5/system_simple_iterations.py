#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def f1_plus(y):
    return np.sqrt(1 - (y ** 2))


def f1_minus(y):
    return -np.sqrt(1 - (y ** 2))


def f2(x):
    return (np.arctan(x ** 2) - 0.5) / x


def simple_iterations_method(f1, f2, x, y, eps):
    x_value = f1(y)
    y_value = f2(x)

    while max(abs(x_value - x), abs(y_value - y)) > eps:
        x = f1(y_value)
        y = f2(x_value)
        x_value = f1(y)
        y_value = f2(x)
    return x, y


if __name__ == "__main__":

    result_1 = list(simple_iterations_method(f1_plus, f2, x=0.9, y=0.3, eps=0.001))
    result_2 = list(simple_iterations_method(f1_minus, f2, x=-0.9, y=-0.3, eps=0.001))

    print('Result:')
    print(result_1, result_2, sep='\n')
