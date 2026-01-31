import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("parkinsons.csv")

# Input (X) and Output (Y)
X = data.drop(['status', 'name'], axis=1)
Y = data['status']

# Scale data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

# Train model
model = SVC(kernel='linear')
model.fit(X_train, Y_train)

# Test accuracy
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(Y_test, pred))

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved successfully!")
