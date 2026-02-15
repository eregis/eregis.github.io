import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# --- Training data: fit sin(x) ---
n_points = 20
X_train = np.linspace(-np.pi, np.pi, n_points)
Y_train = np.sin(X_train)


def init_params(d_hidden):
    """Initialize network parameters with standard normal / sqrt(fan_in)."""
    W1 = np.random.randn(d_hidden, 1) / np.sqrt(1)
    b1 = np.random.randn(d_hidden) / np.sqrt(1)
    W2 = np.random.randn(1, d_hidden) / np.sqrt(d_hidden)
    b2 = np.random.randn(1) / np.sqrt(d_hidden)
    return W1, b1, W2, b2


def forward_batch(X, W1, b1, W2, b2):
    """Forward pass for a batch of scalar inputs.

    Args:
        X: (n,) array of inputs
    Returns:
        Y: (n,) predictions
        H: (n, d_hidden) hidden activations
        Pre: (n, d_hidden) pre-activations
    """
    Pre = W1 @ X.reshape(1, -1) + b1[:, None]  # (d_hidden, n)
    H = np.tanh(Pre)                             # (d_hidden, n)
    Y = (W2 @ H + b2[:, None]).squeeze(0)        # (n,)
    return Y, H.T, Pre.T                         # H, Pre transposed to (n, d_hidden)


def compute_jacobian(X, W1, b1, W2, b2):
    """Compute Jacobian matrix J[i, j] = df(x_i)/dtheta_j.

    Returns:
        J: (n_points, n_params) Jacobian matrix
    """
    n = len(X)
    d_hidden = W1.shape[0]
    _, H, Pre = forward_batch(X, W1, b1, W2, b2)

    tanh_deriv = 1.0 - np.tanh(Pre)**2          # (n, d_hidden)

    rows = []
    for i in range(n):
        h = H[i]                                  # (d_hidden,)
        td = tanh_deriv[i]                        # (d_hidden,)
        x_val = X[i]

        # df/dW2 = h, shape (d_hidden,)
        df_dW2 = h.copy()

        # df/db2 = 1
        df_db2 = np.array([1.0])

        # Backprop: delta = W2^T * tanh'(pre)
        delta = W2[0, :] * td                    # (d_hidden,)

        # df/dW1 = delta * x (outer product flattened), shape (d_hidden,)
        df_dW1 = delta * x_val                   # (d_hidden,) since input is scalar

        # df/db1 = delta
        df_db1 = delta.copy()

        rows.append(np.concatenate([df_dW1, df_db1, df_dW2, df_db2]))

    return np.array(rows)


def compute_ntk(X, W1, b1, W2, b2):
    """Compute NTK matrix Theta(x_i, x_j) = sum_k J_ik J_jk."""
    J = compute_jacobian(X, W1, b1, W2, b2)
    return J @ J.T


def compute_loss_grads(X, Y, W1, b1, W2, b2):
    """Compute MSE loss and parameter gradients manually.

    MSE = (1/n) sum_i (f(x_i) - y_i)^2
    """
    n = len(X)
    Y_pred, H, Pre = forward_batch(X, W1, b1, W2, b2)
    residuals = Y_pred - Y                        # (n,)
    loss = np.mean(residuals**2)

    tanh_deriv = 1.0 - np.tanh(Pre)**2           # (n, d_hidden)

    # dL/df = (2/n) * residuals, shape (n,)
    dL_df = (2.0 / n) * residuals

    # dL/dW2 = dL/df^T @ H, shape (1, d_hidden)
    dL_dW2 = dL_df.reshape(1, -1) @ H            # (1, d_hidden)

    # dL/db2 = sum of dL/df
    dL_db2 = np.sum(dL_df, keepdims=True)         # (1,)

    # Backprop to hidden layer
    # delta = dL/df[:, None] * W2 * tanh_deriv, shape (n, d_hidden)
    delta = dL_df[:, None] * W2 * tanh_deriv      # (n, d_hidden)

    # dL/dW1 = delta^T @ X_col, shape (d_hidden, 1)
    X_col = X.reshape(-1, 1)                      # (n, 1)
    dL_dW1 = delta.T @ X_col                      # (d_hidden, 1)

    # dL/db1 = sum over samples of delta, shape (d_hidden,)
    dL_db1 = np.sum(delta, axis=0)

    return loss, dL_dW1, dL_db1, dL_dW2, dL_db2


def train_and_track_ntk(d_hidden, lr, n_steps, record_every=5):
    """Train network and track relative NTK change over time."""
    W1, b1, W2, b2 = init_params(d_hidden)

    # Compute initial NTK
    NTK_0 = compute_ntk(X_train, W1, b1, W2, b2)
    ntk_norm_0 = np.linalg.norm(NTK_0, 'fro')

    steps_recorded = []
    relative_changes = []
    losses = []

    for step in range(n_steps):
        # Record NTK change periodically
        if step % record_every == 0:
            NTK_t = compute_ntk(X_train, W1, b1, W2, b2)
            rel_change = np.linalg.norm(NTK_t - NTK_0, 'fro') / ntk_norm_0
            steps_recorded.append(step)
            relative_changes.append(rel_change)

        # Compute gradients and update
        loss, dL_dW1, dL_db1, dL_dW2, dL_db2 = compute_loss_grads(
            X_train, Y_train, W1, b1, W2, b2)

        if step % record_every == 0:
            losses.append(loss)

        W1 -= lr * dL_dW1
        b1 -= lr * dL_db1
        W2 -= lr * dL_dW2
        b2 -= lr * dL_db2

    return np.array(steps_recorded), np.array(relative_changes), np.array(losses)


# --- Run experiments ---
print("Training wide network (width=1000)...")
steps_wide, ntk_change_wide, loss_wide = train_and_track_ntk(
    d_hidden=1000, lr=0.001, n_steps=1000, record_every=10)

print("Training narrow network (width=10)...")
steps_narrow, ntk_change_narrow, loss_narrow = train_and_track_ntk(
    d_hidden=10, lr=0.01, n_steps=1000, record_every=10)

# --- Plot ---
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(steps_wide, ntk_change_wide, color='#1f77b4', linewidth=2.5,
        label='Wide network (width = 1000)')
ax.plot(steps_narrow, ntk_change_narrow, color='#d62728', linewidth=2.5,
        label='Narrow network (width = 10)')

ax.set_xlabel('Training step', fontsize=13)
ax.set_ylabel('Relative NTK change  $\\|\\Theta_t - \\Theta_0\\|_F \\,/\\, \\|\\Theta_0\\|_F$',
              fontsize=13)
ax.set_title('Lazy regime vs. feature learning', fontsize=14)
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('assets/neural-tangent-kernel/lazy-vs-feature-learning.png',
            dpi=150, bbox_inches='tight')
plt.show()
