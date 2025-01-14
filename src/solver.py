import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

y0 = [1, 1, 1]  # conditions initiales
a = 0.9
b = 0.2
c = 1.2
h = 0.


def chaotic_finance_system(v, t, a, b, c, h):
    x, y, z = v
    dvdt = [z+(y-a)*x, 1-b*y-x**2, -x-c*z+h*z**2]
    return dvdt


def solutions(graph=True):
    t = np.linspace(0, 6, 1200)
    sol = odeint(chaotic_finance_system, y0, t, args=(a, b, c, h))
    x = sol[:, 0]
    y = sol[:, 1]
    z = sol[:, 2]
    if graph:
        fig, axs = plt.subplots(2, 2)
        fig.suptitle(f'Solutions: a={a:.1f} b={b:.1f} c={c:.1f} h={h:.1f}')
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
    return x, y, z


def phase_graph():
    x_arange = np.linspace(-3, 3, 400)
    y_arange = np.linspace(-1, 4, 400)
    z_arange = np.linspace(-1.5, 2, 400)

    fig, axs = plt.subplots(2, 2)
    axs[1, 1].remove()

    # rappel: dvdt = [zvalues+(yvalues-a)*xvalues, 1-b*y-x**2, -x-c*z+h*z**2]

    xvalues, yvalues = np.meshgrid(x_arange, y_arange)
    zvalues = -0.2
    axs[0, 0].streamplot(xvalues, yvalues, zvalues+(yvalues-a)
                         * xvalues, 1-b*yvalues-xvalues**2, density=2.5)
    axs[0, 0].grid()
    axs[0, 0].set_title('xy')

    xvalues, zvalues = np.meshgrid(x_arange, z_arange)
    yvalues = 1.75
    axs[0, 1].streamplot(xvalues, zvalues, zvalues+(yvalues-a)
                         * xvalues, -xvalues-c*zvalues+h*zvalues**2, density=2.5)
    axs[0, 1].grid()
    axs[0, 1].set_title('xz')

    yvalues, zvalues = np.meshgrid(y_arange, z_arange)
    xvalues = -0.5
    axs[1, 0].streamplot(yvalues, zvalues, 1-b*yvalues-xvalues **
                         2, -xvalues-c*zvalues+h*zvalues**2, density=2.5)
    axs[1, 0].grid()
    axs[1, 0].set_title('yz')
    plt.show()


# x, y, z = solutions_graph()
# plt.plot(y, z, 'r')
# plt.show()
phase_graph()
