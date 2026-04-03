import pandas as pd
from sklearn.ensemble import IsolationForest

# Load dataset
data = pd.read_csv("login_data.csv")

# Train model
model = IsolationForest(contamination=0.4)
model.fit(data)

print("Model trained successfully!")

# Test with a sample input
test = pd.DataFrame([[2, 0, 1]], columns=["login_hour", "location", "device"])  # (2 AM, unknown location, laptop)

prediction = model.predict(test)

if prediction[0] == -1:
    print("⚠️ Suspicious Login Detected")
else:
    print("✅ Normal Login") 