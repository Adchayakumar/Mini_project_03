import streamlit as st
import pickle
import numpy as np
import os

model_path = os.path.join('C:/Users/Admin/OneDrive/Desktop/Power_predictor', 'Power_prediction_model.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Feature list
features = ['Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3',
            'hour', 'day', 'month', 'year', 'peak_hours']

# Get feature importances
importances = model.feature_importances_
importance_dict = dict(zip(features, importances))

# --- Title and Instructions ---
st.set_page_config(page_title="Power Prediction", layout="wide")
st.title("🔌 Household Power Consumption Prediction")
st.markdown("Fill the values below to predict **Global Active Power (kW)** and understand how each input matters.")

# --- Input Section ---
col1, col2, col3 = st.columns(3)
with col1:
    day = st.number_input("📅 Day", min_value=1, max_value=31, value=10,
                          help=f"📊 Importance: {importance_dict['day']*100:.2f}%")
with col2:
    month = st.number_input("📆 Month", min_value=1, max_value=12, value=6,
                            help=f"📊 Importance: {importance_dict['month']*100:.2f}%")
with col3:
    year = st.selectbox("📅 Year", [2006, 2007, 2008],
                        help=f"📊 Importance: {importance_dict['year']*100:.2f}%")

hour = st.slider("🕐 Hour of the Day", 0, 23, 14,
                 help=f"📊 Importance: {importance_dict['hour']*100:.2f}%")

# Show peak hour message
if 6 <= hour <= 9 or 17 <= hour <= 22:
    st.info("🌟 This is a **peak hour** time range!")

peak_hours = 1 if 18 <= hour <= 22 else 0

voltage = st.number_input("🔌 Voltage (V)", min_value=200.0, max_value=260.0, value=240.0,
                          help=f"📊 Importance: {importance_dict['Voltage']*100:.2f}%")

global_intensity = st.number_input("⚡ Global Intensity (A)", min_value=0.0, max_value=60.0, value=5.0,
                                   help=f"📊 Importance: {importance_dict['Global_intensity']*100:.2f}%")

sub_metering_1 = st.number_input("🔋 Sub Metering 1 (Wh)", min_value=0.0, max_value=5.0, value=0.0,
                                 help=f"📊 Importance: {importance_dict['Sub_metering_1']*100:.2f}%")

sub_metering_2 = st.number_input("🔋 Sub Metering 2 (Wh)", min_value=0.0, max_value=5.0, value=1.0,
                                 help=f"📊 Importance: {importance_dict['Sub_metering_2']*100:.2f}%")

sub_metering_3 = st.number_input("🔋 Sub Metering 3 (Wh)", min_value=0.0, max_value=40.0, value=5.0,
                                 help=f"📊 Importance: {importance_dict['Sub_metering_3']*100:.2f}%")

# --- Prediction ---
if st.button("🔮 Predict Power Usage"):
    input_data = np.array([[voltage, global_intensity,
                            sub_metering_1, sub_metering_2, sub_metering_3,
                            hour, day, month, year, peak_hours]])

    prediction = model.predict(input_data)[0]
    st.success(f"✅ Predicted Global Active Power: **{prediction:.3f} kW**")
