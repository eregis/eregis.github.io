import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm, uniform

# Function for Dirac delta approximation
def rectangle(x, center, width, height):
    return np.where((x >= center - width/2) & (x <= center + width/2), height, 0)

def dirac_delta(x):
    return np.where(np.abs(x) < 0.01, 1, 0)

# Plot 1: Dirac Delta Approximation
plt.figure(figsize=(12, 6))
x = np.linspace(-1, 1, 1000)
colors = ['blue', 'green', 'red', 'cyan', 'magenta']
for i, width in enumerate([0.5, 0.2, 0.1, 0.05, 0.02]):
    height = 1 / width
    y = rectangle(x, 0, width, height)
    plt.plot(x, y, color=colors[i], label=f'Width: {width}')

y_delta = dirac_delta(x)
plt.plot(x, y_delta, 'k', label='Dirac delta')

plt.xlim(-1, 1)
plt.ylim(0, 60)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximations of Dirac Delta Function')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: Log-normal distribution
plt.figure(figsize=(12, 6))
x_lognorm = np.linspace(0, 5, 1000)
mu, sigma = 0, 0.5  # mean and standard deviation of the underlying normal distribution
y_lognorm = lognorm.pdf(x_lognorm, s=sigma, scale=np.exp(mu))

plt.plot(x_lognorm, y_lognorm, 'b', label='Log-normal')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Log-normal Distribution (μ=0, σ=0.5)')
plt.legend()
plt.grid(True)
plt.show()

# Plot 3: Log-uniform distribution
plt.figure(figsize=(12, 6))
a, b = 1, np.e**3  # range for the uniform distribution
x_loguniform = np.linspace(0.5, 25, 1000)
y_loguniform = uniform.pdf(np.log(x_loguniform), loc=np.log(a), scale=np.log(b)-np.log(a)) / x_loguniform

plt.plot(x_loguniform, y_loguniform, 'r', label='Log-uniform')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Log-uniform Distribution (a=1, b=e^3)')
plt.legend()
plt.grid(True)
plt.show()
