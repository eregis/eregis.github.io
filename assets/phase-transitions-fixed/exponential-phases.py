import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Create grid
x = np.linspace(-2, 2, 500)
k = np.linspace(-2, 2, 500)
X, K = np.meshgrid(x, k)

# Compute phases
# 0 = maps to 0 (blue)
# 1 = maps to +infinity (green)
# -1 = maps to -infinity (red)
phase = np.zeros_like(X)

# k > 0 and x != 0: sign(x) * infinity
phase[(K > 0) & (X > 0)] = 1   # +infinity
phase[(K > 0) & (X < 0)] = -1  # -infinity

# k < 0: maps to 0
phase[K < 0] = 0

# k = 0: stays at x (we'll treat this as a boundary)
# k > 0 and x = 0: stays at 0
phase[(K > 0) & (X == 0)] = 0

# Create custom colormap with muted/pastel colors
# Muted red, muted blue, muted green
cmap = ListedColormap(['#c97a7a', '#7a9ec9', '#7ac97a'])

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
im = ax.pcolormesh(X, K, phase, cmap=cmap, vmin=-1, vmax=1, shading='auto')

ax.set_xlabel('$x$ (initial condition)', fontsize=12)
ax.set_ylabel('$k$ (parameter)', fontsize=12)
ax.set_title(r'Phase diagram of $\phi_\infty(x; k)$', fontsize=14)

# Prominent axes at x=0 and k=0
ax.axhline(y=0, color='black', linestyle='-', linewidth=1.5)
ax.axvline(x=0, color='black', linestyle='-', linewidth=1.5)

# Add legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#7ac97a', label=r'$+\infty$'),
    Patch(facecolor='#c97a7a', label=r'$-\infty$'),
    Patch(facecolor='#7a9ec9', label=r'$0$')
]
ax.legend(handles=legend_elements, loc='upper right')

plt.tight_layout()
plt.savefig('phase_diagram.png', dpi=150)
plt.show()
