# %%
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

from maths_765_graphs import cm
from maths_765_graphs.models.oregonator import N_u, N_w, mu, par

fig = plt.figure(constrained_layout=True)
spec = gridspec.GridSpec(ncols=1, nrows=3, figure=fig)
fig.set_size_inches([19.58 * cm, 15.88 * cm])
i = 0
f_vals = [0.25, 1, 4]
w_high = [1.2, 0.35, 0.095]
for i in range(3):
    f = f_vals[i]
    par["f"] = f
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

    """
    Figure settings
    """
    ax = fig.add_subplot(spec[i, 0])

    ax.plot(Nu[0], Nu[1], color="C1")
    ax.plot(Nw[0], Nw[1], color="C2")
    ulim = [0, 1.0]
    wlim = [0.0, w_high[i]]
    ax.set_xlim([ulim[0], ulim[-1]])
    ax.set_xticks(ulim)
    ax.set_ylim(wlim[0], wlim[-1])
    ax.set_yticks(wlim)

    ax.set_ylabel(r"$u$")
    ax.set_xlabel(r"$w$")

fig.savefig("oregonator_graphs/oregonator_phaseplane.png", transparent=True, dpi=300)
