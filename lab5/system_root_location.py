#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sympy as sym

if __name__ == "__main__":
    x, y = sym.symbols('x, y')
    f = x ** 2 + y ** 2 - 1
    g = sym.tan(x * y + 0.5) - x ** 2

    args = (x, -2, 2), (y, -2, 2)

    curve_f = sym.plot_implicit(sym.Eq(f, 0), *args, show=False)
    curve_g = sym.plot_implicit(sym.Eq(g, 0), *args, show=False)

    curve_g.extend(curve_f)
    curve_g.show()
