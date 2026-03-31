import matplotlib.pyplot as plt # type: ignore
import numpy as np # pyright: ignore[reportMissingImports]

# Example input data (you can replace this with your own data)
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 25, 15, 30, 20])

# Find index of maximum y value
max_index = np.argmax(y)
max_x = x[max_index]
max_y = y[max_index]

# Create scatter plot
plt.scatter(x, y)

# Highlight the maximum point
plt.scatter(max_x, max_y, marker='o')
plt.text(max_x, max_y, f'({max_x}, {max_y})')

# Labels and title
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot with Highlighted Maximum Point")

# Show plot
plt.show()