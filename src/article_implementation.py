import numpy as np
from scipy.integrate import quad

default_n = 5


def dot_product(f, g):
    two_over_pi = (2./np.pi)
    integral = quad(lambda x: f(x)*g(x)/np.sqrt(1-x**2), -1, 1)[0]
    return two_over_pi*integral


def get_tchebyshev(n):
    """ domaine [-1, 1]"""
    return lambda x: np.cos(n*np.arccos(x))


def get_spectral_representation(f, n=default_n):
    """ f:[-1,1]->R continuous """
    # 0 to n inclusive, see paper
    c = np.zeros(n+1)
    for k in range(n+1):
        Tk = get_tchebyshev(k)
        ck = dot_product(f, Tk)
        c[k] = ck
    c[0] /= 2
    return c


def get_physical_representation(f, x0_to_xn, n=default_n):
    c = get_spectral_representation(f, n=n)
    tcheb = [get_tchebyshev(k) for k in range(n+1)]
    T = np.array([[tcheb[k](xk) for k in range(n+1)] for xk in x0_to_xn])
    v = T@c
    return v


def eval_spectral_representation(u, x):
    n = len(c) - 1
    tcheb = [get_tchebyshev(k) for k in range(n+1)]


def get_collocation_points(n=default_n):
    return np.array([-np.cos((k-0.5)*np.pi/n) for k in range(1, n+1)])


def get_derivative_matrix(np1):
    # TODO: check this, no idea how it should look
    D = np.zeros((np1, np1))
    for k in range(np1):
        for l in range(k+1, np1):
            if (l-k) % 2 != 0:
                D[k][l] = 2*k
    return D


def get_integration_matrix(np1):
    # Warning: last line is 0, if any problems arise check here
    J = np.zeros((np1, np1))
    J[0, 1] = 0.5
    for k in range(1, np1-1):
        J[k, k-1] = 1/k
        J[k, k+1] = -1/k
    return J


def main():
    print(get_derivative_matrix(default_n))
    x0_to_xn = get_collocation_points(default_n)
    print(get_spectral_representation(lambda x: 1.))  # should be 2,0,0...
    # should be 1,1,1...
    print(get_physical_representation(lambda x: 1., x0_to_xn))
    print(get_spectral_representation(lambda x: x))  # should be 2,0,0...
    # should be 1,1,1...
    print(get_physical_representation(lambda x: x, x0_to_xn))
    # should be 2,0,0...
    print(get_spectral_representation(lambda x: 2*x**2-1))
    # should be 1,1,1...
    print(get_physical_representation(lambda x: 2*x**2-1, x0_to_xn))
    # should be 2,0,0...
    print(get_spectral_representation(lambda x: 2*x**2-2))
    # should be 1,1,1...
    print(get_physical_representation(lambda x: 2*x**2-2, x0_to_xn))
    #
    print(get_integration_matrix(default_n+1))


if __name__ == "__main__":
    main()
