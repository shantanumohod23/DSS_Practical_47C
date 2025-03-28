# Statistical Description

import pandas as pd

# Load the dataset
data = pd.read_csv("data/framingham.csv")

# Display the first and last few rows
print(data.head(10))
print(data.tail(10))

# Statistical summary
print(data.describe())

# Dataset information
print(data.info())

# Dataset structure
print(f"Shape: {data.shape}")
print(f"Size: {data.size}")
print(f"Dimensions: {data.ndim}")
