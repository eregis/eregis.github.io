import numpy as np
import matplotlib.pyplot as plt

# Quadratic: L(x) = x^2
a = 2.0
L = lambda x: 0.5 * a * x**2
grad_L = lambda x: a * x
hessian = a

x0 = 3.0
x_plot = np.linspace(-1.0, 4.0, 300)

fig, ax = plt.subplots(figsize=(9, 5))

# Plot the quadratic
ax.plot(x_plot, L(x_plot), 'k-', linewidth=2, label=r'$L(x) = x^2$')

# --- Newton's method: one step to minimum ---
x_newton = x0 - grad_L(x0) / hessian  # = 0
ax.plot(x0, L(x0), 'o', color='#2166ac', markersize=11, zorder=10,
        markeredgecolor='black', markeredgewidth=0.8)
ax.annotate('', xy=(x_newton, L(x_newton) + 0.15), xytext=(x0, L(x0)),
            arrowprops=dict(arrowstyle='->', color='#2166ac', lw=2.5,
                            connectionstyle='arc3,rad=-0.2'))
ax.plot(x_newton, L(x_newton), '*', color='#2166ac', markersize=18, zorder=10,
        markeredgecolor='black', markeredgewidth=0.8,
        label="Newton's method (1 step)")

# --- Gradient descent: multiple steps ---
eta = 0.35
x_gd = x0
gd_points_x = [x_gd]
gd_points_y = [L(x_gd)]
for i in range(6):
    x_next = x_gd - eta * grad_L(x_gd)
    gd_points_x.append(x_next)
    gd_points_y.append(L(x_next))
    x_gd = x_next

# Plot GD trajectory
for i in range(len(gd_points_x) - 1):
    ax.annotate('', xy=(gd_points_x[i+1], gd_points_y[i+1] + 0.1),
                xytext=(gd_points_x[i], gd_points_y[i]),
                arrowprops=dict(arrowstyle='->', color='#d6604d', lw=1.5,
                                alpha=0.7))
    if i > 0:  # skip first point (already drawn as blue)
        ax.plot(gd_points_x[i], gd_points_y[i], 'o', color='#d6604d',
                markersize=6, zorder=8, alpha=0.7)

# Label for GD
ax.plot([], [], 'o-', color='#d6604d', markersize=6, alpha=0.7,
        label=r'Gradient descent ($\eta=0.35$, 6 steps)')

# Labels
ax.annotate(r'$x_0$', xy=(x0, L(x0)), xytext=(x0 + 0.15, L(x0) + 0.5),
            fontsize=13, color='#2166ac', fontweight='bold')
ax.annotate(r'$x^*$', xy=(0, 0), xytext=(-0.45, 0.6),
            fontsize=13, color='#2166ac', fontweight='bold')

ax.set_xlabel('$x$', fontsize=13)
ax.set_ylabel('$L(x)$', fontsize=13)
ax.set_title("Newton's Method vs Gradient Descent on a Quadratic", fontsize=13)
ax.legend(fontsize=11, loc='upper center')
ax.grid(True, alpha=0.3)
ax.set_ylim([-0.5, 10])

plt.savefig('C:/Users/ericf/critical-points/assets/preconditioner-metric-tensor/newtons_method.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("newtons_method.png saved successfully")
