from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.datasets import load_iris

# 1. Load data and apply required feature scaling
data = load_iris()
X, y = data.data, data.target
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 3. Initialize and train the Support Vector Classifier (SVC)
# Using 'rbf' for non-linear data and C=1.0 for regularization
model = SVC(kernel='rbf', C=1.0)
model.fit(X_train, y_train)

# 4. Evaluate performance
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
