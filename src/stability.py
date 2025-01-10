import numpy as np
from polynomial_roots import (
        roots,
        epsilon,
        a, b, c, d,
        Rx, Ry,
)
from numpy import linalg as LA

# garder les racines utiles
roots = roots[abs(roots.imag)<epsilon].real

equilibrium_points = [(Rx(z), Ry(z), z) for z in roots]

def Ak(xbar, ybar, zbar):
    return np.array([
            [ybar - a, xbar, 1],
            [-2*xbar, -b, 0],
            [-1, 0, -c-2*d*zbar],
        ])

evolution_matrices = [Ak(*z) for z in equilibrium_points]

eigen_values = [LA.eig(matrix)[0] for matrix in evolution_matrices]

def main():
    for lambdas in eigen_values:
        print(lambdas)

if __name__=="__main__":
    main()



