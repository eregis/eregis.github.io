"""
Langevin Monte Carlo sampling a bimodal target.

The (unadjusted) Langevin algorithm discretizes the stochastic differential
equation

    dX = grad log p(X) dt + sqrt(2) dW,

whose stationary distribution is exactly the target p. Here p is a symmetric
mixture of two Gaussians. The drift term grad log p pulls the walker toward
regions of high probability; the Brownian noise lets it explore --- and
occasionally hop across the low-probability barrier between the modes.

Output: langevin-dynamics.png --- left: a few Langevin trajectories jittering
within and hopping between the two modes; right: a histogram of Langevin samples
overlaid on the true density, showing the sampler reproduces the target.
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

BLUE, RED, GOLD = "#2166ac", "#b2182b", "#f0a202"

# --- Target: a symmetric two-component Gaussian mixture ---
mus = np.array([-2.0, 2.0])
sig = 0.9
w = 0.5


def density(x):
    g = np.exp(-((x[..., None] - mus) ** 2) / (2 * sig ** 2)) / (sig * np.sqrt(2 * np.pi))
    return (w * g).sum(-1)


def score(x):
    """grad log p(x) for the mixture, evaluated elementwise (vectorized)."""
    g = np.exp(-((x[..., None] - mus) ** 2) / (2 * sig ** 2)) / (sig * np.sqrt(2 * np.pi))
    p = (w * g).sum(-1)
    grad_p = (w * g * (-(x[..., None] - mus) / sig ** 2)).sum(-1)
    return grad_p / p


eps = 0.05

# --- Left panel: a few long single-chain trajectories ---
n_traj_steps = 20000
starts = np.array([-3.0, 0.0, 3.0])
traj = np.empty((len(starts), n_traj_steps))
xt = starts.copy()
for k in range(n_traj_steps):
    xt = xt + eps * score(xt) + np.sqrt(2 * eps) * np.random.normal(size=xt.shape)
    traj[:, k] = xt

# --- Right panel: a large ensemble of chains for a clean histogram ---
n_chains, n_burn, n_keep = 4000, 3000, 3000
xe = np.random.uniform(-5.0, 5.0, size=n_chains)      # broad, symmetric initialization
for _ in range(n_burn):
    xe = xe + eps * score(xe) + np.sqrt(2 * eps) * np.random.normal(size=xe.shape)
kept = np.empty((n_keep, n_chains))
for k in range(n_keep):
    xe = xe + eps * score(xe) + np.sqrt(2 * eps) * np.random.normal(size=xe.shape)
    kept[k] = xe
samples = kept.ravel()

fig, (ax_traj, ax_hist) = plt.subplots(1, 2, figsize=(12, 5))

colors = [BLUE, RED, "#1b7837"]
for i, c in enumerate(colors):
    ax_traj.plot(traj[i], color=c, lw=0.6, alpha=0.8)
for m in mus:
    ax_traj.axhline(m, color="0.6", ls="--", lw=1.0)
ax_traj.set_title("Langevin trajectories hop between modes", fontsize=12)
ax_traj.set_xlabel("iteration")
ax_traj.set_ylabel("position $x$")
ax_traj.set_ylim(-5, 5)
ax_traj.grid(True, alpha=0.3)

xg = np.linspace(-5, 5, 500)
ax_hist.hist(samples, bins=120, density=True, color=BLUE, alpha=0.5,
             label="Langevin samples")
ax_hist.plot(xg, density(xg), color=GOLD, lw=2.2, label="target density $p(x)$")
ax_hist.set_title("Samples reproduce the target", fontsize=12)
ax_hist.set_xlabel("$x$")
ax_hist.set_ylabel("density")
ax_hist.grid(True, alpha=0.3)
ax_hist.legend(loc="upper right", fontsize=10)

fig.suptitle("Langevin Monte Carlo on a bimodal distribution", fontsize=13)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("langevin-dynamics.png", dpi=300, bbox_inches="tight")
plt.close()
print(f"Saved langevin-dynamics.png   {samples.size:,} samples   "
      f"mean={samples.mean():+.3f}  std={samples.std():.3f}")
