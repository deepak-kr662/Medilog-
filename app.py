import streamlit as st
from utils.loader import load_data

st.set_page_config(page_title="MediLog", layout="wide")

st.title("🏥 MediLog")

df = load_data()

# Dashboard Metrics
total_devices = len(df)
healthy_devices = len(df[df["Status"] == "Healthy"])
warning_devices = len(df[df["Status"] == "Warning"])
critical_devices = len(df[df["Status"] == "Critical"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Devices", total_devices)
col2.metric("Healthy", healthy_devices)
col3.metric("Warning", warning_devices)
col4.metric("Critical", critical_devices)

st.divider()

st.subheader("Device Logs")
st.dataframe(df)