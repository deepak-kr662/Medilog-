import streamlit as st
from utils.loader import load_data
from utils.analyzer import analyze_devices

# ================= Page Configuration =================
st.set_page_config(page_title="MediLog", layout="wide")

# ================= Title =================
st.title("🏥 MediLog")

# ================= Load and Analyze Data =================
df = load_data()
df = analyze_devices(df)

# ================= Sidebar Filters =================
st.sidebar.header("Filters")

hospital = st.sidebar.selectbox(
    "Hospital",
    ["All"] + sorted(df["Hospital_Name"].unique().tolist())
)

status = st.sidebar.selectbox(
    "Status",
    ["All"] + sorted(df["Status"].unique().tolist())
)

error_code = st.sidebar.selectbox(
    "Error Code",
    ["All"] + sorted(df["Error_Code"].unique().tolist())
)

attention = st.sidebar.selectbox(
    "Requires Attention",
    ["All", "Yes", "No"]
)

# ================= Apply Filters =================
filtered_df = df.copy()

if hospital != "All":
    filtered_df = filtered_df[
        filtered_df["Hospital_Name"] == hospital
    ]

if status != "All":
    filtered_df = filtered_df[
        filtered_df["Status"] == status
    ]

if error_code != "All":
    filtered_df = filtered_df[
        filtered_df["Error_Code"] == error_code
    ]

if attention != "All":
    filtered_df = filtered_df[
        filtered_df["Requires_Attention"] == attention
    ]

# ================= Dashboard Metrics =================
total_devices = len(filtered_df)
healthy_devices = len(filtered_df[filtered_df["Status"] == "Healthy"])
warning_devices = len(filtered_df[filtered_df["Status"] == "Warning"])
critical_devices = len(filtered_df[filtered_df["Status"] == "Critical"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Devices", total_devices)
col2.metric("Healthy", healthy_devices)
col3.metric("Warning", warning_devices)
col4.metric("Critical", critical_devices)

st.divider()

# ================= Device Table =================
st.subheader("Device Logs")

st.dataframe(filtered_df, use_container_width=True)