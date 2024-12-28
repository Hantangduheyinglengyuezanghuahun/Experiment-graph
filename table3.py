import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# Data
W_W0 = np.array([1.0731, 1.0599, 1.0470, 1.0343, 1.0220, 1.0100,
                 1.0070, 1.0053, 1.0047, 1.0029, 1.0023, 1.0018,
                 1.0012, 1.0006, 1.0000, 0.9994, 0.9988, 0.9983,
                 0.9868, 0.9756, 0.9646, 0.9539])

rho1 = np.array([166, 162, 158, 149, 137, 113, 110, 102,
                  100, 94, 93, 92, 91, 89, 86, 83,
                  82, 81, 43, 32, 26, 23])

# Create a plot
plt.figure(figsize=(10, 6))

# Sort the data for smooth spline fitting
sorted_indices = np.argsort(W_W0)
W_W0_sorted = W_W0[sorted_indices]
rho1_sorted = rho1[sorted_indices]

# Create a smooth spline fit
spline = UnivariateSpline(W_W0_sorted, rho1_sorted, s=1)  # s controls the smoothness
x_smooth = np.linspace(W_W0_sorted.min(), W_W0_sorted.max(), 100)
y_smooth = spline(x_smooth)

# Plot the original data points
plt.plot(W_W0, rho1, marker='o', linestyle='None', color='blue', label='Data Points')

# Plot the smooth spline line
plt.plot(x_smooth, y_smooth, color='red', label='Smooth Spline Fit')
plt.xlim(0.9, 1.1)  # Set x-axis range from 0.9 to 1.1
# Add labels and title
plt.title('Smooth Plot of $\\frac{W}{W_0}$ vs $\\rho_1$')
plt.xlabel('$\\frac{W}{W_0}$')
plt.ylabel('$\\rho_1$')
plt.grid()
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()
plt.show()