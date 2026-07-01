"""
Simulated annealing escaping local minima.

We run the Metropolis algorithm on a rugged 1-D energy landscape while slowly
lowering the temperature on a geometric cooling schedule. At high temperature
the chain accepts uphill moves readily and hops freely between wells; as the
temperature drops it is increasingly confined to low-energy regions, until it
settles into the global minimum. Starting the chain in a shallow *local* well
on the far left makes the escape visible.

Output: simulated-annealing.png --- (1) the energy landscape with the chain's
trajectory colored by iteration, (2) the chain's position over time relaxing to
the global minimum, (3) the geometric cooling schedule.
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

BLUE, RED, GOLD = "#2166ac", "#b2182b", "#f0a202"

# --- A rugged landscape: a mild quadratic bowl dotted with Gaussian wells of
#     varying depth. The deepest well (the global minimum) sits near x = 1. ---
centers = np.array([-6.0, -3.0, 1.0, 5.0])
depths = np.array([1.0, 1.6, 3.0, 1.4])
widths = np.array([0.9, 0.9, 0.9, 0.9])


def energy(x):
    x = np.asarray(x, dtype=float)
    wells = sum(d * np.exp(-((x - c) ** 2) / (2 * w ** 2))
                for c, d, w in zip(centers, depths, widths))
    return 0.03 * x ** 2 - wells


# --- Simulated annealing (Metropolis moves + geometric cooling) ---
n_steps = 4000
T0, alpha = 2.5, 0.9985
x = -6.0                          # start in a shallow local well, far from the global min
E = energy(x)
xs, Es, Ts = np.empty(n_steps), np.empty(n_steps), np.empty(n_steps)
T = T0
for k in range(n_steps):
    x_prop = x + np.random.normal(0.0, 1.2)
    E_prop = energy(x_prop)
    if E_prop < E or np.random.rand() < np.exp(-(E_prop - E) / T):
        x, E = x_prop, E_prop
    xs[k], Es[k], Ts[k] = x, E, T
    T *= alpha

# Evaluate the curve over a wide range so it sits beneath even the chain's
# early high-temperature excursions; the view is focused on the wells below.
grid = np.linspace(-14, 14, 1200)
Eg = energy(grid)
x_star = grid[np.argmin(Eg)]      # global minimum location (for reference lines)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5))

# (1) Landscape with the trajectory colored by iteration.
ax1.plot(grid, Eg, color="0.4", lw=1.5, zorder=1)
sc = ax1.scatter(xs, Es, c=np.arange(n_steps), cmap="viridis", s=10,
                 alpha=0.7, zorder=2)
ax1.plot(x_star, energy(x_star), marker="*", color=GOLD, markersize=20,
         markeredgecolor="k", markeredgewidth=0.5, zorder=3, label="global minimum")
ax1.set_title("Energy landscape and the chain's path", fontsize=12)
ax1.set_xlabel("$x$")
ax1.set_ylabel("energy $E(x)$")
ax1.set_xlim(-9.5, 9.5)
ax1.set_ylim(-3.6, 6.0)
ax1.grid(True, alpha=0.3)
ax1.legend(loc="upper center", fontsize=9)
cbar = fig.colorbar(sc, ax=ax1, fraction=0.046, pad=0.04)
cbar.set_label("iteration")

# (2) The chain's position over time, relaxing onto the global minimum.
ax2.plot(xs, color=BLUE, lw=0.8, alpha=0.9)
ax2.axhline(x_star, color=GOLD, ls="--", lw=1.5, label="global minimum")
ax2.set_title("Position relaxes to the global minimum", fontsize=12)
ax2.set_xlabel("iteration")
ax2.set_ylabel("position $x$")
ax2.grid(True, alpha=0.3)
ax2.legend(loc="upper right", fontsize=9)

# (3) The geometric cooling schedule, with the chain's energy on a twin axis.
ax3.plot(Ts, color=RED, lw=1.8, label="temperature")
ax3.set_yscale("log")
ax3.set_title("Cooling schedule and energy", fontsize=12)
ax3.set_xlabel("iteration")
ax3.set_ylabel("temperature $T$", color=RED)
ax3.tick_params(axis="y", labelcolor=RED)
ax3.grid(True, alpha=0.3, which="both")
ax3b = ax3.twinx()
ax3b.plot(Es, color=BLUE, lw=0.8, alpha=0.8)
ax3b.axhline(energy(x_star), color=GOLD, ls="--", lw=1.5)
ax3b.set_ylabel("energy $E(x_t)$", color=BLUE)
ax3b.tick_params(axis="y", labelcolor=BLUE)

fig.suptitle("Simulated annealing: cooling a Metropolis chain onto the global minimum",
             fontsize=13)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("simulated-annealing.png", dpi=300, bbox_inches="tight")
plt.close()
print(f"Saved simulated-annealing.png   final x = {xs[-1]:.3f}  (global min at x = {x_star:.3f})")
