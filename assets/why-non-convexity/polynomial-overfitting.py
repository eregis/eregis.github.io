import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# True function: x^2 + x
x_true = np.linspace(-3, 3, 300)
y_true = x_true**2 + x_true

# Noisy data
n_points = 15
x_data = np.random.uniform(-3, 3, n_points)
y_data = x_data**2 + x_data + np.random.normal(0, 1.0, n_points)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax, degree, title in zip(axes, [2, 20],
                              ['Degree 2 (correct)', 'Degree 20 (overfit)']):
    coeffs = np.polyfit(x_data, y_data, degree)
    y_fit = np.polyval(coeffs, x_true)

    ax.scatter(x_data, y_data, color='gray', alpha=0.6, s=40,
               label='Data', zorder=2)
    ax.plot(x_true, y_true, 'k--', linewidth=2,
            label='True function ($x^2 + x$)', zorder=3)
    ax.plot(x_true, y_fit, 'b-', linewidth=2,
            label=f'Degree-{degree} fit', zorder=3)

    ax.set_xlabel('$x$', fontsize=13)
    ax.set_ylabel('$y$', fontsize=13)
    ax.set_title(title, fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-5, 15)

fig.suptitle('Overfitting: too many basis functions fit the noise',
             fontsize=15, y=1.02)

plt.tight_layout()
plt.savefig('assets/why-non-convexity/polynomial-overfitting.png',
            dpi=150, bbox_inches='tight')
plt.show()
