import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the transfer functions in the Laplace (s) domain
num_tf1 = [1]
den_tf1 = [1, 2, 1]  # Denominator: s^2 + 2s + 1
tf1 = signal.TransferFunction(num_tf1, den_tf1)

num_tf2 = [1]
den_tf2 = [1, 3]     # Denominator: s + 3
tf2 = signal.TransferFunction(num_tf2, den_tf2)

# Define the feedback system using the transfer functions
num_feedback = signal.convolve(tf1.num, tf2.num)
den_feedback = signal.convolve(tf1.den, tf2.den)
feedback_system = signal.TransferFunction(num_feedback, den_feedback)

# Time vector
time = np.linspace(0, 10, 1000)

# Simulate the response to a step input
t, response = signal.step(feedback_system, T=time)

# Plot the response
plt.plot(t, response)
plt.xlabel('Time')
plt.ylabel('Response')
plt.title('System Response with Feedback Loop')
plt.grid(True)
plt.show()
