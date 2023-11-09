import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# System parameters
omega_n = 2.0       # Natural frequency
zeta = 0.2         # Damping ratio

# Create a transfer function for the second-order system
num = [omega_n**2]
den = [1, 2*zeta*omega_n, omega_n**2]
system = signal.TransferFunction(num, den)

# Time vector
time = np.linspace(0, 10, 1000)

# Simulate the response to a step input
t, response = signal.step(system, T=time)

# Plot the response
plt.plot(t, response)
plt.xlabel('Time')
plt.ylabel('Response')
plt.title(f'System Response with Damping ζ = {zeta}')
plt.grid(True)
plt.show()
