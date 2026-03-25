# Air Quality Index Prediction using Machine Learning

## Project Overview

This project predicts the Air Quality Index (AQI) using machine learning based on major air pollutants such as PM2.5, PM10, O3, NO2, SO2, and CO.
It also displays pollutant charts and historical AQI trends through a web interface built using Flask.

## Features

* Predict AQI using trained machine learning model
* Categorize AQI into air quality levels
* Display pollutant concentration bar chart
* Show historical AQI trend graph
* Simple web interface using Flask

## Technologies Used

* Python
* Flask
* Pandas
* Matplotlib
* Machine Learning

## Project Structure

```bash
project/
│── app/
│   └── app.py
│── src/
│   └── predict_model.py
│── data/
│   └── processed/
│       └── air_quality.csv
│── templates/
│   └── index.html
│── README.md
```

## Installation

1. Clone repository

```bash
git clone https://github.com/yourusername/your-repository-name.git
```

2. Move into project folder

```bash
cd your-repository-name
```

3. Install required libraries

```bash
pip install -r requirements.txt
```

## Run Project

```bash
python app.py
```

## Input Parameters

* PM2.5
* PM10
* O3
* NO2
* SO2
* CO

## Output

* Predicted AQI value
* AQI category
* Pollutant level chart
* Historical AQI trend

## AQI Categories

* Good
* Moderate
* Unhealthy for Sensitive Groups
* Unhealthy
* Very Unhealthy
* Hazardous

## Future Scope

* Real-time AQI data integration
* API connection for live pollution data
* More accurate prediction models
* City-wise AQI forecasting

