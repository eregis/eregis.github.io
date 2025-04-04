import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Set random seed for reproducibility
np.random.seed(42)

# Create figure with three subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

# Generate original points with overlap (10 green and 10 purple)
n_points = 10
grid_size = 100  # Size of the image grid
green_points = np.random.normal(loc=grid_size/2, scale=5, size=(n_points, 2)).astype(int)
purple_points = np.random.normal(loc=grid_size/2, scale=5, size=(n_points, 2)).astype(int)

# Clip points to stay within grid
green_points = np.clip(green_points, 0, grid_size-1)
purple_points = np.clip(purple_points, 0, grid_size-1)

# First plot: Original points
# Create empty RGB image
img1 = np.zeros((grid_size, grid_size, 3))
# Add green points
for x, y in green_points:
    img1[y, x, 1] = 1  # Green channel
# Add purple points (mix of red and blue)
for x, y in purple_points:
    img1[y, x, 0] = 0.5  # Red channel
    img1[y, x, 2] = 0.5  # Blue channel

ax1.imshow(img1)
ax1.set_title('Original Points')
ax1.axis('off')

# Create separate images for green and purple
green_img = np.zeros((grid_size, grid_size))
purple_img = np.zeros((grid_size, grid_size))

# Add points to separate images
for x, y in green_points:
    green_img[y, x] = 1
for x, y in purple_points:
    purple_img[y, x] = 1

# Second plot: Slightly blurred version
sigma_slight = 1  # Reduced from 2 to 1 for less blur
green_slight = gaussian_filter(green_img, sigma=sigma_slight)
purple_slight = gaussian_filter(purple_img, sigma=sigma_slight)

# Combine into RGB image
img2 = np.zeros((grid_size, grid_size, 3))
img2[:, :, 1] = green_slight / green_slight.max()  # Green channel
img2[:, :, 0] = purple_slight / purple_slight.max() * 0.5  # Red channel for purple
img2[:, :, 2] = purple_slight / purple_slight.max() * 0.5  # Blue channel for purple

ax2.imshow(img2)
ax2.set_title('Slightly Blurred')
ax2.axis('off')

# Third plot: More blurred version
sigma_more = 3  # Reduced from 5 to 3 for less blur
green_blurred = gaussian_filter(green_img, sigma=sigma_more)
purple_blurred = gaussian_filter(purple_img, sigma=sigma_more)

# Combine into RGB image
img3 = np.zeros((grid_size, grid_size, 3))
img3[:, :, 1] = green_blurred / green_blurred.max()  # Green channel
img3[:, :, 0] = purple_blurred / purple_blurred.max() * 0.5  # Red channel for purple
img3[:, :, 2] = purple_blurred / purple_blurred.max() * 0.5  # Blue channel for purple

ax3.imshow(img3)
ax3.set_title('More Blurred')
ax3.axis('off')

# Adjust layout and display
plt.tight_layout()
plt.show()
