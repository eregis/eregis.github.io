"""
The Metropolis proposal: a symmetric proposal is blind to the target.

To sample from a target pi, the Metropolis algorithm proposes a move from the
current state x0 by drawing from a simple proposal distribution q(x0, .) --- here
a narrow Gaussian centered at x0. The proposal is symmetric, so it is equally
likely to step left or right, even though the target is bimodal and asymmetric,
with most of its mass off to one side. The proposal has no knowledge of the
target's shape; it is the accept/reject step that corrects for this and steers
the chain toward the high-probability regions.

Output: metropolis-proposal.png --- an asymmetric bimodal target with the
current state marked and a thin symmetric Gaussian proposal centered on it.
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

BLUE, RED, GOLD = "#2166ac", "#b2182b", "#f0a202"

# --- Asymmetric bimodal target: a small left mode and a dominant right mode ---
mus = np.array([-2.0, 2.0])
sig = 0.8
w = np.array([0.35, 0.65])


def density(x):
    g = np.exp(-((x[..., None] - mus) ** 2) / (2 * sig ** 2)) / (sig * np.sqrt(2 * np.pi))
    return (w * g).sum(-1)


# --- Current state and its thin, symmetric Gaussian proposal ---
x0 = 0.5
sig_q = 0.4


def proposal(x):
    return np.exp(-((x - x0) ** 2) / (2 * sig_q ** 2)) / (sig_q * np.sqrt(2 * np.pi))


xg = np.linspace(-5, 5, 800)
dens = density(xg)
# Scale the proposal so it reads as a comparable "bump" rather than a tall spike
# (the two curves are different objects, so the height is only schematic).
prop = proposal(xg)
prop = prop / prop.max() * dens.max() * 0.95

fig, ax = plt.subplots(figsize=(9, 5.5))

ax.plot(xg, dens, color=BLUE, lw=2.2, label=r"target $\pi(x)$")
ax.fill_between(xg, dens, color=BLUE, alpha=0.18)

ax.plot(xg, prop, color=GOLD, lw=2.0, label=r"proposal $q(x_0,\cdot)$")
ax.fill_between(xg, prop, color=GOLD, alpha=0.22)

ax.axvline(x0, color="0.4", ls="--", lw=1.0)
ax.plot(x0, 0, marker="o", color="k", ms=9, zorder=5, clip_on=False,
        label=r"current state $x_0$")

# Symmetric left/right hint.
y_arr = dens.max() * 0.42
ax.annotate("", xy=(x0 - 1.05, y_arr), xytext=(x0, y_arr),
            arrowprops=dict(arrowstyle="->", color="0.35", lw=1.4))
ax.annotate("", xy=(x0 + 1.05, y_arr), xytext=(x0, y_arr),
            arrowprops=dict(arrowstyle="->", color="0.35", lw=1.4))
ax.text(x0, y_arr + dens.max() * 0.03, "equally likely left or right",
        ha="center", va="bottom", fontsize=9, color="0.3")

# Point out where the mass actually is.
ax.annotate("most of the target's mass\nlies to the right",
            xy=(2.0, density(np.array([2.0]))[0] * 0.6), xytext=(3.1, dens.max() * 0.8),
            ha="center", fontsize=9, color=BLUE,
            arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2, alpha=0.7))

ax.set_title("A symmetric proposal is blind to the target's shape", fontsize=13)
ax.set_xlabel("$x$")
ax.set_ylabel("density")
ax.set_xlim(-5, 5)
ax.set_ylim(0, dens.max() * 1.18)
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", fontsize=10)

plt.tight_layout()
plt.savefig("metropolis-proposal.png", dpi=300, bbox_inches="tight")
plt.close()
print("The plot has been saved as 'metropolis-proposal.png'")
