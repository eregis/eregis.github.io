"""
Hamiltonian Monte Carlo vs. random-walk Metropolis on a correlated Gaussian.

HMC augments the target with an auxiliary momentum and simulates Hamiltonian
dynamics with a leapfrog (symplectic) integrator. Because the dynamics nearly
conserve energy, even long proposals are accepted with high probability: the
momentum carries the state in long, coherent arcs along the level sets of the
distribution. Random-walk Metropolis, by contrast, must take tiny isotropic
steps to be accepted at all when the target is strongly correlated, so it only
crawls. Here both methods are given a matched evaluation budget on the same
strongly correlated 2-D Gaussian.

Output: hamiltonian-monte-carlo.png --- left: HMC leapfrog arcs sweeping along
the correlation ridge with the accepted states marked; right: a random-walk
Metropolis path of matched budget barely diffusing through the same target.
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

BLUE, RED, GOLD = "#2166ac", "#b2182b", "#f0a202"

# --- Target: a strongly correlated 2-D Gaussian, U(q) = 0.5 q^T Sigma^{-1} q ---
rho = 0.95
Sigma = np.array([[1.0, rho], [rho, 1.0]])
Sigma_inv = np.linalg.inv(Sigma)


def grad_U(q):
    return Sigma_inv @ q


def U(q):
    return 0.5 * q @ Sigma_inv @ q


def leapfrog(q, p, eps, L):
    """Half-kick / full-drift / half-kick leapfrog (symplectic). Returns the
    proposed (q, p) and the full position path for plotting."""
    path = [q.copy()]
    p = p - 0.5 * eps * grad_U(q)
    for i in range(L):
        q = q + eps * p                       # mass matrix M = I
        if i != L - 1:
            p = p - eps * grad_U(q)
        path.append(q.copy())
    p = p - 0.5 * eps * grad_U(q)
    return q, p, np.array(path)


# --- HMC. eps * sqrt(largest curvature) = 0.15 * sqrt(20) ~ 0.67 < 1, so the
#     integrator is stable and energy is well conserved (high acceptance). ---
eps, L, n_iter = 0.15, 25, 15
q = np.array([-2.0, -2.0])
hmc_path = [q.copy()]
arcs = []
accepts = 0
for _ in range(n_iter):
    p0 = np.random.normal(size=2)
    q_new, p_new, path = leapfrog(q, p0, eps, L)
    H0 = U(q) + 0.5 * p0 @ p0
    H1 = U(q_new) + 0.5 * p_new @ p_new
    arcs.append(path)
    if np.random.rand() < np.exp(H0 - H1):
        q = q_new
        accepts += 1
    hmc_path.append(q.copy())
hmc_path = np.array(hmc_path)

# --- Random-walk Metropolis with a matched evaluation budget (n_iter * L). The
#     isotropic step must stay small (~ the narrow axis, sqrt(1 - rho) ~ 0.22)
#     or almost every proposal is rejected -- which is exactly the point. ---
n_rwm = n_iter * L
s = 0.2
qr = np.array([-2.0, -2.0])
rwm_path = [qr.copy()]
rwm_accepts = 0
for _ in range(n_rwm):
    q_prop = qr + s * np.random.normal(size=2)
    if np.random.rand() < np.exp(U(qr) - U(q_prop)):
        qr = q_prop
        rwm_accepts += 1
    rwm_path.append(qr.copy())
rwm_path = np.array(rwm_path)

# --- Contours of the target density for both backdrops ---
lim = 3.5
gx, gy = np.meshgrid(np.linspace(-lim, lim, 200), np.linspace(-lim, lim, 200))
pos = np.stack([gx, gy], axis=-1)
quad = np.einsum("...i,ij,...j->...", pos, Sigma_inv, pos)
dens = np.exp(-0.5 * quad)

fig, (ax_hmc, ax_rwm) = plt.subplots(1, 2, figsize=(13, 5.5))

# Left: HMC leapfrog arcs sweeping the ridge.
ax_hmc.contour(gx, gy, dens, levels=6, colors="0.6", linewidths=0.8)
for path in arcs:
    ax_hmc.plot(path[:, 0], path[:, 1], color=BLUE, lw=1.0, alpha=0.55)
ax_hmc.plot(hmc_path[:, 0], hmc_path[:, 1], color="0.35", lw=0.8, alpha=0.8, zorder=3)
ax_hmc.scatter(hmc_path[1:, 0], hmc_path[1:, 1], s=42, color=GOLD,
               edgecolor="k", linewidths=0.4, zorder=4, label="accepted states")
ax_hmc.plot(hmc_path[0, 0], hmc_path[0, 1], "o", color="k", ms=7, zorder=5, label="start")
ax_hmc.set_title(f"HMC: long leapfrog arcs  (acceptance {accepts / n_iter:.0%})", fontsize=12)
ax_hmc.set_xlabel("$q_1$")
ax_hmc.set_ylabel("$q_2$")
ax_hmc.set_aspect("equal")
ax_hmc.set_xlim(-lim, lim)
ax_hmc.set_ylim(-lim, lim)
ax_hmc.grid(True, alpha=0.3)
ax_hmc.legend(loc="upper left", fontsize=9, framealpha=0.9)

# Right: random-walk Metropolis path of matched budget.
ax_rwm.contour(gx, gy, dens, levels=6, colors="0.6", linewidths=0.8)
ax_rwm.plot(rwm_path[:, 0], rwm_path[:, 1], color=RED, lw=0.8, alpha=0.85)
ax_rwm.plot(rwm_path[0, 0], rwm_path[0, 1], "o", color="k", ms=7, zorder=5, label="start")
ax_rwm.set_title(f"Random-walk Metropolis: {n_rwm} steps, same budget", fontsize=12)
ax_rwm.set_xlabel("$q_1$")
ax_rwm.set_ylabel("$q_2$")
ax_rwm.set_aspect("equal")
ax_rwm.set_xlim(-lim, lim)
ax_rwm.set_ylim(-lim, lim)
ax_rwm.grid(True, alpha=0.3)
ax_rwm.legend(loc="upper left", fontsize=9, framealpha=0.9)

fig.suptitle("Momentum lets HMC sweep a correlated target in coherent moves, "
             "while random-walk Metropolis only crawls", fontsize=13)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("hamiltonian-monte-carlo.png", dpi=300, bbox_inches="tight")
plt.close()
print(f"Saved hamiltonian-monte-carlo.png   HMC acceptance = {accepts / n_iter:.0%}   "
      f"RWM acceptance = {rwm_accepts / n_rwm:.0%}")
