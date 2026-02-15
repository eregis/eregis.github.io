import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# --- Network parameters ---
d_in, d_hidden, d_out = 1, 50, 1

# Initialize weights with standard normal / sqrt(fan_in)
W1 = np.random.randn(d_hidden, d_in) / np.sqrt(d_in)
b1 = np.random.randn(d_hidden) / np.sqrt(d_in)
W2 = np.random.randn(d_out, d_hidden) / np.sqrt(d_hidden)
b2 = np.random.randn(d_out) / np.sqrt(d_hidden)

# --- Input points ---
n_points = 20
X = np.linspace(-3, 3, n_points)


def forward(x):
    """Forward pass for a single scalar input. Returns output and intermediates."""
    x_vec = np.array([x])                     # (1,)
    pre_act = W1 @ x_vec + b1                 # (d_hidden,)
    h = np.tanh(pre_act)                       # (d_hidden,)
    y = W2 @ h + b2                            # (d_out,)
    return y[0], h, pre_act, x_vec


def jacobian(x):
    """Compute df/dtheta for a single scalar input, returned as a flat vector."""
    _, h, pre_act, x_vec = forward(x)
    tanh_deriv = 1.0 - np.tanh(pre_act)**2    # (d_hidden,)

    # df/dW2 = h^T, shape (d_hidden,) -> flatten to (d_hidden,)
    df_dW2 = h.copy()

    # df/db2 = 1, shape (1,)
    df_db2 = np.array([1.0])

    # Backprop through hidden layer
    # df/dh = W2^T, shape (d_hidden,)
    df_dh = W2[0, :]                          # (d_hidden,)
    delta = df_dh * tanh_deriv                 # (d_hidden,)

    # df/dW1 = delta outer x, shape (d_hidden, d_in) -> flatten
    df_dW1 = np.outer(delta, x_vec).flatten()

    # df/db1 = delta, shape (d_hidden,)
    df_db1 = delta.copy()

    # Concatenate all gradients: W1, b1, W2, b2
    return np.concatenate([df_dW1, df_db1, df_dW2, df_db2])


# --- Compute Jacobian matrix and NTK ---
J = np.array([jacobian(x) for x in X])        # (n_points, n_params)
NTK = J @ J.T                                  # (n_points, n_points)

# --- Plot ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Left panel: heatmap
im = axes[0].imshow(NTK, cmap='viridis', origin='lower',
                     extent=[X[0], X[-1], X[0], X[-1]])
axes[0].set_xlabel('$x$', fontsize=13)
axes[0].set_ylabel("$x'$", fontsize=13)
axes[0].set_title('Neural Tangent Kernel $\\Theta(x, x\')$', fontsize=14)
fig.colorbar(im, ax=axes[0], fraction=0.046, pad=0.04)

# Right panel: kernel slices for reference inputs
ref_values = [-2.0, 0.0, 2.0]
colors = ['#1f77b4', '#d62728', '#2ca02c']
X_dense = np.linspace(-3, 3, 200)

for x_ref, color in zip(ref_values, colors):
    # Compute Jacobian for reference point
    j_ref = jacobian(x_ref)                    # (n_params,)
    # Compute kernel slice on dense grid
    kernel_slice = np.array([j_ref @ jacobian(xd) for xd in X_dense])
    axes[1].plot(X_dense, kernel_slice, color=color, linewidth=2,
                 label=f'$x_{{\\mathrm{{ref}}}} = {x_ref:.0f}$')

axes[1].set_xlabel('$x$', fontsize=13)
axes[1].set_ylabel('$\\Theta(x_{\\mathrm{ref}}, x)$', fontsize=13)
axes[1].set_title('Kernel slices at reference inputs', fontsize=14)
axes[1].legend(fontsize=12)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('assets/neural-tangent-kernel/ntk-similarity.png',
            dpi=150, bbox_inches='tight')
plt.show()
