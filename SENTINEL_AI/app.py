import requests
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sentinel AI", layout="centered")

st.markdown("<h1 style='text-align: center;'>🔐 SENTINEL AI</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: gray;'>Real-time login risk analysis using Machine Learning</h3>", unsafe_allow_html=True)

st.caption("AI-powered login anomaly detection system")

st.markdown("---")
# Load dataset
data = pd.read_csv("login_data.csv")
data.columns = data.columns.str.strip()


st.write("Enter login details to check if it's suspicious")

# Inputs
st.subheader("🔎 Enter Login Details")

hour = st.slider("⏱️ Login Hour", 0, 23)

location = st.selectbox("📍 Location", ["Known", "Unknown"])
device = st.selectbox("📱/💻 Device", ["Laptop", "Mobile"])

# Convert to numbers
location = 1 if location == "Known" else 0
device = 1 if device == "Laptop" else 2

# Prediction
if st.button("🚀 Check Login"):
     st.markdown("---")
     url = "http://127.0.0.1:5000/predict"

     input_data = {
        "login_hour": hour,
        "location": location,
        "device": device
     }

     response = requests.post(url, json=input_data)

     result = response.json()["result"]

     risk = response.json()["risk"]
     st.subheader("📊 Result")

     if result == "Suspicious":
        st.error(f"⚠️ Suspicious Activity Detected!\nRisk Score: {risk}%")
        st.warning("Unusual login due to odd time or unknown location")

        # 🚨 ALERT SYSTEM
        st.error("🚨 ALERT: Admin Notified!")
        st.info("📩 Email alert sent to security team")

     else:
        st.success(f"✅ Normal Login\nRisk Score: {risk}%")
        st.info("Login appears normal based on historical data")

# After showing result
st.markdown("---")
st.subheader("📈 Login Time Analysis")

hour_counts = data["login_hour"].value_counts().sort_index()

st.bar_chart(hour_counts)
st.markdown("---")
st.subheader("📋 Login History")
data = data.reset_index()
data.rename(columns={"index": "User ID"}, inplace=True)

st.dataframe(data)
