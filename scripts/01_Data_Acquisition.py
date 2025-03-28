# Data Acquisition

import pandas as pd

# Load the dataset
data = pd.read_csv("data/diabetes_data.csv")

# Display the first few rows
print(data.head())

# Display the last few rows
print(data.tail())
