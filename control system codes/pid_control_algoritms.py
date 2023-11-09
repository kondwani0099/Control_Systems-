from control import TransferFunction, pid, feedback
import numpy as np
import matplotlib.pyplot as plt

# Simulated system transfer function
num = [1]
den = [10, 1]
sys = TransferFunction(num, den)

# Create a PID controller
Kp = 1.0
Ki = 0.1
Kd = 0.01
controller = pid(Kp, Ki, Kd)

# Create a closed-loop system
closed_loop_sys = feedback(sys * controller, 1)

# Simulate the response to a step input
time, response = np.linspace(0, 10, 1000, retstep=True)
time, response = control.step_response(closed_loop_sys, time)

# Plot the response
plt.plot(time, response)
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Temperature Control with PID')
plt.grid(True)
plt.show()
