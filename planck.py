import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
e = 1.602e-19
n = int(input("Enter the number of data points: "))
frequency = []
stopping_potential = []
print("\nEnter the frequency (in Hz) and stopping potential (in V):")
for i in range(n):
    f = float(input(f"  Frequency {i+1} (Hz): "))
    V = float(input(f"  Stopping potential {i+1} (V): "))
    frequency.append(f)
    stopping_potential.append(V)
f = np.array(frequency)
Vs = np.array(stopping_potential)
slope, intercept, r_value, p_value, std_err = linregress(f, Vs)

h_calculated = slope * e
phi = -intercept * e
threshold_frequency = phi / h_calculated

print("\n----- Results -----")
print(f"Slope (V/Hz): {slope:.4e}")
print(f"Intercept (V): {intercept:.4e}")
print(f"Calculated Planck’s constant (h): {h_calculated:.4e} J·s")
print(f"Work function (φ): {phi:.4e} J")
print(f"Threshold frequency (f₀): {threshold_frequency:.4e} Hz")
print(f"R-squared (R²): {r_value**2:.4f}")

plt.figure(figsize=(8, 5))
plt.scatter(f, Vs, color='blue', label='Measured Data')
plt.plot(f, slope * f + intercept, color='red', label='Linear Fit')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Stopping Potential (V)')
plt.title('Photoelectric Effect: Stopping Potential vs Frequency')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
