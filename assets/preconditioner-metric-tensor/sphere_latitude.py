import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Draw a translucent sphere
u = np.linspace(0, 2 * np.pi, 80)
v = np.linspace(0, np.pi, 60)
x_sphere = np.outer(np.cos(u), np.sin(v))
y_sphere = np.outer(np.sin(u), np.sin(v))
z_sphere = np.outer(np.ones_like(u), np.cos(v))
ax.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.07, color='gray',
                edgecolor='lightgray', linewidth=0.2)

# Parameters
dphi = np.pi / 3  # same angular displacement in phi
phi_start = np.pi / 6

# Latitude 1: equator (theta = pi/2)
theta_eq = np.pi / 2
# Latitude 2: near north pole (theta = pi/6, i.e. 30 degrees from pole)
theta_pole = np.pi / 6

# Draw full latitude circles (thin, dashed)
phi_full = np.linspace(0, 2 * np.pi, 200)
for theta_val, color, label in [(theta_eq, '#2166ac', 'Equator'),
                                  (theta_pole, '#b2182b', r'$\theta = \pi/6$')]:
    x_lat = np.sin(theta_val) * np.cos(phi_full)
    y_lat = np.sin(theta_val) * np.sin(phi_full)
    z_lat = np.cos(theta_val) * np.ones_like(phi_full)
    ax.plot(x_lat, y_lat, z_lat, color=color, alpha=0.3, linewidth=0.8,
            linestyle='--')

# Draw highlighted arcs for same dphi
phi_arc = np.linspace(phi_start, phi_start + dphi, 100)

for theta_val, color, zorder, label in [
    (theta_eq, '#2166ac', 10, 'Equator'),
    (theta_pole, '#b2182b', 10, r'Near pole ($\theta=\pi/6$)')
]:
    x_arc = np.sin(theta_val) * np.cos(phi_arc)
    y_arc = np.sin(theta_val) * np.sin(phi_arc)
    z_arc = np.cos(theta_val) * np.ones_like(phi_arc)
    arc_length = np.sin(theta_val) * dphi

    ax.plot(x_arc, y_arc, z_arc, color=color, linewidth=4, alpha=0.9,
            label=f'{label}: arc = {arc_length:.2f}')

    # Mark endpoints
    for phi_val in [phi_start, phi_start + dphi]:
        ax.scatter(np.sin(theta_val) * np.cos(phi_val),
                   np.sin(theta_val) * np.sin(phi_val),
                   np.cos(theta_val),
                   color=color, s=60, zorder=15, edgecolor='black', linewidth=0.5)

# Annotations
ax.text(0.0, 0.0, 1.15, 'N', fontsize=12, ha='center', fontweight='bold')

ax.set_xlim([-1.1, 1.1])
ax.set_ylim([-1.1, 1.1])
ax.set_zlim([-1.1, 1.1])
ax.set_box_aspect([1, 1, 1])
ax.set_axis_off()
ax.view_init(elev=20, azim=35)

ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
ax.set_title(r'Same $\Delta\phi$, different arc lengths', fontsize=14, pad=15)

plt.savefig('C:/Users/ericf/critical-points/assets/preconditioner-metric-tensor/sphere_latitude.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("sphere_latitude.png saved successfully")
