import streamlit as st
import pandas as pd
import os

# Load data
@st.cache_data
def load_data():
    file_path = os.path.join("data", "delhi_aqi.csv")  
    return pd.read_csv(file_path, encoding='ISO-8859-1')

df = load_data()

# Title
st.title("Delhi Air Quality Checker")

# Sidebar: select station
station = st.sidebar.selectbox("Select Station", df['station'].unique())

# Filter data for selected station
filtered_df = df[df['station'] == station]

# Display AQI pollutants
st.subheader(f"AQI Data for: {station}")
st.dataframe(filtered_df[['pollutant_id', 'pollutant_min', 'pollutant_max', 'pollutant_avg']])

# Show decision
avg_aqi = filtered_df['pollutant_avg'].mean()

def get_air_quality_message(aqi):
    if aqi <= 50:
        return "🟢 Good - Safe to go out"
    elif aqi <= 100:
        return "🟡 Moderate - Okay for most"
    elif aqi <= 200:
        return "🟠 Poor - Limit outdoor activities"
    elif aqi <= 300:
        return "🔴 Unhealthy - Avoid going out"
    else:
        return "⚫ Hazardous - Stay indoors"

st.markdown(f"### Overall AQI: **{int(avg_aqi)}**")
st.markdown(f"### Recommendation: **{get_air_quality_message(avg_aqi)}**")
