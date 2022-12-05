from scipy import integrate
import math
import matplotlib.pyplot as plt
import sympy as sp

def task4_1():
    # 20 вариант
    def f(x):
        return math.sqrt(3 - 2*x - x**2)

    integral, err = integrate.quad(f, -1, 1)

    print("Значение интеграла: ", integral)

    x = []
    y = []
    h = -1

    while h <= 1:
        x.append(h)
        y.append(f(h))
        h += 0.01

    plt.title(f"График функции")
    plt.grid()
    plt.xlabel("Значения x")
    plt.ylabel("Значения функции f(x)")
    plt.plot(x, y, 'b-')
    plt.show()


def task4_2():

    # 11 вариант
    def f(x):
        return (x**2)*sp.atan(x)

    x = sp.symbols('x')

    integral = sp.integrate(f(x), x)

    print("Неопределенный интеграл равен: ", integral)

task4_1()
task4_2()