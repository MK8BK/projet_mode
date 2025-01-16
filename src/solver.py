import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from problem import f, a, b, c, d
from stability import equilibrium_points


def solutions(X0, tmax=5, graph=True):
    t = np.linspace(0, tmax, int(1e6))
    sol = odeint(f, X0, t)
    x = sol[:, 0]
    y = sol[:, 1]
    z = sol[:, 2]
    return t, x, y, z

def graph2d_solution(t, x, y, z, x0, y0, z0):
    fig, axs = plt.subplots(2, 2)
    fig.suptitle(f'Solutions: $a$={a:.2f} $b$={b:.2f} $c$={c:.2f} $d$={d:.2f}'+
            f' $x_0$={x0:.2f} $y_0$={y0:.2f} $z_0$={z0:.2f}')
    axs[0, 0].plot(t, x, label='x(t)')
    axs[0, 0].set_title('x(t)')
    axs[0, 1].plot(t, y, label='y(t)')
    axs[0, 1].set_title('y(t)')
    axs[1, 0].plot(t, z, label='z(t)')
    axs[1, 0].set_title('z(t)')
    for row in axs:
        for ax in row:
            ax.legend(loc='best')
            ax.set_xlabel('t')
            ax.grid()
    axs[1, 1].remove()
    plt.show()

def graph3d_solution(x, y, z, x0, y0, z0, ax=None, show=True):
    if ax is None:
        ax = plt.figure().add_subplot(projection='3d')
    # Prepare arrays x, y, z
    #print(type(ax))
    ax.plot(x, y, z, label='solution')
    ax.set_title(f'Solutions: $a$={a:.2f} $b$={b:.2f} $c$={c:.2f} $d$={d:.2f}'+
            f' $x_0$={x0:.2f} $y_0$={y0:.2f} $z_0$={z0:.2f}')
    ax.legend()
    if show:
        plt.show()
    return ax

def graph_solution(X0):
    t, x, y, z = solutions(X0)
    graph3d_solution(x, y, z, *X0)
    graph2d_solution(t, x, y, z, *X0)

def main():
    x0bar, x1bar, x2bar, x3bar = equilibrium_points
    #graph_solution(x0bar)
    #graph_solution(x1bar)
    #graph_solution(x2bar)
    #graph_solution(x3bar)
    graph_solution([1, 1, 1])
    #graph_solution([-1, 2, -0.5])

if __name__=="__main__":
    main()

def vary_x():
    X0 = [1, 1, 1]  # conditions initiales
    t, x, y, z = solutions(X0)
    ax = graph3d_solution(x, y, z, *X0, show=False)
    for x0 in np.linspace(0, 10, 10):
        X0 = [x0, 2, -0.5]  # conditions initiales
        _, x, y, z = solutions(X0)
        graph3d_solution(x, y, z, *X0, ax=ax, show=False)
    plt.show()

