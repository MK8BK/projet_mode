import numpy as np

a = 0.9
b = 0.2
c = 1.2
d = 0.02


def f(X, a=a, b=b, c=c, d=d):
    x, y, z = X
    dx = z + (y-a)*x
    dy = 1 - b*y - x**2
    dz = -x - c*z - d*z**2
    return np.array([dx, dy, dz])

# on aurait aussi pu factoriser f en [f1,f2,f3]

def f1(x, y, z, *, a=a, b=b, c=c, d=d):
    dx = z + np.multiply(y-a, x)
    return dx


def f2(x, y, z, *, a=a, b=b, c=c, d=d):
    dy = 1 - b*y - np.multiply(x, x)
    return dy


def f3(x, y, z, *, a=a, b=b, c=c, d=d):
    dz = -x - c*z - d*np.multiply(z, z)
    return dz
