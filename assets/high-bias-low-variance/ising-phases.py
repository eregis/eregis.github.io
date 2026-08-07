"""
Two 40x40 Ising configurations, one from each side of the phase transition.

The 2D Ising model, H = -J sum_{<ij>} s_i s_j (J = k_B = 1) on a periodic
L x L lattice, orders below the Onsager critical temperature
T_c = 2 / ln(1 + sqrt(2)) ~= 2.269 and is disordered above it. A human
glancing at either configuration below can name its phase immediately --
one is a near-uniform block of a single color pierced by a few small
minority-spin droplets, the other is uncorrelated salt-and-pepper noise.
That "immediately" is the puzzle Mehta et al. pose: what does a machine
have to learn to make the same call? Both configurations are drawn from
the same 40x40, periodic-boundary, Metropolis-sampled family as the
dataset in Mehta's notes.

Equilibration: both chains run for several thousand full-lattice
(checkerboard) sweeps. The T = 1.5 chain is started cold, from the
all-up configuration, rather than from a random one -- deep in the
ordered phase, single-spin-flip dynamics only ever has to nucleate and
heal small droplets, never erase a system-spanning domain wall, so it
equilibrates fast. (A random start can instead freeze into a multi-domain
state that local-update Metropolis will not mix out of on any reasonable
time scale.) The T = 3.5 chain, well above T_c with no metastability to
worry about, is started from a random configuration.

Output: assets/high-bias-low-variance/ising-phases.png
"""
import numpy as np
import matplotlib.pyplot as plt

L = 40                                   # lattice is L x L, periodic BCs
J = 1.0                                  # ferromagnetic coupling, k_B = 1
T_C = 2.0 / np.log(1.0 + np.sqrt(2.0))   # Onsager critical temperature ~= 2.269
T_LO, T_HI = 1.5, 3.5                    # ordered / disordered example temperatures
N_SWEEPS = 5000                          # full-lattice sweeps for equilibration


def checkerboard_sweep(spins, T, rng):
    """One full-lattice Metropolis sweep.

    Sites are two-colored like a checkerboard: on the square lattice with
    nearest-neighbor coupling, every site of one color is flanked only by
    sites of the other color, so an entire color can be updated at once
    with no conflicts -- a standard vectorization of single-spin-flip
    Metropolis dynamics.
    """
    Lx = spins.shape[0]
    i, j = np.indices((Lx, Lx))
    checker = (i + j) % 2
    for color in (0, 1):
        neighbor_sum = (np.roll(spins, 1, axis=0) + np.roll(spins, -1, axis=0)
                         + np.roll(spins, 1, axis=1) + np.roll(spins, -1, axis=1))
        dE = 2.0 * J * spins * neighbor_sum
        flip = (checker == color) & ((dE <= 0)
                                      | (rng.random((Lx, Lx)) < np.exp(-dE / T)))
        spins[flip] *= -1
    return spins


def sample_configuration(T, start, rng, n_sweeps=N_SWEEPS):
    spins = start.copy()
    for _ in range(n_sweeps):
        checkerboard_sweep(spins, T, rng)
    return spins


rng_lo = np.random.default_rng(0)
rng_hi = np.random.default_rng(1)

start_lo = np.ones((L, L))                            # cold start: all spins up
start_hi = rng_hi.choice([-1.0, 1.0], size=(L, L))     # random start

config_lo = sample_configuration(T_LO, start_lo, rng_lo)
config_hi = sample_configuration(T_HI, start_hi, rng_hi)

fig, (ax_lo, ax_hi) = plt.subplots(1, 2, figsize=(9, 4.7))

panels = ((ax_lo, config_lo, T_LO, "ordered"), (ax_hi, config_hi, T_HI, "disordered"))
for ax, config, T, phase in panels:
    ax.imshow(config, cmap="binary", vmin=-1, vmax=1, interpolation="nearest")
    ax.set_title(f"$T = {T:g}$ ({phase})", fontsize=13)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal")

fig.suptitle(rf"$40\times 40$ Ising configurations, Metropolis-sampled "
             rf"($T_c \approx {T_C:.3f}\,J/k_B$)", fontsize=13)
plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig("assets/high-bias-low-variance/ising-phases.png", dpi=150,
            bbox_inches="tight")
plt.close()

m_lo, m_hi = config_lo.mean(), config_hi.mean()
print("saved assets/high-bias-low-variance/ising-phases.png")
print(f"T = {T_LO} (ordered):    m = {m_lo:+.3f}")
print(f"T = {T_HI} (disordered): m = {m_hi:+.3f}")
