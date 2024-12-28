import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# Data
W_W0 = np.array([1.0731, 1.0599, 1.0470, 1.0343, 1.0220, 1.0100,
                 1.0070, 1.0065, 1.0059, 1.0053, 1.0047, 1.0029,
                 1.0023, 1.0018, 1.0012, 1.0006, 1.0000, 0.9994,
                 0.9988, 0.9983, 0.9868, 0.9756, 0.9646, 0.9539])

A1 = np.array([33, 40, 52, 68, 91.5, 114.9, 121, 121.8,
               123, 124.6, 126, 127.9, 129, 129.4, 130,
               132, 133, 132, 131, 125.1, 70.5, 52, 41, 34])

# Create a plot
plt.figure(figsize=(10, 6))

# Sort the data for smooth spline fitting
sorted_indices = np.argsort(W_W0)
W_W0_sorted = W_W0[sorted_indices]
A1_sorted = A1[sorted_indices]

# Create a smooth spline fit
spline = UnivariateSpline(W_W0_sorted, A1_sorted, s=1)  # s controls the smoothness
x_smooth = np.linspace(W_W0_sorted.min(), W_W0_sorted.max(), 100)
y_smooth = spline(x_smooth)

# Plot the original data points
plt.plot(W_W0, A1, marker='o', linestyle='None', color='blue', label='Data Points')

# Plot the smooth spline line
plt.plot(x_smooth, y_smooth, color='red', label='Smooth Spline Fit')
plt.xlim(0.9, 1.1)  # Set x-axis range from 0.9 to 1.1
# Add labels and title
plt.title('Smooth Plot of $\\frac{W}{W_0}$ vs A1')
plt.xlabel('$\\frac{W}{W_0}$')
plt.ylabel('A1')
plt.grid()
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()
plt.show()