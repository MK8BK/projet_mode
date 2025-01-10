import numpy as np
import matplotlib.pyplot as plt
from problem import f
from stability import equilibrium_points

# inspire en grande partie de 
# https://matplotlib.org/stable/gallery/mplot3d/lorenz_attractor.html


def plot_trajectory_around(equilibrium, show=True, ax=None, dt=1e-4,\
        nbsteps=int(1e6), nbstart=8, std=0.01):
    x, y, z = equilibrium
    # puisque les equilibres sont instables, on peut demarer 
    # tres proche de l'equilibre pour explorer le comportement autour
    disturb = lambda: np.random.normal(scale=std)
    if ax is None:
        ax = plt.figure().add_subplot(projection='3d')
    ax.scatter([x], [y], [z])
    for nb_starting_point in range(nbstart):
        Xs = np.empty((nbsteps+1, 3))
        Xs[0] = x+disturb(), y+disturb(), z+disturb()
        for k in range(nbsteps):
            Xs[k+1] = Xs[k] + f(Xs[k])*dt
        ax.plot(*Xs.T, lw=0.5)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.set_title('orgasme de lyapunov')
    if show:
        plt.show()
    return ax


def main():
    # parameters to view interesting dynamics for this equilibrium point
    ##plot_trajectory_around(equilibrium_points[0], dt=1e-5, nbsteps=int(1e5), nbstart=8*4, std=0.01)
    #plot_trajectory_around(equilibrium_points[0], dt=1e-5, nbsteps=int(1e5), nbstart=8*4, std=0.01)
    # commentaire:
    #           looks like a hyperbola

    # parameters to view interesting dynamics for this equilibrium point
    ##plot_trajectory_around(equilibrium_points[1], dt=1e-4, nbsteps=int(1e5), nbstart=8, std=0.02)
    plot_trajectory_around(equilibrium_points[1], dt=1e-4, nbsteps=int(1e5), nbstart=8, std=0.02)
    # commentaire: 
    #           looks like an outward spiral

    # parameters to view interesting dynamics for this equilibrium point
    ##plot_trajectory_around(equilibrium_points[2], dt=1e-3, nbsteps=int(2e4), nbstart=8*4, std=0.60)
    #plot_trajectory_around(equilibrium_points[2], dt=1e-3, nbsteps=int(2e4), nbstart=8*4, std=0.60)
    # commentaire: 
    #           double spirale, ressemble a lorentz

    # parameters to view interesting dynamics for this equilibrium point
    ##plot_trajectory_around(equilibrium_points[3], dt=1e-4, nbsteps=int(1e5), nbstart=8, std=0.02)
    #plot_trajectory_around(equilibrium_points[3], dt=1e-4, nbsteps=int(1e5), nbstart=8, std=0.02)
    # commentaire: 
    #           looks like an outward spiral

    # parameters to view interesting dynamics for this equilibrium point
    #ax = plot_trajectory_around(equilibrium_points[1], dt=1e-3, nbsteps=int(2e4), nbstart=8*2, std=0.60, show=False)
    #plot_trajectory_around(equilibrium_points[3], dt=1e-3, nbsteps=int(2e4), nbstart=8*2, std=0.60, ax=ax)
    # commentaire: 
    #           double spirale, ressemble a lorentz


if __name__=='__main__':
    main()



