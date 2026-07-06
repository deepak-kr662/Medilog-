import os
from datetime import datetime

import streamlit as st

from utils.loader import load_data
from utils.database import save_to_database
from utils.charts import (
    battery_chart,
    status_chart,
    hospital_chart,
    error_chart
)

# ================= Page Configuration =================

st.set_page_config(
    page_title="MediLog",
    layout="wide"
)

st.title("🏥 MediLog - Connected Medical Device Log Analyzer")

# ================= Sidebar =================

st.sidebar.header("Upload Logs")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV",
    type=["csv"]
)

# ================= Load Data =================

df = load_data(uploaded_file)

save_to_database(df)

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

total = len(filtered_df)

healthy = len(
    filtered_df[
        filtered_df["Status"] == "Healthy"
    ]
)

warning = len(
    filtered_df[
        filtered_df["Status"] == "Warning"
    ]
)

critical = len(
    filtered_df[
        filtered_df["Status"] == "Critical"
    ]
)

avg_health = round(
    filtered_df["Health_Score"].mean(),
    1
)

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Total Devices", total)
c2.metric("Healthy", healthy)
c3.metric("Warning", warning)
c4.metric("Critical", critical)
c5.metric("Avg Health Score", avg_health)

st.divider()

# ================= Alerts Panel =================

st.subheader("🚨 Active Alerts")

a1, a2, a3, a4, a5 = st.columns(5)

low_battery = len(df[df["Battery_Level"] < 20])
high_temp = len(df[df["Temperature"] > 40])
weak_signal = len(df[df["Signal_Strength"] < 40])
bluetooth = len(df[df["Bluetooth_Status"] == "Disconnected"])
sterilization = len(df[df["Sterilization_Status"] == "Failed"])

a1.error(f"Low Battery\n\n{low_battery}")
a2.warning(f"High Temperature\n\n{high_temp}")
a3.warning(f"Weak Signal\n\n{weak_signal}")
a4.info(f"Bluetooth Off\n\n{bluetooth}")
a5.error(f"Sterilization Failed\n\n{sterilization}")

st.divider()

# ================= Charts =================

chart1, chart2 = st.columns(2)

with chart1:
    st.pyplot(
        battery_chart(filtered_df)
    )

with chart2:
    st.pyplot(
        status_chart(filtered_df)
    )

chart3, chart4 = st.columns(2)

with chart3:
    st.pyplot(
        hospital_chart(filtered_df)
    )

with chart4:
    st.pyplot(
        error_chart(filtered_df)
    )

st.divider()

# ================= Device Logs =================

st.subheader("Device Logs")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# ================= Report =================

st.divider()

if st.button("Generate Report"):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"reports/device_report_{timestamp}.txt"
    )

    report = f"""
==============================
MediLog Report
==============================

Generated On:
{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

---------------------------------

Total Devices : {total}

Healthy : {healthy}

Warning : {warning}

Critical : {critical}

Average Health Score : {avg_health}

---------------------------------

Devices Requiring Attention

{len(filtered_df[filtered_df["Requires_Attention"]=="Yes"])}

---------------------------------

Top 5 Error Codes

{filtered_df["Error_Code"].value_counts().head().to_string()}

---------------------------------

Top Hospitals

{filtered_df["Hospital_Name"].value_counts().head().to_string()}

---------------------------------

Alert Summary

Low Battery : {low_battery}

High Temperature : {high_temp}

Weak Signal : {weak_signal}

Bluetooth Disconnected : {bluetooth}

Sterilization Failed : {sterilization}

"""

    with open(
        filename,
        "w"
    ) as file:

        file.write(report)

    st.success(
        f"Report saved successfully!\n\n{filename}"
    )