#%%
from maths_765_graphs.models.lotka import lotka, N_x, N_y, eq, par
from maths_765_graphs.models import getIVP
from maths_765_graphs import add_arrow_to_line2D
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.lines as mlines
import numpy as np

# Trajectories
trajs = []
for x in [0.2, 0.3, 0.4, 0.6, 0.9]:
    ics = {
        'X': x, 
        'Y': 1
    }
    tf = 12
    traj = getIVP(lotka, par, ics, tini=0, tf=tf)
    trajs.append(traj)

# Nullclines
n = 10
x0 = np.linspace(0, 2, n)
y0 = np.linspace(0, 2, n)
Nx = N_x(x0, y0, par)
Ny = N_y(x0, y0, par)

#%%
"""
Figure settings
"""
fig = plt.figure(constrained_layout = True)
spec = gridspec.GridSpec(ncols = 1, nrows=1, figure=fig)
cm = 1/2.54
fig.set_size_inches([19.58*cm,15.88*cm])
ax = fig.add_subplot(spec[0, 0])

for traj in trajs:
    t, X, Y = traj
    line, = ax.plot(X, Y, color = 'C0')
    add_arrow_to_line2D(ax, line, arrow_locs = [0.2, 0.4, 0.6, 0.8], arrowsize=2)
ax.plot(Nx[0], Nx[1], label = 'X nullcline', color = 'C1')
ax.plot(Ny[0], Ny[1], label = 'Y nullcline', color = 'C2')

ax.set_xlim([0, 2])
ax.set_xticks([0, 1, 2])
ax.set_ylim([0, 2])
ax.set_yticks([0, 1, 2])
ax.legend()

ax.set_ylabel('Y')
ax.set_xlabel('X')

fig.savefig('Lotka_graphs/lotka_phase_plane.png',transparent=True, dpi=300)