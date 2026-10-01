#%%
from maths_765_graphs.models.brusselator import brusselator, N_x, N_y, eq, trapping_lines, trapping_lines_markers,par
from maths_765_graphs.models import getIVP
from maths_765_graphs import cm, add_arrow_to_line2D
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.lines as mlines
import numpy as np

# Nullclines
n = 200
xlim = [0.2, 5]
ylim = [0.2, 5]
x0 = np.linspace(xlim[0], xlim[-1], n)
y0 = np.linspace(ylim[0], ylim[-1], n)
Nx = N_x(x0, y0, par)
Ny = N_y(x0, y0, par)

# Trapping lines
xlim = [0, 5]
ylim = [0, 5]
x0 = np.linspace(xlim[0], xlim[-1], n)
y0 = np.linspace(ylim[0], ylim[-1], n)
trap_lines = trapping_lines(x0, y0)

"""
Figure settings
"""
fig = plt.figure(constrained_layout = True)
spec = gridspec.GridSpec(ncols = 1, nrows=1, figure=fig)
fig.set_size_inches([19.58*cm,15.88*cm])
ax = fig.add_subplot(spec[0, 0])

for line in trap_lines:
    X, Y = line
    line, = ax.plot(X, Y, color = 'C1')
i = 1
for marker in trapping_lines_markers():
    X, Y = marker
    ax.text(X, Y, 'L' + str(i))
    i+= 1
ax.plot(Nx[0], Nx[1], label = 'X nullcline', color = 'C7')
ax.plot(Ny[0], Ny[1], label = 'Y nullcline', color = 'C7')
xlim = [0, 5]
ylim = [0, 4.75]
ax.set_xlim([xlim[0], xlim[-1]])
ax.set_xticks(xlim)
ax.set_ylim(ylim[0], ylim[-1])
ax.set_yticks(ylim)
ax.legend()

ax.set_ylabel('Y')
ax.set_xlabel('X')

fig.savefig('brusselator_graphs/brusselator_trapping.png',transparent=True, dpi=300)