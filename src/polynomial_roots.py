import matplotlib.pyplot as plt
import numpy as np
from problem import a, b, c, d

np.set_printoptions(precision=16)

epsilon = 1e-12

# s stands for simple, to verify that the 
# numerical roots are in fact: roots
def sRx(z):
    return -c*z - d*z**2

def sRy(z):
    return (-d**2 / b)*z**4 + (-2*c*d/b)*z**3 + (-c**2 / b)*z**2 + (1./b)

def sP(z):
    return z + (sRy(z) - a)*sRx(z)

Rx = np.polynomial.Polynomial([0., -c, -d])
Ry = np.polynomial.Polynomial([1./b, 0, -c**2/b, -2*c*d/b, -d**2/b])
z = np.polynomial.polynomial.Polynomial.basis(1)
P = z + (Ry - a)*Rx

assert z(1) == 1
assert z(213) == 213
assert Rx(0) == 0
assert abs(Ry(0) - 1./b) < epsilon

roots = P.roots()

def main():
    print(f"a={a} b={b} c={c} d={d}")
    print(f"P(x) = {P}")
    print() # nouvelle ligne
    for root in roots:
        print(f"supposed root: z={root:.10f} : sP(z)={sP(root):.10f}")
    print("\nroots:")
    for root in roots:
        print(f"\t{root}")



if __name__=="__main__":
    main()




