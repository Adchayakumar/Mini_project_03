# ⚡ PowerPulse: Household Energy Usage Forecast

PowerPulse is a Streamlit-based web application that predicts household energy consumption using a machine learning model and provides actionable insights into energy usage patterns. This project is aimed at improving energy efficiency and cost savings for households while supporting energy providers in demand forecasting.

---

## 🛠 Problem Statement

In the modern world, energy management is a critical issue for both households and energy providers. Predicting energy consumption accurately enables better planning, cost reduction, and resource optimization.

The goal of this project is to:
- Develop a machine learning model that predicts household energy consumption.
- Analyze historical energy data to derive **actionable insights**.
- Help consumers understand and optimize their energy usage.
- Assist energy providers in improving demand forecasting.

---

## 🎯 Key Features

- 🔋 **Energy Prediction**: Predicts energy consumption using Random Forest based on input features.
- 📊 **Energy Usage Insights**: Visualizes daily, weekly, monthly, and seasonal usage patterns.
- 💡 **Actionable Advice**: Suggests real-world tips to reduce energy costs during peak hours.
- 📈 **Interactive Dashboard**: Built with Streamlit for user-friendly experience.
- 🧠 **Machine Learning Model**: Tree-based regression model trained on public energy dataset.

---

## 📊 Dataset Description

This project uses a **public energy consumption dataset** with the following variables:

| Feature               | Description                                                                                   |
|----------------------|-----------------------------------------------------------------------------------------------|
| `date`, `time`       | Date and time of energy recording                                                             |
| `global_active_power`| Minute-averaged active power (kilowatts)                                                      |
| `global_reactive_power`| Minute-averaged reactive power (kilowatts)                                                 |
| `voltage`            | Minute-averaged voltage (volts)                                                               |
| `global_intensity`   | Minute-averaged current intensity (amperes)                                                   |
| `sub_metering_1`     | Kitchen usage: dishwasher, oven, microwave                                                   |
| `sub_metering_2`     | Laundry room: washing machine, dryer, fridge                                                 |
| `sub_metering_3`     | Electric water heater and AC                                                                 |

Additional engineered features:
- `hour`, `day`, `month`, `year`, `peak_hour` (binary feature indicating high-demand hours)

---

## 🧠 Model Details

- **Model Used**: Random Forest Regressor  
- **Reason**: Robust to outliers and non-linearity (better than Linear Regression for this data)
- **Performance**:
  - 🔹 Average Train MSE: 0.0333
  - 🔹 Average Test MSE: 0.0333
  - ✅ Average Train R²: 0.9776
  - ✅ Average Test R²: 0.9776

---

## 🖥 User Inputs for Prediction

The app uses the following features for prediction:


**Description of Inputs:**

| Feature            | Description                                                       |
|--------------------|-------------------------------------------------------------------|
| `Voltage`          | Minute-averaged voltage (Volts)                                  |
| `Global_intensity` | Minute-averaged current intensity (Amps)                         |
| `Sub_metering_1`   | Kitchen usage (Watt-hours)                                       |
| `Sub_metering_2`   | Laundry room usage (Watt-hours)                                  |
| `Sub_metering_3`   | Water heater & AC usage (Watt-hours)                             |
| `hour`             | Hour of the day (0–23)                                           |
| `day`              | Day of the week (1–7)                                            |
| `month`            | Month of the year (1–12)                                         |
| `year`             | Year of the reading                                              |
| `peak_hour`        | 1 if usage is during peak hours, 0 otherwise                     |

Users can adjust these inputs via sliders, dropdowns, or input fields in the app to receive a **real-time energy usage prediction**.


## 🔍 Technical Tags

`Data Preprocessing`, `Regression Modeling`, `Feature Engineering`,  
`Hyperparameter Tuning`, `Visualization`,  
`Python`, `Scikit-learn`, `Pandas`, `Matplotlib`, `Seaborn`, `Streamlit`

