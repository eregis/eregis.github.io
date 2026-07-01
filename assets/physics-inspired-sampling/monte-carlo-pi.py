"""
Estimating pi by Monte Carlo.

Draw points uniformly from the square [-1, 1] x [-1, 1] and ask what fraction
land inside the inscribed unit circle. The circle has area pi and the square
has area 4, so the fraction inside is pi/4; multiplying the running fraction by
4 gives a Monte Carlo estimate of pi that converges as the sample count grows
(the law of large numbers).

Output: monte-carlo-pi.png --- left: a readable subset of the sampled points,
colored by whether they fall inside the circle; right: the running estimate of
pi converging to the true value as the number of samples increases.
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

BLUE, RED, GOLD = "#2166ac", "#b2182b", "#f0a202"

# --- Draw a large pool of uniform samples in the square [-1, 1]^2 ---
N = 200_000
pts = np.random.uniform(-1.0, 1.0, size=(N, 2))
inside = (pts[:, 0] ** 2 + pts[:, 1] ** 2) <= 1.0

# Running estimate of pi: 4 * (fraction of the first n points inside the circle).
n = np.arange(1, N + 1)
running_pi = 4.0 * np.cumsum(inside) / n

fig, (ax_scatter, ax_conv) = plt.subplots(1, 2, figsize=(12, 5))

# --- Left panel: scatter of a readable subset of the points ---
n_show = 3000
sx, sy = pts[:n_show, 0], pts[:n_show, 1]
sin = inside[:n_show]
ax_scatter.scatter(sx[sin], sy[sin], s=7, color=BLUE, alpha=0.6, label="inside circle")
ax_scatter.scatter(sx[~sin], sy[~sin], s=7, color=RED, alpha=0.6, label="outside circle")
theta = np.linspace(0, 2 * np.pi, 400)
ax_scatter.plot(np.cos(theta), np.sin(theta), color="k", lw=1.5)
ax_scatter.add_patch(plt.Rectangle((-1, -1), 2, 2, fill=False, edgecolor="k", lw=1.0))
ax_scatter.set_aspect("equal")
ax_scatter.set_xlim(-1.08, 1.08)
ax_scatter.set_ylim(-1.08, 1.08)
ax_scatter.set_title(f"{n_show:,} uniform samples in the square", fontsize=12)
ax_scatter.set_xlabel("$x$")
ax_scatter.set_ylabel("$y$")
ax_scatter.grid(True, alpha=0.3)
ax_scatter.legend(loc="upper right", fontsize=9, framealpha=0.9)

# --- Right panel: running estimate vs sample count (log x-axis) ---
# The indicator is Bernoulli(pi/4), so the estimator's standard error shrinks
# like 1/sqrt(N): SE = sqrt(pi (4 - pi) / N). Shading it shows why Monte Carlo
# convergence is slow -- the error funnels in only as the square root of effort.
se = np.sqrt(np.pi * (4 - np.pi) / n)
ax_conv.fill_between(n, np.pi - se, np.pi + se, color=BLUE, alpha=0.15,
                     label=r"$\pi \pm \mathrm{SE}$  (shrinks like $1/\sqrt{N}$)")
ax_conv.axhline(np.pi, color=GOLD, ls="--", lw=1.6, label=r"true $\pi$")
ax_conv.plot(n, running_pi, color=BLUE, lw=1.0)
ax_conv.set_xscale("log")
ax_conv.set_xlim(1, N)
ax_conv.set_ylim(2.6, 3.7)
ax_conv.set_title("Running estimate converges to $\\pi$", fontsize=12)
ax_conv.set_xlabel("number of samples")
ax_conv.set_ylabel(r"$\hat{\pi} = 4 \times (\mathrm{fraction\ inside})$")
ax_conv.grid(True, alpha=0.3)
ax_conv.legend(loc="upper right", fontsize=10)
ax_conv.text(0.97, 0.06,
             f"final estimate ($N = {N:,}$):  $\\hat{{\\pi}} = {running_pi[-1]:.4f}$",
             transform=ax_conv.transAxes, ha="right", fontsize=9,
             bbox=dict(boxstyle="round", fc="white", ec="0.7", alpha=0.9))

fig.suptitle("Estimating $\\pi$ by Monte Carlo", fontsize=13)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("monte-carlo-pi.png", dpi=300, bbox_inches="tight")
plt.close()
print(f"Saved monte-carlo-pi.png   final estimate: {running_pi[-1]:.5f}  (true pi = {np.pi:.5f})")
