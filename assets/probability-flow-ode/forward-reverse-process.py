"""
Forward (noising) and reverse (denoising) processes of a diffusion model.

The forward Ornstein-Uhlenbeck process  dX_t = -X_t dt + sqrt(2) dW_t  carries a
multimodal data distribution rho_0 to the standard Gaussian gamma = N(0, 1). For a
Gaussian-mixture rho_0 every marginal rho_t is available in closed form: the OU
transition kernel is  X_t | X_0 ~ N(X_0 e^{-t}, 1 - e^{-2t}),  so each mixture
component N(mu, s^2) maps to N(mu e^{-t}, s^2 e^{-2t} + (1 - e^{-2t})) --- the means
contract toward 0 and the variances relax toward 1.

The figure shows rho_t at several times morphing from the trimodal data distribution
(left, blue) into the standard Gaussian (right, red). The forward process runs
left-to-right (add noise); the reverse SDE / probability flow ODE run right-to-left
(denoise).

Output: forward-reverse-process.png
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import FancyArrowPatch

# --- multimodal data distribution rho_0: a mixture of three Gaussians ---
weights = np.array([0.36, 0.28, 0.36])
means = np.array([-2.2, 0.2, 2.3])
stds = np.array([0.45, 0.35, 0.42])


def gaussian(x, mu, sigma):
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))


def ou_marginal(x, t):
    """Density of the OU marginal rho_t for the Gaussian-mixture rho_0 above."""
    decay = np.exp(-t)
    var = stds ** 2 * decay ** 2 + (1.0 - decay ** 2)
    dens = np.zeros_like(x)
    for w, mu, v in zip(weights, means * decay, var):
        dens += w * gaussian(x, mu, np.sqrt(v))
    return dens


x = np.linspace(-4.5, 4.5, 600)
times = [0.0, 0.25, 0.6, 1.2, 3.0]

# blue (data) -> red (standard Gaussian) gradient across the panels
c0 = np.array(mcolors.to_rgb("#2166ac"))
c1 = np.array(mcolors.to_rgb("#b2182b"))
colors = [(1 - a) * c0 + a * c1 for a in np.linspace(0, 1, len(times))]

fig, axes = plt.subplots(1, len(times), figsize=(13, 3.8), sharex=True, sharey=True)
fig.subplots_adjust(left=0.03, right=0.97, top=0.73, bottom=0.22, wspace=0.12)

for ax, t, color in zip(axes, times, colors):
    dens = ou_marginal(x, t)
    ax.fill_between(x, dens, color=color, alpha=0.85, linewidth=0)
    ax.plot(x, dens, color=color, lw=1.6)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#999999")

axes[0].set_ylim(0, 0.55)

# panel labels: the two endpoints are the "two distributions"; intermediates show the morph
axes[0].set_title(r"$\rho_0$  (data)", fontsize=13, color=colors[0], pad=8)
axes[-1].set_title(r"$\gamma$  (standard Gaussian)", fontsize=13, color=colors[-1], pad=8)
for ax, t, color in zip(axes[1:-1], times[1:-1], colors[1:-1]):
    ax.set_title(rf"$\rho_t,\ t={t}$", fontsize=10, color=color, pad=8)

# forward / reverse arrows spanning the panels (figure coordinates)
fig.add_artist(FancyArrowPatch((0.06, 0.93), (0.94, 0.93), transform=fig.transFigure,
                               arrowstyle="-|>", mutation_scale=22, lw=2.2, color="#444444"))
fig.add_artist(FancyArrowPatch((0.94, 0.07), (0.06, 0.07), transform=fig.transFigure,
                               arrowstyle="-|>", mutation_scale=22, lw=2.2, color="#444444"))
fig.text(0.5, 0.965, "forward process: add noise  (OU process)",
         ha="center", va="center", fontsize=12, color="#444444")
fig.text(0.5, 0.035, "reverse process: denoise  (reverse SDE  /  probability flow ODE)",
         ha="center", va="center", fontsize=12, color="#444444")

out_dir = "C:/Users/ericf/critical-points/assets/probability-flow-ode"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "forward-reverse-process.png")
plt.savefig(out_path, dpi=300, facecolor="white")
plt.close()
print("Figure saved to", out_path)
