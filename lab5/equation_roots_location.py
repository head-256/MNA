#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def func(x: np.ndarray):
    return x - 1 / (3 + np.sin(3.6 * x))


if __name__ == "__main__":

    x = np.arange(-1, 1, 0.1)
    y = func(x)

    plt.grid(True)
    plt.axhline(0, color='black')
    plt.plot(x, y)

    plt.show()
