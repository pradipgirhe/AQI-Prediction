import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data():
    return pd.read_excel("data/raw/air_quality.xlsx")

def process_data(data):
    data = data.copy()

    data['AQI'] = pd.to_numeric(data['AQI'], errors='coerce')

    pollutants = ['PM2.5', 'PM10', 'O3', 'NO2', 'SO2', 'CO']

    data[pollutants] = data[pollutants].fillna(data[pollutants].mean())

    data = data.dropna(subset=['AQI'])

    X = data[pollutants]
    y = data['AQI']

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(x_train)
    X_test_scaled = scaler.transform(x_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler

