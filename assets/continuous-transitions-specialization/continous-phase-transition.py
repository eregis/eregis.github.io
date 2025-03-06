import numpy as np
import matplotlib.pyplot as plt

# First figure: Magnetization vs Temperature
plt.figure(figsize=(8, 5))
T = np.linspace(0, 2, 1000)  # Temperature normalized by T_c
Tc = 1.0  # Critical temperature
M = np.zeros_like(T)

# Calculate magnetization
# Below Tc: M = ±√(1-(T/Tc)^2) to get semicircle
mask = T < Tc
M[mask] = np.sqrt(1 - (T[mask]/Tc)**2)

plt.plot(T, M, 'b-', linewidth=2, label='M > 0')
plt.plot(T, -M, 'b-', linewidth=2, label='M < 0')
plt.grid(True, alpha=0.3)
plt.xlabel('Temperature (T/Tc)', fontsize=10)
plt.ylabel('Magnetization (M)', fontsize=10)
plt.title('Magnetization vs Temperature', fontsize=12)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.legend()
plt.tight_layout()

# Second figure: Free Energy vs Order Parameter (three subplots)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
axes = [ax1, ax2, ax3]
t_values = [0.5, 0, -0.5]  # Temperature-like parameter
m = np.linspace(-1, 1, 1000)  # Order parameter
c = 1  # Coefficient of quartic term

for ax, t in zip(axes, t_values):
    # Free energy: F = t*m^2 + c*m^4
    F = t * m**2 + c * m**4
    
    ax.plot(m, F, 'b-', linewidth=2)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Order Parameter (m)', fontsize=10)
    ax.set_ylabel('Free Energy (F)', fontsize=10)
    ax.set_title(f't = {t}', fontsize=12)
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)

plt.tight_layout()
plt.show()
