import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

X = np.array([1.019, 0.2746, 2.589, 2.286, 8.622, 0.4762, 0.5618, 0.8501, 9.625, 8.786])
Y = np.array([3.443, 2.335, -7.057, -7.238, -13.62, 3.598, 3.947, 4.108, -7.672, -13.57])

linspline = interpolate.interp1d(X, Y)
quadspline = interpolate.interp1d(X, Y, kind="quadratic")
cubespline = interpolate.interp1d(X, Y, kind="cubic")

x = np.linspace(min(X), max(X), num=100, endpoint=True)

plt.plot(x, linspline(x), '-', x, quadspline(x), '--', x, cubespline(x), ':')
plt.legend(['linear','quadratic', 'cubic'], loc='best')
plt.show()