# SVM Classifier

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
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
columns_to_fill = ['education', 'glucose', 'heartRate', 'BMI', 'cigsPerDay', 'totChol', 'BPMeds']
for col in columns_to_fill:
    df[col].fillna(df[col].mean(), inplace=True)

# Check if missing values are handled
print("\nMissing Values After Treatment:\n", df.isna().sum())

# Splitting independent (X) and dependent (y) variables
X = df.drop("TenYearCHD", axis=1)
y = df["TenYearCHD"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# SVM Classifier
svc = SVC(kernel='linear')  # Using linear kernel
svc.fit(X_train, y_train)

# Predictions
y_pred = svc.predict(X_test)

# Model Accuracy
train_accuracy = svc.score(X_train, y_train) * 100
test_accuracy = accuracy_score(y_test, y_pred) * 100
print("\nModel Training Accuracy:", train_accuracy, "%")
print("Model Testing Accuracy:", test_accuracy, "%")

# Confusion Matrix & Classification Report
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Plot Confusion Matrix
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix for SVM")
plt.show()
