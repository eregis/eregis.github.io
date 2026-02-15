import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# True function: x^2 + x
x_true = np.linspace(-3, 3, 300)
y_true = x_true**2 + x_true

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

for ax, n_points in zip(axes, [15, 100, 1000]):
    # Generate noisy data (fresh seed per panel for variety, but deterministic)
    rng = np.random.RandomState(42)
    x_data = rng.uniform(-3, 3, n_points)
    y_data = x_data**2 + x_data + rng.normal(0, 1.0, n_points)

    coeffs = np.polyfit(x_data, y_data, 20)
    y_fit = np.polyval(coeffs, x_true)

    ax.scatter(x_data, y_data, color='gray', alpha=0.4, s=20,
               label='Data', zorder=2)
    ax.plot(x_true, y_true, 'k--', linewidth=2,
            label='True function ($x^2 + x$)', zorder=3)
    ax.plot(x_true, y_fit, 'b-', linewidth=2,
            label='Degree-20 fit', zorder=3)

    ax.set_xlabel('$x$', fontsize=13)
    ax.set_ylabel('$y$', fontsize=13)
    ax.set_title(f'$n = {n_points}$', fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-5, 15)

fig.suptitle('More data tames overfitting',
             fontsize=15, y=1.02)

plt.tight_layout()
plt.savefig('assets/why-non-convexity/polynomial-bias-variance.png',
            dpi=150, bbox_inches='tight')
plt.show()
