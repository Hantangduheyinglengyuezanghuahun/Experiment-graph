import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# Data for amplitude and period
amplitude = np.array([19.5, 21, 22, 24, 26, 27.5, 29.5, 30.5, 32.5, 34.5,
                      36, 37.5, 39.5, 41.5, 43, 44.5, 46.5, 48.5, 50,
                      51.5, 53.5, 55.5, 57.5, 59.5, 61.5, 63.5, 65.5,
                      67.5, 69, 71, 73, 75, 77, 79, 81, 83, 84.5, 86,
                      88, 90, 92, 94, 96, 98, 100, 102, 104.5, 106.5,
                      109, 111.5, 113.5, 116.5, 118.5, 121.5, 124,
                      126.5, 129, 131.5, 134.5, 137, 140, 142, 145,
                      147.5, 150])

period = np.array([1.6903, 1.6910, 1.6912, 1.6921, 1.6931, 1.6928, 1.6937,
                   1.6935, 1.6938, 1.6948, 1.6946, 1.6949, 1.6951, 1.6959,
                   1.6963, 1.6959, 1.6961, 1.6967, 1.6969, 1.6970, 1.6972,
                   1.6973, 1.6973, 1.6976, 1.6986, 1.6987, 1.6991, 1.6996,
                   1.6999, 1.7004, 1.7008, 1.7011, 1.7015, 1.7018, 1.7023,
                   1.7024, 1.7030, 1.7034, 1.7041, 1.7044, 1.7046, 1.7053,
                   1.7058, 1.7060, 1.7066, 1.7073, 1.7076, 1.7080, 1.7089,
                   1.7094, 1.7099, 1.7103, 1.7110, 1.7114, 1.7120, 1.7126,
                   1.7130, 1.7136, 1.7142, 1.7147, 1.7152, 1.7158, 1.7164,
                   1.7170, 1.7174])

# Create a scatter plot
plt.scatter(amplitude, period, color='blue', label='Data Points')

# Create a smooth spline fit
spline = UnivariateSpline(amplitude, period, s=0.5)  # s controls the smoothness
x_smooth = np.linspace(amplitude.min(), amplitude.max(), 100)
y_smooth = spline(x_smooth)

# Plot the smooth line
plt.plot(x_smooth, y_smooth, color='red', label='Smooth Spline Fit')

# Add labels and title
plt.title('Amplitude vs Period')
plt.xlabel('Amplitude (振幅θ)')
plt.ylabel('Period (周期T)')
plt.legend()
plt.grid()

# Show the plot
plt.show()
