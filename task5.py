import sympy as sp
from math import *

def task5():
    # 20 вариант

    x = sp.Symbol('x')
    x0 = pi/4

    f = sp.ln((sp.sqrt(4*sp.tan(x)+1) - 2*sp.sqrt(sp.tan(x)))
              /(sp.sqrt(4*sp.tan(x)+1) + 2*sp.sqrt(sp.tan(x))))

    f_diff = sp.diff(f, x)
    print("Производная функции: ", f_diff, sep='\n')
    print("Производная функции в точке х0: ", f_diff.subs(x, x0), sep='\n')
    print("Вторая производная функции в точке x0: ", f_diff.diff(x).subs(x, x0), sep='\n')


task5()


