"""
Hopfield network as a dissipative dynamical system.

A Hopfield network stores binary patterns as the local minima of an energy
function E(s) = -1/2 s^T W s. Starting from a corrupted pattern, the network
updates one neuron at a time, and each update can only lower (or hold) the
energy. The trajectory therefore slides "downhill" until it settles into the
nearest stored memory --- a clean illustration of optimization as a ball
rolling downhill and coming to rest at the bottom.

Output: hopfield_visualization.png (stored | corrupted | recovered, plus the
energy descending over the course of the relaxation).
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

np.random.seed(7)

GRID = 10  # patterns live on a 10x10 grid -> N = 100 neurons


def pattern(rows):
    """Turn an ASCII bitmap ('#' = on, '.' = off) into a +/-1 vector."""
    grid = np.array([[1 if c == '#' else -1 for c in row] for row in rows])
    return grid.reshape(-1)


# Three stored memories: the letters C, P, T on a 10x10 grid.
C = pattern([
    "..######..",
    ".########.",
    "##......##",
    "##........",
    "##........",
    "##........",
    "##........",
    "##......##",
    ".########.",
    "..######..",
])
P = pattern([
    "########..",
    "#########.",
    "##......##",
    "##......##",
    "#########.",
    "########..",
    "##........",
    "##........",
    "##........",
    "##........",
])
T = pattern([
    "##########",
    "##########",
    "....##....",
    "....##....",
    "....##....",
    "....##....",
    "....##....",
    "....##....",
    "....##....",
    "....##....",
])

memories = np.stack([C, P, T])
N = memories.shape[1]

# Hebbian (outer-product) learning rule with a zero diagonal.
W = (memories.T @ memories) / N
np.fill_diagonal(W, 0.0)


def energy(s):
    return -0.5 * s @ W @ s


# Corrupt the target memory (C) by flipping ~28% of its pixels at random.
target = C.copy()
state = target.copy()
flip = np.random.rand(N) < 0.28
state[flip] *= -1
corrupted = state.copy()

# Asynchronous relaxation: update one random neuron at a time and record the
# energy after every update so we can watch it descend.
energies = [energy(state)]
rng_order = np.random.permutation(N)
sweeps = 6
for _ in range(sweeps):
    for i in np.random.permutation(N):
        state[i] = 1 if W[i] @ state >= 0 else -1
        energies.append(energy(state))
recovered = state.copy()

# ---- Figure: stored | corrupted | recovered, with energy descent below ----
fig = plt.figure(figsize=(10, 7))
gs = GridSpec(2, 3, height_ratios=[2, 1.3], hspace=0.35, wspace=0.15)

panels = [
    ("Stored memory", target),
    ("Corrupted input", corrupted),
    ("Recovered state", recovered),
]
for col, (title, vec) in enumerate(panels):
    ax = fig.add_subplot(gs[0, col])
    ax.imshow(vec.reshape(GRID, GRID), cmap="binary", vmin=-1, vmax=1)
    ax.set_title(title, fontsize=12)
    ax.set_xticks([])
    ax.set_yticks([])

ax_e = fig.add_subplot(gs[1, :])
ax_e.plot(energies, color="#b2182b", lw=2)
ax_e.set_xlabel("neuron update")
ax_e.set_ylabel("energy  $E = -\\frac{1}{2}\\, s^\\top W s$")
ax_e.set_title("The network slides downhill until it settles in a stored memory",
               fontsize=11)
ax_e.grid(True, alpha=0.3)

mismatch = int(np.sum(recovered != target))
fig.suptitle(
    f"A Hopfield network recovering a corrupted pattern "
    f"({mismatch} of {N} pixels wrong after relaxation)",
    fontsize=13)

plt.savefig("hopfield_visualization.png", dpi=300, bbox_inches="tight")
plt.close()
print("The plot has been saved as 'hopfield_visualization.png'")
print(f"Pixels still wrong after relaxation: {mismatch} / {N}")
