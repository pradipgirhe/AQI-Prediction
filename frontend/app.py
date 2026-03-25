import sys
import os
import matplotlib.ticker as ticker


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request
from src.predict_model import predict_aqi, categorize_aqi
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get pollutant inputs from form
    pm25 = float(request.form['PM2.5'])
    pm10 = float(request.form['PM10'])
    o3 = float(request.form['O3'])
    no2 = float(request.form['NO2'])
    so2 = float(request.form['SO2'])
    co = float(request.form['CO'])

    # Prepare input data
    input_data = [pm25, pm10, o3, no2, so2, co]

    # Predict AQI
    aqi_prediction = predict_aqi(input_data)

    category, color = categorize_aqi(aqi_prediction)

    plt.figure(figsize=(6, 4))
    plt.bar(['PM2.5', 'PM10', 'O3', 'NO2', 'SO2', 'CO'], input_data, color='#00796b')
    plt.title("Pollutant Levels")
    plt.ylabel("Concentration")
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    chart_data = base64.b64encode(buf.getvalue()).decode()
    buf.close()
    plt.close()

    csv_path = os.path.join(BASE_DIR, "data", "processed", "air_quality.csv")
    df = pd.read_csv(csv_path)
    df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
    df_sorted = df.sort_values("Time")
    plt.figure(figsize=(8, 4))
    plt.plot(df_sorted['Time'], df_sorted['AQI'], marker='o', linestyle='-', color='#d84315')
    plt.xticks(rotation=45)
    plt.title("Historical AQI Trend")
    plt.ylabel("AQI")
    plt.tight_layout()
    ax = plt.gca()
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=10))  # limit number of y ticks
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
    buf_trend = BytesIO()
    plt.savefig(buf_trend, format="png")
    buf_trend.seek(0)
    trend_chart_data = base64.b64encode(buf_trend.getvalue()).decode()
    buf_trend.close()
    plt.close()

    return render_template("index.html",
                           prediction=aqi_prediction,
                           category=category,
                           color=color,
                           chart_data=chart_data,
                           trend_chart_data=trend_chart_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
