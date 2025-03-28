# Data Manipulation using Pandas

import pandas as pd

# Load the dataset
data = pd.read_csv("data/Titanic.csv")

# Display dataset overview
print(data.head())
print(data.tail())

# Statistical summary and info
print(data.describe())
print(data.info())

# Dataset structure
print(f"Shape: {data.shape}")
print(f"Size: {data.size}")
print(f"Dimensions: {data.ndim}")
print(f"Columns: {data.columns.tolist()}")

# Drop the 'Age' column (not modifying the original DataFrame)
data_dropped_column = data.drop(labels="Age", axis=1)
print("Data after dropping 'Age' column:\n", data_dropped_column.head())

# Drop the row at index 2 (not modifying the original DataFrame)
data_dropped_row = data.drop(labels=2, axis=0)
print("Data after dropping row at index 2:\n", data_dropped_row.head())
