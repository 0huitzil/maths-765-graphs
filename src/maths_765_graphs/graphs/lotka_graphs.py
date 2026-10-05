# %%
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

from maths_765_graphs import add_arrow_to_line2D, cm
from maths_765_graphs.models import getIVP
from maths_765_graphs.models.lotka import N_x, N_y, lotka, par

# Trajectories
trajs = []
for x in [0.2, 0.3, 0.4, 0.6, 0.9]:
    ics = {"X": x, "Y": 1}
    tf = 12
    traj = getIVP(lotka, par, ics, tini=0, tf=tf)
    trajs.append(traj)

# Nullclines
n = 10
xlim = [0, 2]
ylim = [0, 2]
x0 = np.linspace(xlim[0], xlim[-1], n)
y0 = np.linspace(ylim[0], ylim[-1], n)
Nx = N_x(x0, y0, par)
Ny = N_y(x0, y0, par)

"""
Figure settings
"""
fig = plt.figure(constrained_layout=True)
spec = gridspec.GridSpec(ncols=1, nrows=1, figure=fig)
fig.set_size_inches([19.58 * cm, 15.88 * cm])
ax = fig.add_subplot(spec[0, 0])

for traj in trajs:
    t, X, Y = traj
    (line,) = ax.plot(X, Y, color="C0")
    add_arrow_to_line2D(ax, line, arrow_locs=[0.2, 0.4, 0.6, 0.8], arrowsize=2)
ax.plot(Nx[0], Nx[1], label="X nullcline", color="C1")
ax.plot(Ny[0], Ny[1], label="Y nullcline", color="C2")
xlim = [0, 2]
ylim = [0, 2]
ax.set_xlim([xlim[0], xlim[-1]])
ax.set_xticks(xlim)
ax.set_ylim(ylim[0], ylim[-1])
ax.set_yticks(ylim)
ax.legend()

ax.set_ylabel("Y")
ax.set_xlabel("X")

fig.savefig("Lotka_graphs/lotka_phase_plane.png", transparent=True, dpi=300)
