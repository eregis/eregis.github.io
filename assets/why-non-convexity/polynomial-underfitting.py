import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# True function: x^3
x_true = np.linspace(-2, 2, 300)
y_true = x_true**3

# Noisy data points
n_points = 50
x_data = np.random.uniform(-2, 2, n_points)
y_data = x_data**3 + np.random.normal(0, 1.5, n_points)

# Fit using {1, x, x^2} basis (degree 2 polynomial)
coeffs = np.polyfit(x_data, y_data, 2)
y_fit = np.polyval(coeffs, x_true)

fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter(x_data, y_data, color='gray', alpha=0.5, s=30, label='Data', zorder=2)
ax.plot(x_true, y_true, 'k--', linewidth=2, label='True function ($x^3$)', zorder=3)
ax.plot(x_true, y_fit, 'b-', linewidth=2, label='Best quadratic fit', zorder=3)

ax.set_xlabel('$x$', fontsize=14)
ax.set_ylabel('$y$', fontsize=14)
ax.set_title('Underfitting: fitting $x^3$ with $\\{1, x, x^2\\}$ basis', fontsize=14)
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)
ax.set_ylim(-10, 10)

plt.tight_layout()
plt.savefig('assets/why-non-convexity/polynomial-underfitting.png', dpi=150, bbox_inches='tight')
plt.show()
