# Save this as app.py and run with: streamlit run app.py

import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("dns_spoof_detector.pkl")  # change if you have a new trained model

st.set_page_config(page_title="DNS Spoofing Detector", layout="centered")
st.title("🧠 DNS Spoofing Prediction App")

st.markdown("Enter the values below to predict whether the DNS request is **benign** or **spoofed**.")

# User inputs
entropy = st.slider("Domain Entropy", 0.0, 5.0, 2.5, 0.1)
time_gap = st.slider("Time Between Queries (sec)", 0.0, 30.0, 10.0, 0.5)

# Prediction
if st.button("Predict"):
    input_data = np.array([[entropy, time_gap]])
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0]

    label = "🚨 Spoofed" if prediction == 1 else "✅ Benign"
    st.subheader(f"Prediction: {label}")
    st.write(f"**Probability (Benign):** {proba[0]:.2f}")
    st.write(f"**Probability (Spoofed):** {proba[1]:.2f}")
