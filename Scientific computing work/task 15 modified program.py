import numpy as np
import matplotlib.pyplot as plt

# Time in seconds
time = np.array([0, 1, 2, 3, 4, 5, 6],
                dtype=float)

# Vehicle speed in metres per second
velocity = np.array([0, 3, 7, 12, 18, 25, 33],
                    dtype=float)

# Create acceleration array
acceleration = np.zeros_like(velocity)

# Forward difference
acceleration[0] = (
    velocity[1] - velocity[0]
) / (time[1] - time[0])

# Central difference
for i in range(1, len(time) - 1):

    acceleration[i] = (
        velocity[i + 1] - velocity[i - 1]
    ) / (
        time[i + 1] - time[i - 1]
    )

# Backward difference
acceleration[-1] = (
    velocity[-1] - velocity[-2]
) / (
    time[-1] - time[-2]
)

# Display results
for t, v, a in zip(time, velocity, acceleration):
    print(
        f"Time={t:.0f}s, Velocity={v:.1f}m/s, "
        f"Acceleration={a:.2f}m/s^2"
    )

# Plot graph
plt.plot(time, acceleration, marker="o")

plt.xlabel("Time (seconds)")
plt.ylabel("Acceleration (m/s^2)")
plt.title("Vehicle Acceleration Analysis")

plt.grid(True)
plt.show()