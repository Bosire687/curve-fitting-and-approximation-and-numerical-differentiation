import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Website visitors and loading time
visitors = np.array([20, 40, 60, 80, 100, 120, 140],
                    dtype=float)

loading_time = np.array([1.2, 1.5, 2.0, 2.8, 3.8, 5.2, 6.9])

# Quadratic model
def model(x, a, b, c):
    return a*x**2 + b*x + c

# Fit model
parameters, covariance = curve_fit(
    model, visitors, loading_time
)

a, b, c = parameters

# Predictions
predicted = model(visitors, a, b, c)

# Calculate error
rmse = np.sqrt(np.mean((loading_time - predicted)**2))

print("Fitted equation:")
print(f"y = {a:.6f}x^2 + {b:.4f}x + {c:.4f}")

print(f"RMSE: {rmse:.4f}")

# Plot
x_plot = np.linspace(20, 160, 300)

plt.scatter(visitors, loading_time,
            label="Actual measurements")

plt.plot(x_plot, model(x_plot, a, b, c),
         label="Fitted curve")

plt.xlabel("Number of website visitors")
plt.ylabel("Loading time (seconds)")
plt.title("Website Performance Analysis")
plt.legend()
plt.grid(True)
plt.show()