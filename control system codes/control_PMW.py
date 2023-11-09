import time

# Constants
Kp = 0.7    # Proportional gain
Ki = 0.1     # Integral gain
setpoint = 25.0  # Desired temperature setpoint (in degrees Celsius)
initial_pwm = 50  # Initial PWM value for motor speed
pwm_range = (0, 255)  # PWM value range

# Simulation setup
current_temp = 30.0  # Initial temperature
dt = 1.0  # Time step (seconds)

integral_term = 0.0
pwm_value = initial_pwm

# Simulate control loop
for _ in range(10):  # Simulate for 10 time steps
    error = setpoint - current_temp
    integral_term += error * dt

    # Calculate control output and limit to PWM range
    control_output = Kp * error + Ki * integral_term
    control_output = max(min(control_output, pwm_range[1]), pwm_range[0])

    pwm_value = initial_pwm + control_output

    # Simulate motor speed adjustment
    print(f"Temperature: {current_temp:.2f}°C, PWM: {pwm_value}")
    
    # Simulate temperature change
    current_temp -= 1.0
    
    time.sleep(dt)  # Simulate time passing

print("Control simulation finished.")
