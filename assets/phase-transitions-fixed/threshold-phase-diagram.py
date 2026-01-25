import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Create grid
x = np.linspace(-2, 2, 500)
a = np.linspace(-2, 2, 500)
X, A = np.meshgrid(x, a)

# Compute phases (assuming k > 0)
# 1 = maps to +infinity (green): x > a
# -1 = maps to -infinity (red): x < a
# 0 = stays at a (blue): x = a (the boundary)
phase = np.zeros_like(X)

phase[X > A] = 1   # +infinity
phase[X < A] = -1  # -infinity

# Create custom colormap with muted/pastel colors
cmap = ListedColormap(['#c97a7a', '#7a9ec9', '#7ac97a'])

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
im = ax.pcolormesh(X, A, phase, cmap=cmap, vmin=-1, vmax=1, shading='auto')

ax.set_xlabel('$x$ (initial condition)', fontsize=12)
ax.set_ylabel('$a$ (parameter)', fontsize=12)
ax.set_title(r'Phase diagram of $\phi_\infty(x; a)$ for $k > 0$', fontsize=14)

# Prominent axes at x=0 and a=0
ax.axhline(y=0, color='black', linestyle='-', linewidth=1.5)
ax.axvline(x=0, color='black', linestyle='-', linewidth=1.5)

# Draw the phase boundary x = a
ax.plot([-2, 2], [-2, 2], color='black', linestyle='--', linewidth=1.5, label='$x = a$')

# Add legend
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
legend_elements = [
    Patch(facecolor='#7ac97a', label=r'$+\infty$'),
    Patch(facecolor='#c97a7a', label=r'$-\infty$'),
    Line2D([0], [0], color='black', linestyle='--', linewidth=1.5, label='$x = a$ (boundary)')
]
ax.legend(handles=legend_elements, loc='upper left')

plt.tight_layout()
plt.savefig('phase_diagram_a.png', dpi=150)
plt.show()
