"""
The bias-variance U-curve is the first half of a double-descent curve.

One experiment, two views. The model is linear in its trained parameters:
minimum-norm least squares on p random ReLU features,

    phi_j(x) = max(0, w_j . x),  w_j ~ N(0, I_d / d),
    f_p(x)   = sum_{j <= p} theta_j phi_j(x),  theta = pinv(Phi_p) y.

For p < n this is ordinary least squares. For p > n it is the interpolating
solution of smallest ||theta|| (what gradient descent from theta = 0 converges
to). The model can represent far more functions than n points pin down, and
"smallest norm" is a soft preference among them, not a restriction on which
functions are allowed. That is Wilson's point in "Deep Learning is Not So
Mysterious or Different": the U-curve and double descent both appear in a plain
linear model, with no neural-network training involved.

Experiment
  - Inputs x ~ N(0, I_d), d = 20. Target f(x) = x_1 + 0.3 tanh(2 x_2): mostly
    linear, mildly nonlinear. Labels y = f(x) + N(0, sigma^2), sigma = 0.35.
  - One pool of 2000 features is drawn once; model p uses the first p of them
    (nested), so capacity grows monotonically with p.
  - K = 500 independent training sets of n = 100 points (new inputs and new label
    noise each time). Every p is fit on the same K sets and scored on the same
    fixed test inputs.
  - bias^2(p) = E_x[(mean_k f_k(x) - f(x))^2] and Var(p) = E_x[Var_k f_k(x)], from
    the K predictions at each test input. Both use unbiased estimators (ddof = 1
    for Var; Var/K subtracted from bias^2, since a mean of K predictions is itself
    noisy). Test error = bias^2 + Var + sigma^2.
  - Check: the test MSE measured directly against freshly noised labels (new noise
    for every draw) must match bias^2 + Var + sigma^2. The gap printed below is
    the Monte Carlo noise of those labels.
  - p = n - 1, n, n + 1 are skipped. The ridgeless error there is dominated by a
    few near-singular training sets (at p = n the mean is ~100x the median, and 3
    of 1000 draws supply half of it). n +/- 2 is the closest usable pair. The spike
    height there is still a heavy-tailed average (it can move by tens of percent
    between runs); its location and its size relative to the plateau are robust.
    No ridge is used.
  - For p > n the fit is computed in the dual form theta = Phi^T (Phi Phi^T)^{-1} y,
    identical to the pseudo-inverse solution (checked on the first draw below).

What was tuned ("ratio" = test error at p = 20 n divided by the best p < n; the
figure needs ratio < 1; exploratory runs used K = 120-200)
  - 1-D inputs do not work. With x ~ U(-1, 1), features ReLU(+-x + b), b ~ U(-1, 1),
    n = 50, p up to 1500, three smooth targets and sigma in {0.05, 0.1, 0.3}, the
    error at p = 1500 was 60x to 5000x the best p < n. Even the median training set
    (target sin(pi x), sigma = 0.1) had excess error 0.26 against 0.005 for least
    squares on 8 features: interpolating random 1-D inputs amplifies the noise.
    Hence d = 20.
  - n/d matters. At n = 100, d = 16, 20, 24, 30 give ratios 0.55, 0.44, 0.40, 0.43;
    d = 12 (n/d = 8) gives 0.99, i.e. no gain. d = 20 (n/d = 5) is a round middle.
  - sigma = 0.35. At sigma = 0.5 the ratio is 0.61.
  - The target has to suit the soft bias (n = 100, d = 20):
        x_1                            0.42     tanh(2 x_1)        0.76
        x_1 + 0.3 tanh(2 x_2)  (used)  0.44     sin(1.5 x_1)       1.17
        x_1 + 0.6 tanh(2 x_2)          0.45     x_1 x_2            0.96
        x_1 + 0.5 (x_2^2 - 1)/sqrt(2)  0.47
    Minimum-norm solutions favor low-degree structure; when the target's energy
    sits in higher-degree terms the interpolating regime does not win.
  - Random biases on the features (std 0.5) move the ratio by ~0.03: not used.
  - The pool seed was not searched: seed 42. Eight other pools (seeds 1-8) give
    ratios 0.35 to 0.51.
  - The small steps in the left-panel curves are real. One nested pool means a
    feature that happens to align with the target direction x_1 lowers bias^2 and
    variance at once. Every (d, sigma) tried has them (11-22 local minima over
    p < n). Averaging over several pools would smooth them; the pool is drawn
    once on purpose.

Left: p < n only. Bias^2 falls, variance rises, test error is U-shaped; its
minimum is the classical "sweet spot". Right: the full sweep on log-log axes. The
training error reaches zero at p = n, the test error peaks there, and then falls
below the sweet spot as p keeps growing.

Run from the repository root (about 2 minutes).
Output: assets/links-october-2026/bias-variance-double-descent.png
"""
import numpy as np
import matplotlib.pyplot as plt

