#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def f_1(values):
    return np.arctan(values[0] ** 2 - 0.5) / values[0]


def f_2_plus(values):
    return np.sqrt(1 - (values[1] ** 2))


def f_2_minus(values):
    return -np.sqrt(1 - (values[1] ** 2))


def precision(solution0, solution_prev, eps=0.001):
    for i in range(len(solution0)):
        if abs(solution0[i] - solution_prev[i]) > eps:
            return False
    return True


def simple_iterations_method(functions, solution_start):
    solution_prev = solution_start[:]
    solution0 = solution_start[:]
    for i in range(len(solution_prev)):
        solution_prev[i] += 1

    while not precision(solution0, solution_prev):
        solution_prev = solution0[:]
        for i in range(len(solution0)):
            solution0[i] = functions[i](solution0)
    return solution0


if __name__ == "__main__":

    solution_plus = simple_iterations_method([f_2_plus, f_1], [0.9, 0.3])
    solution_minus = simple_iterations_method([f_2_minus, f_1], [-0.9, -0.3])
    solution = solution_plus + solution_minus

    print("Result: {roots}".format(roots=solution))
