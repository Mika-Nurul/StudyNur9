import numpy as np
import matplotlib.pyplot as plt
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])
n = len(x)
def l(i, xo):
    res = 1
    for j in range(n):
        if (j==i):
            continue
        res *= (xo-x[j]) / (x[i] - x[j])
    return res
def L(x):
    res = 0
    for i in range(n):
        res += y[i]*l(i,x)
    return res

z = np.linspace(0, 4, 100)
plt.plot(z, L(z))

plt.show()
