import numpy as np

a = 0.9
b = 0.2
c = 1.2
d = 0.02

def f(X, *, a=a, b=b, c=c, d=d):
    x, y , z = X
    dx = z + (y-a)*x
    dy = 1 - b*y - x**2
    dz = -x -c*z - d*z**2
    return np.array([dx, dy, dz])



