import math
import matplotlib.pyplot as plt
import numpy as np
import random as rnd




def task1_1_11():
    def f(arg):
        if arg < 0:
            return math.sin(arg + 5)/(pow(arg, 2) + 13)
        else:
            return arg/(pow(arg, 2) + 1)

    x = [i for i in range(-100, 100)]
    y = [f(i) for i in x]

    plt.title("График одной переменной.")
    plt.grid()
    plt.xlabel("Значения X")
    plt.ylabel("Значения функции")
    plt.plot(x, y)
    plt.show()


def task1_2_13():

    x = [i for i in range(-20, 20)]
    y = [i for i in range(-20, 20)]

    x.remove(0)
    y.remove(0)

    xgrid, ygrid = np.meshgrid(x, y)

    zgrid = pow(xgrid, (1/ygrid))*pow(ygrid, 2)

    fig = plt.figure(figsize=(7, 4))
    ax = plt.axes(projection='3d')
    ax.plot_surface(xgrid, ygrid, zgrid)
    plt.show()


def task1_3_1():
    t = np.arange(0, 2*np.pi, 0.1)
    b = 50

    y1 = b*(np.cos(t)**3)
    y2 = b*(np.sin(t)**3)

    plt.title(f"График параметрически заданной функции (коэффициент b = {b}).")
    plt.grid()
    plt.xlabel("Значения t")
    plt.ylabel("Значения функции")
    plt.plot(t, y1, 'b-')
    plt.plot(t, y2, 'r-')
    plt.show()


if __name__ == '__main__':
    # task1_1_11()
    # task1_2_13()
    task1_3_1()