SEED = 42
rng = np.random.default_rng(SEED)

# --- Experiment settings ---
N_TRAIN = 100   # training points n
D = 20          # input dimension
SIGMA = 0.35    # label-noise standard deviation
K = 500         # independent training sets
N_TEST = 2000   # fixed test inputs
P_MAX = 2000    # size of the nested feature pool (20 n)

# p < n: every integer up to n - 2. p > n: dense just above the threshold, then
# geometric. p = n - 1, n, n + 1 are skipped (see docstring).
P_GRID = np.unique(np.concatenate([
    np.arange(1, N_TRAIN - 1),
    N_TRAIN + np.array([2, 3, 4, 5, 6, 8]),
    np.round(np.geomspace(N_TRAIN + 10, P_MAX, 28)).astype(int),
]))


def target(X):
    return X[:, 0] + 0.3 * np.tanh(2.0 * X[:, 1])


def relu_features(X, W):
    return np.maximum(X @ W.T, 0.0)


def min_norm_fits(Phi, y, Phi_te, p_grid):
    """Test predictions and training MSE of the minimum-norm least-squares fit on
    the first p features, for each p in p_grid (ascending)."""
    n = Phi.shape[0]
    preds = np.empty((len(p_grid), Phi_te.shape[0]))
    train = np.empty(len(p_grid))
    G = np.zeros((n, n))                  # Gram matrix Phi_p Phi_p^T, grown with p
    C = np.zeros((Phi_te.shape[0], n))    # cross-kernel Phi_test,p Phi_p^T
    done = 0
    for i, p in enumerate(p_grid):
        if p < n:                         # fewer features than points: ordinary least squares
            theta = np.linalg.lstsq(Phi[:, :p], y, rcond=None)[0]
            preds[i] = Phi_te[:, :p] @ theta
            train[i] = np.mean((Phi[:, :p] @ theta - y) ** 2)
        else:                             # more features than points: theta = Phi^T (Phi Phi^T)^{-1} y
            B = Phi[:, done:p]
            G += B @ B.T
            C += Phi_te[:, done:p] @ B.T
            done = p
            alpha = np.linalg.solve(G, y)
            preds[i] = C @ alpha          # = Phi_test,p theta
            train[i] = np.mean((G @ alpha - y) ** 2)   # = mean((Phi_p theta - y)^2)
    return preds, train


# --- Feature pool (drawn once) and fixed test inputs ---
W = rng.standard_normal((P_MAX, D)) / np.sqrt(D)
x_test = rng.standard_normal((N_TEST, D))
f_test = target(x_test)
Phi_test = relu_features(x_test, W)

# --- Simulate K training sets ---
S1 = np.zeros((len(P_GRID), N_TEST))   # sum over draws of f_k(x)
S2 = np.zeros_like(S1)                 # sum over draws of f_k(x)^2
mse_direct = np.zeros(len(P_GRID))     # directly measured test MSE (noisy labels)
mse_train = np.zeros(len(P_GRID))

print(f"Simulating {K} training sets (n = {N_TRAIN}, d = {D}, sigma = {SIGMA}, "
      f"{len(P_GRID)} values of p up to {P_MAX}) ...")
for k in range(K):
    X = rng.standard_normal((N_TRAIN, D))
    y = target(X) + SIGMA * rng.standard_normal(N_TRAIN)
    y_test = f_test + SIGMA * rng.standard_normal(N_TEST)   # fresh noisy labels for this draw
    Phi = relu_features(X, W)
    preds, train = min_norm_fits(Phi, y, Phi_test, P_GRID)
    if k == 0:   # dual form vs. pseudo-inverse, at the smallest, a middle, and the largest p > n
        dual_dev = 0.0
        for i in np.flatnonzero(P_GRID > N_TRAIN)[[0, 12, -1]]:
            ref = Phi_test[:, :P_GRID[i]] @ (np.linalg.pinv(Phi[:, :P_GRID[i]]) @ y)
            dual_dev = max(dual_dev, np.max(np.abs(preds[i] - ref)))
    S1 += preds
    S2 += preds ** 2
    mse_direct += np.mean((preds - y_test) ** 2, axis=1)
    mse_train += train

# --- Bias-variance decomposition from the K draws ---
mean_pred = S1 / K
var_x = (S2 / K - mean_pred ** 2) * K / (K - 1)                  # unbiased Var_k f_k(x), per test input
variance = var_x.mean(axis=1)
bias2 = ((mean_pred - f_test) ** 2).mean(axis=1) - variance / K  # drop the Var/K noise in mean_pred
test_err = bias2 + variance + SIGMA ** 2
test_direct = mse_direct / K
train_err = mse_train / K

