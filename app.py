import streamlit as st
from utils.loader import load_data
from utils.analyzer import analyze_devices
from utils.database import save_to_database
from utils.charts import (
    battery_chart,
    status_chart,
    hospital_chart,
    error_chart
)
from datetime import datetime
import os

# ================= Page Configuration =================
st.set_page_config(page_title="MediLog", layout="wide")

st.title("🏥 MediLog")

# ================= Load Data =================
df = load_data()
df = analyze_devices(df)
save_to_database(df)

# ================= Sidebar =================
st.sidebar.header("Filters")

hospital = st.sidebar.selectbox(
    "Hospital",
    ["All"] + sorted(df["Hospital_Name"].unique())
)

status = st.sidebar.selectbox(
    "Status",
    ["All"] + sorted(df["Status"].unique())
)

error_code = st.sidebar.selectbox(
    "Error Code",
    ["All"] + sorted(df["Error_Code"].unique())
)

attention = st.sidebar.selectbox(
    "Requires Attention",
    ["All", "Yes", "No"]
)

# ================= Filters =================
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

# ================= Metrics =================
total = len(filtered_df)
healthy = len(filtered_df[filtered_df["Status"] == "Healthy"])
warning = len(filtered_df[filtered_df["Status"] == "Warning"])
critical = len(filtered_df[filtered_df["Status"] == "Critical"])

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Devices", total)
c2.metric("Healthy", healthy)
c3.metric("Warning", warning)
c4.metric("Critical", critical)

# ================= Report =================
if st.button("Generate Report"):

    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/device_report_{timestamp}.txt"

    report = f"""
MediLog Report
==========================

Generated On : {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

Total Devices : {total}
Healthy Devices : {healthy}
Warning Devices : {warning}
Critical Devices : {critical}

Top 5 Error Codes

{filtered_df["Error_Code"].value_counts().head().to_string()}

Hospitals with Most Devices

{filtered_df["Hospital_Name"].value_counts().head().to_string()}
"""

    with open(filename, "w") as file:
        file.write(report)

    st.success(f"Report saved as {filename}")

st.divider()

# ================= Charts =================
chart1, chart2 = st.columns(2)

with chart1:
    st.pyplot(battery_chart(filtered_df))

with chart2:
    st.pyplot(status_chart(filtered_df))

chart3, chart4 = st.columns(2)

with chart3:
    st.pyplot(hospital_chart(filtered_df))

with chart4:
    st.pyplot(error_chart(filtered_df))

st.divider()

# ================= Device Table =================
st.subheader("Device Logs")

st.dataframe(filtered_df, use_container_width=True)