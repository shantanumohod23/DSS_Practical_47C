# Data Visualization

import numpy as np
from matplotlib import pyplot as plt 

# Create data
x = np.arange(1, 11)
y = 2 * x  

# Line Chart
plt.plot(x, y)
plt.title("Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Bar Chart
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Scatter Plot
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Histogram
H = [1, 2, 3, 3, 4, 6, 7, 4, 3, 2, 1, 2, 3, 4, 5, 5, 6, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 5, 6, 3, 2, 1, 1, 2]
plt.hist(H)
plt.title("Histogram")
plt.show()
