import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    classification_report
)

# Load Dataset
dataset = pd.read_csv(r"D:\DS_PRACTICE\03-06-2026\Churn_Modelling.csv")

# Independent and Dependent Variables
X = dataset.iloc[:, 3: -1].values
y = dataset.iloc[:, -1].values
print("X=", X)
print("y=", y)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:, 2] = le.fit_transform(X[:, 2])

print("X=",  X)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers= [('encoder', OneHotEncoder(),[1])], remainder= 'passthrough')

X = np.array(ct.fit_transform(X))
# Split Dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=0
)

from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(X_train, y_train)

y_pred =classifier.predict(X_test)


# Predict Test Data
y_pred = classifier.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Accuracy
ac = accuracy_score(y_test, y_pred)
print("Accuracy Score =", ac)

# Test Accuracy
test_accuracy = classifier.score(X_test, y_test)
print("Test Accuracy =", test_accuracy)


# Training Accuracy (Bias)
train_accuracy = classifier.score(X_train, y_train)
print("Training Accuracy =", train_accuracy)


# Classification Report
cr = classification_report(y_test, y_pred)
print("\nClassification Report:")
print(cr)

# Variance Approximation
variance = train_accuracy - test_accuracy
print("Variance =", variance)