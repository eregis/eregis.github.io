import numpy as np
import matplotlib.pyplot as plt

# --- Grid of 1D points ---
n_grid = 200
X = np.linspace(-3, 3, n_grid)
XX, YY = np.meshgrid(X, X)


def rbf_kernel(x, xp, sigma=1.0):
    """Gaussian (RBF) kernel: K(x,x') = exp(-||x-x'||^2 / (2*sigma^2))"""
    return np.exp(-(x - xp)**2 / (2 * sigma**2))


def arccosine_kernel_deg1(x, xp):
    """Arc-cosine kernel of degree 1 (ReLU kernel).

    K(x,x') = (1/pi) * ||x|| * ||x'|| * (sin(alpha) + (pi - alpha) * cos(alpha))
    where alpha = arccos(x_hat . x_hat'), with x_hat = x/||x|| for scalars.

    For scalar inputs, ||x|| = |x| and x_hat = sign(x), so
    x_hat . x_hat' = sign(x) * sign(x').
    """
    norm_x = np.abs(x)
    norm_xp = np.abs(xp)

    # Compute cos(alpha) = x_hat . x_hat' for scalars
    # Handle zero carefully
    cos_alpha = np.zeros_like(x * xp, dtype=float)
    nonzero = (norm_x > 1e-12) & (norm_xp > 1e-12)
    cos_alpha[nonzero] = (x[nonzero] * xp[nonzero]) / (norm_x[nonzero] * norm_xp[nonzero])

    # Clip for numerical safety
    cos_alpha = np.clip(cos_alpha, -1.0, 1.0)
    alpha = np.arccos(cos_alpha)

    K = (1.0 / np.pi) * norm_x * norm_xp * (np.sin(alpha) + (np.pi - alpha) * np.cos(alpha))
    return K


# --- Compute kernel matrices ---
K_rbf = rbf_kernel(XX, YY, sigma=1.0)
K_arc = arccosine_kernel_deg1(XX, YY)

# --- Reference points for slices ---
ref_points = [-2.0, 0.0, 2.0]
colors = ['#1f77b4', '#d62728', '#2ca02c']

# --- Plot ---
fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# Top-left: RBF heatmap
im0 = axes[0, 0].imshow(K_rbf, cmap='viridis', origin='lower',
                          extent=[X[0], X[-1], X[0], X[-1]])
axes[0, 0].set_xlabel('$x$', fontsize=13)
axes[0, 0].set_ylabel("$x'$", fontsize=13)
axes[0, 0].set_title('RBF (Gaussian) kernel', fontsize=14)
fig.colorbar(im0, ax=axes[0, 0], fraction=0.046, pad=0.04)

# Top-right: Arc-cosine heatmap
im1 = axes[0, 1].imshow(K_arc, cmap='viridis', origin='lower',
                          extent=[X[0], X[-1], X[0], X[-1]])
axes[0, 1].set_xlabel('$x$', fontsize=13)
axes[0, 1].set_ylabel("$x'$", fontsize=13)
axes[0, 1].set_title('Arc-cosine kernel (degree 1, ReLU)', fontsize=14)
fig.colorbar(im1, ax=axes[0, 1], fraction=0.046, pad=0.04)

# Bottom-left: RBF slices
for x_ref, color in zip(ref_points, colors):
    slice_vals = rbf_kernel(np.full_like(X, x_ref), X, sigma=1.0)
    axes[1, 0].plot(X, slice_vals, color=color, linewidth=2,
                     label=f'$x_{{\\mathrm{{ref}}}} = {x_ref:.0f}$')
axes[1, 0].set_xlabel('$x$', fontsize=13)
axes[1, 0].set_ylabel("$K(x_{\\mathrm{ref}}, x)$", fontsize=13)
axes[1, 0].set_title('RBF kernel slices', fontsize=14)
axes[1, 0].legend(fontsize=11)
axes[1, 0].grid(True, alpha=0.3)

# Bottom-right: Arc-cosine slices
for x_ref, color in zip(ref_points, colors):
    x_ref_arr = np.full_like(X, x_ref)
    slice_vals = arccosine_kernel_deg1(x_ref_arr, X)
    axes[1, 1].plot(X, slice_vals, color=color, linewidth=2,
                     label=f'$x_{{\\mathrm{{ref}}}} = {x_ref:.0f}$')
axes[1, 1].set_xlabel('$x$', fontsize=13)
axes[1, 1].set_ylabel("$K(x_{\\mathrm{ref}}, x)$", fontsize=13)
axes[1, 1].set_title('Arc-cosine kernel slices', fontsize=14)
axes[1, 1].legend(fontsize=11)
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('assets/neural-tangent-kernel/kernel-examples.png',
            dpi=150, bbox_inches='tight')
plt.show()
