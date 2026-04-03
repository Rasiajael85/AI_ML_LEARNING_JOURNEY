from flask import Flask, request, jsonify
import pandas as pd
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

# Load dataset
data = pd.read_csv("login_data.csv")

# Train model
model = IsolationForest(contamination=0.4)
model.fit(data)

'''@app.route("/")
def home():
    return "Backend is running!"'''

# 🔥 NEW API
@app.route("/predict", methods=["POST"])
def predict():
    input_data = request.json

    hour = input_data["login_hour"]
    location = input_data["location"]
    device = input_data["device"]

    test = pd.DataFrame([[hour, location, device]],
                        columns=["login_hour", "location", "device"])

    result = model.predict(test)[0]
    score = model.decision_function(test)[0]
    risk = round((1 - score) * 100, 2)
    return jsonify({
        "result": "Suspicious" if result == -1 else "Normal",
        "risk": risk
    })

if __name__ == "__main__":
    app.run(debug=True)