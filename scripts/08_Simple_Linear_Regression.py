# Simple Linear Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("data/Salary.csv")

# Display basic info
print("Dataset Info:\n")
print(df.info())
print("\nFirst 10 Rows:\n", df.head(10))
print("\nDataset Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())

# Assigning values to X & y
X = df.iloc[:, :-1].values  # Independent variable (Years of Experience)
y = df.iloc[:, -1].values   # Dependent variable (Salary)

# Splitting dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Linear Regression Model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Model Coefficients
print("\nCoefficient (Slope):", lr.coef_)
print("Intercept:", lr.intercept_)

# Model Accuracy
accuracy = lr.score(X_test, y_test) * 100
print("\nModel Accuracy:", accuracy, "%")

# Visualization: Scatter Plot & Regression Line
plt.scatter(X_train, y_train, color='blue', label="Training Data")
plt.scatter(X_test, y_test, color='red', label="Test Data")
plt.plot(X_train, lr.predict(X_train), color='green', label="Regression Line")
plt.title("Simple Linear Regression - Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()
