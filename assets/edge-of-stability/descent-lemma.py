import numpy as np
import matplotlib.pyplot as plt

def quadratic(x, a):
    """Quadratic function f(x) = (a/2) * x^2"""
    return 0.5 * a * x**2

def gradient(x, a):
    """Gradient of quadratic function: f'(x) = a * x"""
    return a * x

def gradient_descent_step(x, a, eta):
    """One step of gradient descent"""
    return x - eta * gradient(x, a)

# Set up the problem
a = 2.0  # Curvature parameter
x_init = 3.0  # Initial position
n_steps = 20  # Number of gradient descent steps

# Define step sizes for three scenarios
eta_small = 0.3 / a    # Small step size (< 1/a)
eta_medium = 1.5 / a   # Medium step size (between 1/a and 2/a)
eta_large = 2.2 / a    # Large step size (> 2/a)

# Run gradient descent for each step size
def run_gradient_descent(x_init, a, eta, n_steps):
    trajectory = [x_init]
    x = x_init
    for _ in range(n_steps):
        x = gradient_descent_step(x, a, eta)
        trajectory.append(x)
    return np.array(trajectory)

trajectory_small = run_gradient_descent(x_init, a, eta_small, n_steps)
trajectory_medium = run_gradient_descent(x_init, a, eta_medium, n_steps)
trajectory_large = run_gradient_descent(x_init, a, eta_large, n_steps)

# Create the figure
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# X-axis for plotting the function
x_plot = np.linspace(-4, 4, 200)
y_plot = quadratic(x_plot, a)

# Plot for each scenario
scenarios = [
    (trajectory_small, eta_small, "Small step size", axes[0]),
    (trajectory_medium, eta_medium, "Medium step size", axes[1]),
    (trajectory_large, eta_large, "Large step size", axes[2])
]

for traj, eta, title, ax in scenarios:
    # Plot the quadratic function
    ax.plot(x_plot, y_plot, 'b-', alpha=0.5, linewidth=2, label='$f(x) = \\frac{a}{2}x^2$')
    
    # Plot the trajectory points
    y_traj = quadratic(traj, a)
    ax.plot(traj, y_traj, 'ro-', markersize=6, alpha=0.7, linewidth=1)
    
    # Mark the starting point
    ax.plot(traj[0], y_traj[0], 'go', markersize=10, label='Start')
    
    # Add arrows to show the path
    for i in range(min(5, len(traj)-1)):
        ax.annotate('', xy=(traj[i+1], y_traj[i+1]), 
                   xytext=(traj[i], y_traj[i]),
                   arrowprops=dict(arrowstyle='->', color='red', alpha=0.5))
    
    # Set labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(f'{title}\n$\\eta = {eta:.3f}$ (${eta*a:.2f}/a$)')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    # Fixed axis limits for all panels
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 15)

# Add main title
fig.suptitle(f'Gradient Descent Convergence: $f(x) = \\frac{{a}}{{2}}x^2$ with $a = {a}$\n' + 
             f'Critical step size: $2/a = {2/a:.3f}$', fontsize=14)

plt.tight_layout()
plt.show()

# Print convergence analysis
print("Convergence Analysis:")
print("Critical step size: η = 2/a")
print("Step size for smooth convergence: η = 1/a")
print("\nScenario Analysis:")
print("1. Small step (η = 0.3/a): η < 1/a → Smooth convergence")
print("2. Medium step (η = 1.5/a): 1/a < η < 2/a → Oscillating convergence")
print("3. Large step (η = 2.2/a): η > 2/a → Divergence")
