from math import exp

import numpy as np


class InitialValueMethods:
    x0 = 0
    y0 = 0
    N = 10
    start = 0
    finish = 3

    delta = (start + finish) / N

    # Analytic solution
    def excact_method(self):
        x = np.linspace(self.start, self.finish, self.N)
        y = [self.y0]

        for i in range(1, len(x)):
            y.append(2 * x[i] + exp(-2 * x[i]) - 1)

        return [x, y]

    def euler_method(self):
        x = np.linspace(self.start, self.finish, self.N)
        y = [self.y0]
        delta = (self.start + self.finish) / self.N

        for i in range(1, len(x)):
            y.append(y[i - 1] + delta * (-2 * y[i - 1] + 4 * x[i - 1]))

        return [x, y]

    def euler_method_improved(self):
        x = np.linspace(self.start, self.finish, self.N)
        y = [self.y0]
        delta = (self.start + self.finish) / self.N

        for i in range(1, len(x)):
            y.append(y[i - 1] + (delta / 2) * (
                    f(x[i - 1], y[i - 1]) + f(x[i - 1] + delta, y[i - 1] + delta * f(x[i - 1], y[i - 1]))))

        return [x, y]

    def runge_kutta_method(self):
        x = np.linspace(self.start, self.finish, self.N)
        y = [self.y0]
        delta = (self.start + self.finish) / self.N

        for i in range(1, len(x)):
            k1 = f(x[i - 1], y[i - 1])
            k2 = f(x[i - 1] + delta / 2, y[i - 1] + (delta / 2) * k1)
            k3 = f(x[i - 1] + delta / 2, y[i - 1] + (delta / 2) * k2)
            k4 = f(x[i - 1] + delta, y[i - 1] + delta * k3)

            y.append(y[i - 1] + (delta/6)*(k1 + 2*k2 + 2*k3 + k4))

        return [x, y]


def f(x, y):
    return -2 * y + 4 * x
