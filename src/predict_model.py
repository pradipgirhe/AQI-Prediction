import numpy as np
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "../models/linear_regression_aqi_model.pkl")
scaler_path = os.path.join(BASE_DIR, "../models/scaler.pkl")

with open(model_path, "rb") as file:
    model = pickle.load(file)

with open(scaler_path, "rb") as file:
    scaler = pickle.load(file)

def predict_aqi(input_data):
    input_array = np.array(input_data).reshape(-1, 1).T  # reshape to (1, n_features)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)
    return float(prediction[0])

def categorize_aqi(aqi):
    if aqi <= 50:
        return "Good", "#4caf50"
    elif aqi <= 100:
        return "Moderate", "#ffeb3b"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups", "#ff9800"
    elif aqi <= 200:
        return "Unhealthy", "#f44336"
    elif aqi <= 300:
        return "Very Unhealthy", "#9c27b0"
    else:
        return "Hazardous", "#7e0023"
