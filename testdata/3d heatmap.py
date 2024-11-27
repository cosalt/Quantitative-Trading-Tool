import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate sample data
x = np.linspace(-5, 5, 100)  # x values
y = np.linspace(-5, 5, 100)  # y values
x, y = np.meshgrid(x, y)      # Create a grid
z = np.sin(np.sqrt(x**2 + y**2))  # Z values (function for heatmap)

# Create a 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Set labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Value')

# Show the plot
plt.show()
