# %%
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

from maths_765_graphs import add_arrow_to_line2D, cm
from maths_765_graphs.models import getIVP
from maths_765_graphs.models.oregonator import N_u, N_w, eps, f, mu, oregonator, par

# Nullclines
n = 350
ulim = [mu + 1e-8, 1.0]
wlim = [0.0, 0.35]
w0 = np.linspace(wlim[0], wlim[-1], n)
u0 = np.linspace(ulim[0], ulim[-1], n)
Nu = N_u(u0, w0, par)
ulim = [0, 1.0]
u0 = np.linspace(ulim[0], ulim[-1], n)
Nw = N_w(u0, w0, par)

# Trajectories
trajs = []
eps_vals = [eps, 1e-8]
tf = 6
for eps_val in eps_vals:
    par["epsilon"] = eps_val
    ics = {"u": 0.3, "v": 0.3}
    traj = getIVP(oregonator, par, ics, tini=0, tf=1)
    ics = {"u": traj[1][-1], "v": traj[2][-1]}
    traj = getIVP(oregonator, par, ics, tini=0, tf=tf)
    trajs.append(traj)

# Relax oscillator points
sq = 1 + np.sqrt(2)
# A = [1-6*mu, sq**2*mu/f]
A = [1 - 6 * mu, N_u(1 - 6 * mu, 0, par)[1]]
B = [0.5 - mu, N_u(0.5 - mu, 0, par)[1]]
C = [(1 + 8 * mu) * mu, 1 / (f * 4) + mu / f]
D = [sq * mu, N_u(1 - 6 * mu, 0, par)[1]]

"""
Figure settings
"""
fig = plt.figure(constrained_layout=True)
spec = gridspec.GridSpec(ncols=1, nrows=1, figure=fig)
fig.set_size_inches([19.58 * cm, 15.88 * cm])
ax = fig.add_subplot(spec[0, 0])

ax.plot(Nu[0], Nu[1], color="C1")
ax.plot(Nw[0], Nw[1], color="C2")
for i in range(2):
    t, u, w = trajs[i]
    (line,) = ax.plot(
        u, w, label=r"$\epsilon = $" + f"{eps_vals[i]:.1e}", color="C" + str(4 * i + 0)
    )
    if i == 0:
        add_arrow_to_line2D(ax, line, arrow_locs=[0.2, 0.4, 0.6, 0.8], arrowsize=2)
nu = 0.02
nw = 0.01
ax.plot(A[0], A[1], marker="o", markersize=10, color="C1")
ax.text(A[0] + nu, A[1], "A")
ax.plot(B[0], B[1], marker="o", markersize=10, color="C2")
ax.text(B[0], B[1] + nw, "B")
ax.plot(C[0], C[1], marker="o", markersize=10, color="C3")
ax.text(C[0] + nu, C[1] + nw, "C")
ax.plot(D[0], D[1], marker="o", markersize=10, color="C4")
ax.text(D[0], D[1] + nw, "D")
xlim = [0, 1]
ylim = [0.05, 0.35]
ax.set_xlim([xlim[0], xlim[-1]])
ax.set_xticks(xlim)
ax.set_ylim([ylim[0], ylim[-1]])
ax.set_yticks(ylim)
ax.legend()

fig.savefig("oregonator_graphs/oregonator_relax.png", transparent=True, dpi=300)
