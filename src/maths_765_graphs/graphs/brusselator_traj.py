#%%
from maths_765_graphs.models.brusselator import brusselator, N_x, N_y, eq, trapping_lines, par
from maths_765_graphs.models import getIVP
from maths_765_graphs import cm, add_arrow_to_line2D
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.lines as mlines
import numpy as np

# Trajectories
trajs = []
rng = np.random.default_rng()
low = 0
high = 3
n_traj = 5
x = rng.uniform(low, high, size=n_traj)
y = rng.uniform(low, high, size=n_traj)

for i in range(n_traj):
    ics = {
        'X': x[i], 
        'Y': y[i]
    }
    tf = 6
    traj = getIVP(brusselator, par, ics, tini=0, tf=tf)
    trajs.append(traj)
t, X, Y = traj

# Nullclines
n = 200
xlim = [0.2, 5]
ylim = [0.2, 5]
x0 = np.linspace(xlim[0], xlim[-1], n)
y0 = np.linspace(ylim[0], ylim[-1], n)
Nx = N_x(x0, y0, par)
Ny = N_y(x0, y0, par)

"""
Figure settings
"""
fig = plt.figure(constrained_layout = True)
spec = gridspec.GridSpec(ncols = 1, nrows=1, figure=fig)
fig.set_size_inches([19.58*cm,15.88*cm])
ax = fig.add_subplot(spec[0, 0])

for traj in trajs:
    t, X, Y = traj
    ax.plot(X[0], Y[0], color = 'C4', marker='o', markersize=10)
    line, = ax.plot(X, Y, color = 'C0')
    add_arrow_to_line2D(ax, line, arrow_locs = [0.2, 0.4, 0.6, 0.8], arrowsize=2)
ax.plot(Nx[0], Nx[1], label = 'X nullcline', color = 'C1')
ax.plot(Ny[0], Ny[1], label = 'Y nullcline', color = 'C2')
ax.plot([0, 4], [0.01,0.01], color = 'C2', lw = 2)
xlim = [0, 4]
ylim = [0, 4]
ax.set_xlim([xlim[0], xlim[-1]])
ax.set_xticks(xlim)
ax.set_ylim(ylim[0], ylim[-1])
ax.set_yticks(ylim)
ax.legend()

ax.set_ylabel('Y')
ax.set_xlabel('X')

fig.savefig('brusselator_graphs/brusselator_phase_plane.png',transparent=True, dpi=300)