classical = P_GRID < N_TRAIN
i_sweet = int(np.argmin(np.where(classical, test_err, np.inf)))
i_peak = int(np.argmax(test_err))
p_sweet, err_sweet = int(P_GRID[i_sweet]), test_err[i_sweet]

# --- Figure ---
C_BIAS, C_VAR, C_TEST, C_TRAIN, C_STAR = '#9467bd', '#ff7f0e', '#d62728', '#1f77b4', '#2ca02c'

fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

# Left: the classical regime (p < n) -- bias^2 falls, variance rises, test error is U-shaped
ax = axes[0]
ax.plot(P_GRID[classical], bias2[classical], color=C_BIAS, linewidth=2.2, label=r'Bias$^2$')
ax.plot(P_GRID[classical], variance[classical], color=C_VAR, linewidth=2.2, label='Variance')
ax.plot(P_GRID[classical], test_err[classical], color=C_TEST, linewidth=2.6,
        label=r'Test error ($\mathrm{bias}^2 + \mathrm{var} + \sigma^2$)')
ax.scatter([p_sweet], [err_sweet], color=C_STAR, marker='*', s=260, zorder=6,
           edgecolor='white', linewidth=0.8, label=rf'Sweet spot ($p = {p_sweet}$)')
ax.set_xlabel('Number of features $p$', fontsize=13)
ax.set_ylabel('Mean squared error', fontsize=13)
ax.set_title('The classical picture', fontsize=14)
ax.set_xlim(0, N_TRAIN)
ax.set_ylim(0, 1.8)
ax.legend(fontsize=10, loc='upper left', framealpha=0.9)
ax.grid(True, alpha=0.3)

# Right: the full sweep, log-log -- the second descent goes below the sweet spot
ax2 = axes[1]
ax2.plot(P_GRID, test_err, color=C_TEST, linewidth=2.2, label='Test error')
# Training error is zero to machine precision (< 1e-22) for p > n; clip it below the axis
# so the curve drops out of view at the threshold.
ax2.plot(P_GRID, np.maximum(train_err, 1e-9), color=C_TRAIN, linewidth=2.2, label='Training error')
ax2.axvline(N_TRAIN, color='0.35', linestyle='--', linewidth=1.5, zorder=2)
ax2.axhline(err_sweet, color=C_STAR, linestyle=':', linewidth=1.5, zorder=2)
ax2.scatter([p_sweet], [err_sweet], color=C_STAR, marker='*', s=260, zorder=6,
            edgecolor='white', linewidth=0.8, label='Classical sweet spot')

ax2.text(N_TRAIN * 1.07, 1.3e-3, 'interpolation threshold\n$p = n$', rotation=90,
         va='bottom', ha='left', fontsize=10, color='0.25')
ax2.text(0.03, 0.96, 'classical regime\n($p < n$)', transform=ax2.transAxes,
         fontsize=9.5, color='0.35', ha='left', va='top', style='italic')
ax2.text(0.97, 0.96, 'overparameterized regime\n($p > n$, zero training error)',
         transform=ax2.transAxes, fontsize=9.5, color='0.35', ha='right', va='top',
         style='italic')

ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlim(0.85, P_MAX * 1.15)
ax2.set_ylim(1e-3, 60)
ax2.set_xlabel('Number of features $p$', fontsize=13)
ax2.set_ylabel('Mean squared error', fontsize=13)
ax2.set_title('Double descent', fontsize=14)
ax2.legend(fontsize=10, loc='lower left', framealpha=0.9)
ax2.grid(True, alpha=0.3)

fig.suptitle(rf'Minimum-norm least squares on random ReLU features ($n = {N_TRAIN}$ training points)',
             fontsize=15, y=1.02)

plt.tight_layout()
plt.savefig('assets/links-october-2026/bias-variance-double-descent.png',
            dpi=150, bbox_inches='tight')

# --- Summary / checks ---
gap = np.max(np.abs(test_err - test_direct) / test_direct)
interp = P_GRID > N_TRAIN
print(f"dual form vs pinv (first draw, three values of p > n): max |diff| = {dual_dev:.1e}")
print(f"max relative gap, (bias^2 + variance + sigma^2) vs directly measured test MSE: {gap:.2e}")
print(f"classical sweet spot: p = {p_sweet}, test error = {err_sweet:.4f}")
print(f"peak: p = {int(P_GRID[i_peak])} (n = {N_TRAIN}), test error = {test_err[i_peak]:.3g}")
print(f"largest p = {int(P_GRID[-1])}: test error = {test_err[-1]:.4f} "
      f"({test_err[-1] / err_sweet:.2f}x the sweet spot; noise floor sigma^2 = {SIGMA ** 2:.4f})")
print(f"below the classical sweet spot: {bool(test_err[-1] < err_sweet)}")
print(f"max training MSE for p > n: {train_err[interp].max():.1e} (interpolation)")
