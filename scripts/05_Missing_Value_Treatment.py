# Missing Value Treatment

import pandas as pd

# Load the dataset
data = pd.read_csv("data/Titanic.csv")

# Display dataset overview
print(data.head(25))
print(data.info())

# Statistical summary
print(data.describe())

# Dataset structure
print(f"Shape: {data.shape}")
print(f"Size: {data.size}")
print(f"Dimensions: {data.ndim}")

# Check for missing values
print("Missing values per column:\n", data.isna().sum())

# Drop rows with missing values
cleaned_data = data.dropna()
print("Data after dropping missing values:\n", cleaned_data.head())

# Fill missing values in 'Age' column with mean
data["Age"].fillna(data["Age"].mean(), inplace=True)

# Check for remaining missing values
print("Missing values after treatment:\n", data.isna().sum())
