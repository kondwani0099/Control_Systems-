import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Simulated system transfer function
num = [1]
den = [10, 1]
system = signal.TransferFunction(num, den)

# PID controller gains
Kp = 1.0
Ki = 0.1
Kd = 0.01

# Time vector
time = np.linspace(0, 10, 1000)

# Simulate the response to a step input
t, response = signal.step(system, T=time)

# Plot the response
plt.plot(t, response)
plt.xlabel('Time')
plt.ylabel('Response')
plt.title('System Response with PID Control')
plt.grid(True)
plt.show()
