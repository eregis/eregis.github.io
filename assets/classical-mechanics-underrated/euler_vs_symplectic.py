"""
Euler discretization vs. a symplectic integrator on a planetary orbit.

Both schemes integrate the same two-body Kepler problem (a body orbiting a
fixed mass at the origin, with an inverse-square force and GM = 1), starting
from identical initial conditions and using the same step size. The only
difference is the update rule:

  * Explicit (forward) Euler is NOT symplectic. It systematically injects
    energy into the system, so the orbit spirals outward and the energy drifts
    upward without bound.

  * Velocity Verlet (leapfrog) IS symplectic: it preserves the geometric
    structure of phase space. It does not conserve energy exactly, but the
    energy error stays bounded forever, so the orbit remains stable.

Output: euler_vs_symplectic.png --- two orbit panels plus an energy-vs-time
panel that makes the drift explicit.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Kepler dynamics: inverse-square attraction toward the origin, GM = 1 ---
def accel(r):
    return -r / np.linalg.norm(r) ** 3

def energy(r, v):
    """Total specific energy: kinetic + gravitational potential."""
    return 0.5 * np.dot(v, v) - 1.0 / np.linalg.norm(r)

# Shared initial conditions and step size (a moderately eccentric ellipse).
r0 = np.array([1.0, 0.0])
v0 = np.array([0.0, 1.2])
dt = 0.05
n_steps = 2600  # several orbital periods


def integrate(method):
    r, v = r0.copy(), v0.copy()
    traj = np.empty((n_steps + 1, 2))
    ener = np.empty(n_steps + 1)
    traj[0], ener[0] = r, energy(r, v)
    a = accel(r)
    for n in range(n_steps):
        if method == "euler":
            # Forward Euler: update position with the OLD velocity.
            r = r + dt * v
            v = v + dt * a
            a = accel(r)
        elif method == "verlet":
            # Velocity Verlet (symplectic): half-kick, drift, half-kick.
            v_half = v + 0.5 * dt * a
            r = r + dt * v_half
            a = accel(r)
            v = v_half + 0.5 * dt * a
        traj[n + 1], ener[n + 1] = r, energy(r, v)
    return traj, ener


euler_traj, euler_E = integrate("euler")
verlet_traj, verlet_E = integrate("verlet")
t = np.arange(n_steps + 1) * dt

# ------------------------------- Figure -------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

orbit_panels = [
    (axes[0], euler_traj, "Explicit Euler", "#b2182b"),
    (axes[1], verlet_traj, "Symplectic (velocity Verlet)", "#2166ac"),
]
for ax, traj, title, color in orbit_panels:
    ax.plot(traj[:, 0], traj[:, 1], color=color, lw=0.9, alpha=0.8)
    ax.plot(0, 0, marker="*", color="#f0a202", markersize=18,
            markeredgecolor="k", markeredgewidth=0.5, label="central mass")
    ax.plot(r0[0], r0[1], "o", color="k", markersize=6, label="start")
    ax.set_title(title, fontsize=12)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", fontsize=9)

# Match the orbit panels to the same window so the spiral-out is obvious.
lim = np.abs(euler_traj).max() * 1.05
for ax in axes[:2]:
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

axes[2].plot(t, euler_E, color="#b2182b", lw=1.8, label="explicit Euler")
axes[2].plot(t, verlet_E, color="#2166ac", lw=1.8, label="symplectic")
axes[2].axhline(energy(r0, v0), color="gray", ls="--", lw=1, alpha=0.7,
                label="true energy")
axes[2].set_title("Total energy over time", fontsize=12)
axes[2].set_xlabel("time")
axes[2].set_ylabel("energy  $E = \\frac{1}{2}|v|^2 - 1/|r|$")
axes[2].grid(True, alpha=0.3)
axes[2].legend(loc="upper left", fontsize=9)

fig.suptitle(
    "Same orbit, same step size: explicit Euler injects energy and spirals out, "
    "while a symplectic integrator keeps the orbit bounded",
    fontsize=13)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("euler_vs_symplectic.png", dpi=300, bbox_inches="tight")
plt.close()
print("The plot has been saved as 'euler_vs_symplectic.png'")
print(f"Final energy  ---  Euler: {euler_E[-1]:+.3f}   "
      f"symplectic: {verlet_E[-1]:+.3f}   true: {energy(r0, v0):+.3f}")
