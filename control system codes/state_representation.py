import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define system matrices
A = np.array([[-0.5, -2.0],
              [1.0,  0.0]])
B = np.array([[1.0],
              [0.0]])
C = np.array([[1.0, 0.0]])
D = np.array([[0.0]])

# Define the system dynamics function
def system_dynamics(t, x, u):
    return np.dot(A, x) + np.dot(B, u)

# Initial state and input
x0 = np.array([0.0, 0.0])
u = np.array([1.0])

# Time vector
t_span = (0, 10)
t_eval = np.linspace(*t_span, num=100)

# Solve the state equations
solution = solve_ivp(system_dynamics, t_span, x0, args=(u,), t_eval=t_eval)

# Extract the state variable trajectories
x1 = solution.y[0]
x2 = solution.y[1]

# Plot the state variables
plt.plot(solution.t, x1, label='State 1')
plt.plot(solution.t, x2, label='State 2')
plt.xlabel('Time')
plt.ylabel('State Variables')
plt.title('State-Space Representation')
plt.legend()
plt.grid(True)
plt.show()
