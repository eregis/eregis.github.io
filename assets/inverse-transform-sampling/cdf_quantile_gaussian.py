import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Create figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Generate x values for CDF
x_cdf = np.linspace(-4, 4, 1000)
# Calculate CDF values using scipy's norm.cdf
y_cdf = norm.cdf(x_cdf)

# Generate p values for quantile function (from 0 to 1)
p = np.linspace(0.001, 0.999, 1000)  # avoid exact 0 and 1 due to infinity
# Calculate quantile values using scipy's norm.ppf (percent point function = quantile function)
x_quantile = norm.ppf(p)

# Plot CDF
ax1.plot(x_cdf, y_cdf, 'b-', lw=2)
ax1.grid(True)
ax1.set_title('Standard Normal CDF (Φ)')
ax1.set_xlabel('x')
ax1.set_ylabel('Φ(x)')
ax1.set_ylim(-0.1, 1.1)

# Plot quantile function
ax2.plot(p, x_quantile, 'r-', lw=2)
ax2.grid(True)
ax2.set_title('Standard Normal Quantile Function (Φ⁻¹)')
ax2.set_xlabel('p')
ax2.set_ylabel('Φ⁻¹(p)')

# Add horizontal and vertical lines at 0.5 probability and 0 value
ax1.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
ax1.axvline(x=0, color='gray', linestyle='--', alpha=0.5)
ax2.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
ax2.axvline(x=0.5, color='gray', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
