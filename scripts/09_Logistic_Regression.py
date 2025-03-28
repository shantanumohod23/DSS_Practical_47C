# Logistic Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import warnings

# Ignore warnings for clean output
warnings.filterwarnings('ignore')

# Load dataset
df = pd.read_csv("data/framingham.csv")

# Display dataset info
print("\nDataset Overview:")
print(df.info())
print("\nMissing Values:\n", df.isna().sum())

# Missing Value Treatment (Replacing with column mean)
columns_to_fill = ['glucose', 'education', 'heartRate', 'BMI', 'cigsPerDay', 'totChol', 'BPMeds']
for col in columns_to_fill:
    df[col].fillna(df[col].mean(), inplace=True)

# Check if missing values are handled
print("\nMissing Values After Treatment:\n", df.isna().sum())

# Splitting independent (X) and dependent (y) variables
X = df.drop("TenYearCHD", axis=1)
y = df["TenYearCHD"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Model Accuracy
train_accuracy = model.score(X_train, y_train) * 100
test_accuracy = model.score(X_test, y_test) * 100
print("\nModel Training Accuracy:", train_accuracy, "%")
print("Model Testing Accuracy:", test_accuracy, "%")

# Confusion Matrix & Classification Report
from sklearn.metrics import classification_report, confusion_matrix

y_pred = model.predict(X_test)

print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Visualizing Feature Importance
coefficients = pd.DataFrame({"Feature": X.columns, "Coefficient": model.coef_[0]})
coefficients = coefficients.sort_values(by="Coefficient", ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x="Coefficient", y="Feature", data=coefficients, palette="coolwarm")
plt.title("Feature Importance in Logistic Regression")
plt.show()
