# Creation of 1D, 2D, and multidimensional arrays (Data cube/OLAP) using NumPy.

import numpy as np

# Creating a 1D array
a1 = np.array([50, 60, 30, 80, 20, 90])
print("1D Array:")
print(a1)

# Creating a 2D array
a2 = np.array([[50, 60, 30, 80, 20, 90], [10, 40, 60, 70, 80, 90]])
print("\n2D Array:")
print(a2)

# Creating a multidimensional array (3D)
a3 = np.array([
    ['P1', 'P2', 'P3', 'P4'],
    ['AAA', 'BBB', 'CCC', 'DDD'],
    [10, 20, 30, 40]
])
print("\nMultidimensional Array (3D):")
print(a3)
