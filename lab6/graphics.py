#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import linear_spline as ls
import quadratic_spline as qs
import cubic_spline as cs
import newton_polynomial as newton
import lagrange_polynomial as lagrange


if __name__ == '__main__':
    data = [(0.452, 1.252), (0.967, 2.015), (2.255, 4.342), (4.013, 5.752), (5.432, 6.911)]

    x_newton = np.arange(0, 5.432, 0.1)
    y_newton = newton.newton(data, x_newton)

    x_lagrange = np.arange(0, 5.432, 0.1)
    y_lagrange = lagrange.lagrange(data, x_lagrange)

    spline, xl = ls.linear_spline(data)
    x_linear, y_linear = ls.splines_to_plot(spline, xl, grid_res=1000)

    spline, xq = qs.quadratic_spline(data)
    x_quadratic, y_quadratic = qs.splines_to_plot(spline, xq, grid_res=1000)

    spline, xc = cs.cubic_spline(data)
    x_cubic, y_cubic = cs.splines_to_plot(spline, xc, grid_res=1000)

    plt.grid(True)
    plt.plot(x_newton, y_newton, linewidth=4)
    plt.plot(x_lagrange, y_lagrange, '-')
    plt.plot(x_linear, y_linear, 'r-')
    plt.plot(x_quadratic, y_quadratic, 'g-')
    plt.plot(x_cubic, y_cubic, 'y-')

    plt.show()
