import numpy as np
import matplotlib.pyplot as plt
from problem import f, f1, f2, f3
from stability import equilibrium_points


def plot_trajectory_around(equilibrium, eqname, show=True, ax=None, dt=1e-4,
                           nbsteps=int(1e6), nbstart=8, std=0.01, eqcolor='r', title=""):
    # inspiree en grande partie de
    # https://matplotlib.org/stable/gallery/mplot3d/lorenz_attractor.html
    x, y, z = equilibrium
    # puisque les equilibres sont instables, on peut demarer
    # tres proche de l'equilibre pour explorer le comportement autour
    def disturb(): return np.random.normal(scale=std)
    if ax is None:
        # permet de composer plusieur points d'eq sur une meme figure
        ax = plt.figure().add_subplot(projection='3d')
    ax.scatter([x], [y], [z], color=eqcolor, label=eqname)
    ax.legend()
    for nb_starting_point in range(nbstart):
        Xs = np.empty((nbsteps+1, 3))
        Xs[0] = x+disturb(), y+disturb(), z+disturb()
        for k in range(nbsteps):
            Xs[k+1] = Xs[k] + f(Xs[k])*dt
        ax.plot(*Xs.T, 'b', lw=0.5)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.set_title(title)
    if show:
        plt.show()
    return ax


def plot3_axes_phase(equilibrium, title="", halfrange=3):
    # cette fonction pourrait etre factorisee plus succintement, mais ce n'est pas
    # prioritaire: NE PAS LIRE
    x, y, z = equilibrium
    n = 30
    Xrange = np.linspace(x-halfrange, x+halfrange, n)
    Yrange = np.linspace(y-halfrange, y+halfrange, n)
    Zrange = np.linspace(z-halfrange, z+halfrange, n)
    cstz = np.full((n, n), z)
    csty = np.full((n, n), y)
    cstx = np.full((n, n), x)
    # y = f(x)
    Xpz, Ypz = np.meshgrid(Xrange, Yrange)
    Upz = f1(Xpz, Ypz, cstz)
    Vpz = f2(Xpz, Ypz, cstz)
    normZcut = np.sqrt(Upz*Upz+Vpz*Vpz)
    Upz = Upz / normZcut
    Vpz = Vpz / normZcut
    # z = f(x)
    Xpy, Zpy = np.meshgrid(Xrange, Zrange)
    Upy = f1(Xpy, Zpy, csty)
    Vpy = f2(Xpy, Zpy, csty)
    normYcut = np.sqrt(Upy*Upy+Vpy*Vpy)
    Upy = Upy / normYcut
    Vpy = Vpy / normYcut
    # z = f(y)
    Ypx, Zpx = np.meshgrid(Yrange, Zrange)
    Upx = f1(Ypx, Zpx, cstx)
    Vpx = f2(Ypx, Zpx, cstx)
    normXcut = np.sqrt(Upx*Upx+Vpx*Vpx)
    Upx = Upx / normXcut
    Vpx = Vpx / normXcut
    # debut des graphismes
    fig, axs = plt.subplots(2, 2)
    axs[1][1].remove()
    ax0, ax1, ax2 = axs[0][0], axs[0][1], axs[1][0]
    # y = f(x)
    ax0.scatter([x], [y])
    ax0.set_xlabel("x")
    ax0.set_ylabel("y")
    q = ax0.quiver(Xpz, Ypz, Upz, Vpz, normZcut, cmap="plasma")
    fig.colorbar(q, ax=ax0)
    # z = f(x)
    ax1.scatter([x], [z])
    ax1.set_xlabel("x")
    ax1.set_ylabel("z")
    q = ax1.quiver(Xpy, Zpy, Upy, Vpy, normYcut, cmap="plasma")
    fig.colorbar(q, ax=ax1)
    # z = f(y)
    ax2.scatter([y], [z])
    ax2.set_xlabel("y")
    ax2.set_ylabel("z")
    q = ax2.quiver(Ypx, Zpx, Upx, Vpx, normXcut, cmap="plasma")
    fig.colorbar(q, ax=ax2)
    # affichage
    fig.suptitle(title)
    plt.show()


def main():
    x0bar, x1bar, x2bar, x3bar = equilibrium_points
    def see_x0bar():
        # parameters to view interesting dynamics for this equilibrium point
        # config
        plot_trajectory_around(x0bar, r"$\overline{x}_0$", dt=1e-5, nbsteps=int(1e5),
                               nbstart=8*4, std=0.04, title=r"$\overline{x}_0$")
    def see_x123bar():
        # parameters to view interesting dynamics for these three equilibrium points
        # config
        ax = plot_trajectory_around(x1bar, r"$\overline{x}_1$", dt=1e-3, nbsteps=int(2e4),
                                    nbstart=8*2, std=0.60, show=False, eqcolor='darkviolet')
        ax = plot_trajectory_around(x2bar, r"$\overline{x}_2$", dt=1e-3, nbsteps=int(2e4),
                                    nbstart=8*2, std=0.60, show=False, ax=ax, eqcolor="goldenrod")
        plot_trajectory_around(x3bar, r"$\overline{x}_3$",
                               dt=1e-3, nbsteps=int(2e4), nbstart=8*2, std=0.60, ax=ax, eqcolor="crimson",
                               title=r"Dynamique autour de $\overline{x}_1$, $\overline{x}_2$ et $\overline{x}_3$")

    # Afin de generer des diagrammes du rapport,
    # decommenter une seule de ces lignes et executez ce fichier

    # see_x0bar() # pas tres utile, voir diagramme de phase 2D
    # see_x123bar()
    # plot3_axes_phase(x0bar, title=r"Dynamique autour de $\overline{x}_0$", halfrange=5)
    # plot3_axes_phase(x2bar, title=r"Dynamique autour de $\overline{x}_2$", halfrange=5)
    plot3_axes_phase(x1bar, title=r"Dynamique autour de $\overline{x}_1$", halfrange=5)
    # plot3_axes_phase(x3bar, title=r"Dynamique autour de $\overline{x}_3$", halfrange=5)


if __name__ == '__main__':
    main()
