"""
Ridge-regularized polynomial regression: lambda as the free knob.

Same target function and data-generating setup as the polynomial figures in
"Non-Convexity as Feature Learning" (assets/why-non-convexity/polynomial-*.py):
g(x) = x^2 + x on x in [-3, 3], n = 15 noisy training points. Here the basis
is pushed into the overparameterized regime -- a degree-10 polynomial (11
coefficients) fit to 15 points -- and instead of comparing degrees, we fix
the degree and sweep the ridge penalty lambda:

    L_ridge(theta) = sum_i (y_i - f(x_i; theta))^2 + lambda * ||theta||^2

lambda = 0 recovers ordinary least squares (high variance, low bias:
interpolates the noise). lambda too large shrinks every coefficient toward
zero, so the fit degenerates to the training mean (high bias, low variance).
Left: three regimes of the same fit, at three values of lambda. Right:
training and test MSE against lambda (log-log), with the test-error minimum
-- the "sweet spot" -- marked.

Output: assets/high-bias-low-variance/polynomial-regularization-sweep.png
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# --- Target function and data, matching assets/why-non-convexity/polynomial-*.py ---
X_LO, X_HI = -3.0, 3.0
NOISE_STD = 1.0
N_TRAIN = 15
DEGREE = 10  # 11 coefficients (incl. intercept) fit to 15 points: overparameterized


def target(x):
    return x**2 + x


x_true = np.linspace(X_LO, X_HI, 300)
y_true = target(x_true)

x_train = np.random.uniform(X_LO, X_HI, N_TRAIN)
y_train = target(x_train) + np.random.normal(0, NOISE_STD, N_TRAIN)

# A large held-out set gives a clean estimate of the test-error curve.
x_test = np.random.uniform(X_LO, X_HI, 3000)
y_test = target(x_test) + np.random.normal(0, NOISE_STD, 3000)


def poly_features(x, degree):
    """[x, x^2, ..., x^degree], with x rescaled to [-1, 1] for conditioning.
    The constant column is handled separately below as an intercept, which
    ridge leaves unpenalized (standard practice, e.g. sklearn's Ridge)."""
    x_scaled = np.asarray(x).reshape(-1, 1) / X_HI
    powers = np.arange(1, degree + 1)
    return x_scaled ** powers


def ridge_fit(Phi, y, lam):
    """Ridge regression with an unpenalized intercept, via SVD (numerically
    stabler at high degree than solving the normal equations directly)."""
    x_mean = Phi.mean(axis=0)
    y_mean = y.mean()
    U, S, Vt = np.linalg.svd(Phi - x_mean, full_matrices=False)
    shrink = S / (S**2 + lam)
    coef = Vt.T @ (shrink * (U.T @ (y - y_mean)))
    intercept = y_mean - x_mean @ coef
    return intercept, coef


def predict(x, degree, intercept, coef):
    return intercept + poly_features(x, degree) @ coef


def mse(y_pred, y):
    return np.mean((y_pred - y) ** 2)


Phi_train = poly_features(x_train, DEGREE)
Phi_test = poly_features(x_test, DEGREE)

# --- Sweep lambda and track training / test error ---
lambdas = np.logspace(-6, 6, 300)
train_err = np.empty_like(lambdas)
test_err = np.empty_like(lambdas)
for i, lam in enumerate(lambdas):
    b0, coef = ridge_fit(Phi_train, y_train, lam)
    train_err[i] = mse(b0 + Phi_train @ coef, y_train)
    test_err[i] = mse(b0 + Phi_test @ coef, y_test)

best_idx = np.argmin(test_err)
lambda_sweet = lambdas[best_idx]

# --- Three regimes for the left panel ---
lambda_huge = 1000.0
regimes = [
    (0.0, '#d62728', '-', 2.2, r'$\lambda = 0$ (overfit)'),
    (lambda_sweet, '#2ca02c', '-', 2.6, rf'$\lambda \approx {lambda_sweet:.2g}$ (sweet spot)'),
    (lambda_huge, '#9467bd', '-', 2.2, rf'$\lambda = {lambda_huge:.0f}$ (over-smoothed)'),
]

fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

# --- Left: data, true function, and three regularized fits ---
ax = axes[0]
ax.scatter(x_train, y_train, color='gray', alpha=0.6, s=45, zorder=4, label='Data')
ax.plot(x_true, y_true, 'k--', linewidth=2, zorder=3,
        label='True function ($x^2 + x$)')

for lam, color, ls, lw, label in regimes:
    b0, coef = ridge_fit(Phi_train, y_train, lam)
    y_fit = predict(x_true, DEGREE, b0, coef)
    ax.plot(x_true, y_fit, color=color, linestyle=ls, linewidth=lw,
             label=label, zorder=5)

ax.set_xlabel('$x$', fontsize=13)
ax.set_ylabel('$y$', fontsize=13)
ax.set_title(f'Degree-{DEGREE} fit, $n = {N_TRAIN}$ points', fontsize=14)
ax.legend(fontsize=9.5, loc='upper center', ncol=1, framealpha=0.9)
ax.grid(True, alpha=0.3)
ax.set_xlim(X_LO, X_HI)
ax.set_ylim(-7, 15)

# --- Right: training / test error vs. lambda, sweet spot marked ---
ax2 = axes[1]
ax2.plot(lambdas, train_err, color='#1f77b4', linewidth=2.2, label='Training error')
ax2.plot(lambdas, test_err, color='#d62728', linewidth=2.2, label='Test error')
ax2.axvline(lambda_sweet, color='#2ca02c', linestyle='--', linewidth=1.5, zorder=2)
ax2.scatter([lambda_sweet], [test_err[best_idx]], color='#2ca02c', marker='*',
            s=260, zorder=6, edgecolor='white', linewidth=0.8, label='Sweet spot')

ax2.annotate(rf'$\lambda \approx {lambda_sweet:.2g}$',
             xy=(lambda_sweet, test_err[best_idx]),
             xytext=(lambda_sweet * 0.05, test_err[best_idx] * 3.2),
             fontsize=10.5, color='#2ca02c', ha='center',
             arrowprops=dict(arrowstyle='->', color='#2ca02c', lw=1.2))

ax2.text(0.03, 0.93, 'high variance,\nlow bias', transform=ax2.transAxes,
          fontsize=9.5, color='#d62728', ha='left', va='top', style='italic')
ax2.text(0.97, 0.40, 'high bias,\nlow variance', transform=ax2.transAxes,
          fontsize=9.5, color='#9467bd', ha='right', va='top', style='italic')

ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlabel(r'Regularization strength $\lambda$', fontsize=13)
ax2.set_ylabel('Mean squared error', fontsize=13)
ax2.set_title('Bias-variance tradeoff vs. $\\lambda$', fontsize=14)
ax2.legend(fontsize=10, loc='lower right', framealpha=0.9)
ax2.grid(True, alpha=0.3)

fig.suptitle(r'Regularization strength $\lambda$ trades variance for bias',
             fontsize=15, y=1.02)

plt.tight_layout()
plt.savefig('assets/high-bias-low-variance/polynomial-regularization-sweep.png',
            dpi=150, bbox_inches='tight')

print(f"lambda_sweet = {lambda_sweet:.4g}")
print(f"test error: lambda->0 = {test_err[0]:.3g}, sweet spot = {test_err[best_idx]:.3g}, "
      f"lambda huge = {test_err[-1]:.3g}")
