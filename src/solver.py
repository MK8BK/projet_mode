import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from problem import f, a, b, c, d


def solutions(X0, tmax=5, graph=True):
    t = np.linspace(0, tmax, int(1e6))
    sol = odeint(f, X0, t)
    x = sol[:, 0]
    y = sol[:, 1]
    z = sol[:, 2]
    return t, x, y, z

def graph_solution(t, x, y, z):
    fig, axs = plt.subplots(2, 2)
    fig.suptitle(f'Solutions: a={a:.2f} b={b:.2f} c={c:.2f} d={d:.2f}')
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

def graph3d_solution(x, y, z, ax=None, show=True):
    if ax is None:
        ax = plt.figure().add_subplot(projection='3d')
    # Prepare arrays x, y, z
    #print(type(ax))
    ax.plot(x, y, z, label='solution')
    ax.legend()
    if show:
        plt.show()
    return ax

def vary_x():
    X0 = [-1, 2, -0.5]  # conditions initiales
    t, x, y, z = solutions(X0)
    ax = graph3d_solution(x, y, z, show=False)
    for x0 in np.linspace(0, 10, 10):
        X0 = [x0, 2, -0.5]  # conditions initiales
        _, x, y, z = solutions(X0)
        graph3d_solution(x, y, z, ax=ax, show=False)
    plt.show()


def main():
    #vary_x()

    from stability import equilibrium_points
    x0bar, x1bar, x2bar, x3bar = equilibrium_points
    X0 = [1, 1, 1]  # conditions initiales

    X0 = [x+np.random.normal() for x in x2bar]

    t, x, y, z = solutions(X0)
    graph3d_solution(x, y, z)
    graph_solution(t, x, y, z)



if __name__=="__main__":
    main()


