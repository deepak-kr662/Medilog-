# 🏥 MediLog

MediLog is a Python-based dashboard that analyzes simulated logs from connected medical devices. It is designed as a learning project to demonstrate how engineers can monitor device health, identify potential issues, and generate simple reports using Python.

The application reads device log data from a CSV file (or an uploaded CSV), performs rule-based analysis, stores the processed data in SQLite, and displays the results through an interactive Streamlit dashboard.

---

## Features

- Dashboard showing total, healthy, warning, and critical devices
- Rule-based anomaly detection
- Health Score (0–100) for each device
- Alerts for:
  - Low Battery
  - High Temperature
  - Weak Signal
  - Bluetooth Disconnected
  - Sterilization Failed
- Upload custom CSV log files
- Filter devices by:
  - Hospital
  - Status
  - Error Code
  - Requires Attention
- Interactive charts using Matplotlib
- Store processed logs in SQLite
- Generate timestamped health reports
- Modular Python project structure

---

## Tech Stack

- Python 3
- Streamlit
- Pandas
- SQLite
- Matplotlib
- Git
- GitHub
- VS Code

---

## Project Structure

```
Medilog/
│
├── app.py
├── device_logs.csv
├── generate_data.py
├── requirements.txt
├── README.md
│
├── database/
│   └── device_logs.db
│
├── reports/
│
├── charts/
│
└── utils/
    ├── loader.py
    ├── analyzer.py
    ├── database.py
    └── charts.py
```

---

## Device Health Analysis

Each device starts with a Health Score of **100**.

The score is reduced when any of the following conditions are detected:

- Battery Level below 20%
- Temperature above 40°C
- Signal Strength below 40%
- Bluetooth Disconnected
- Sterilization Failed

Devices with one or more issues are marked as **Requires Attention**.

---

## Dashboard

The Streamlit dashboard includes:

- Device summary metrics
- Average Health Score
- Active alerts
- Battery level distribution
- Device status distribution
- Hospital-wise device count
- Top error codes
- Searchable and filterable device table

---

## Report Generation

The application generates a text report containing:

- Total devices
- Healthy, Warning and Critical device count
- Average Health Score
- Top Error Codes
- Hospital summary
- Alert summary

Reports are saved automatically inside the **reports/** folder with a timestamp.

---

## Installation

Clone the repository

```bash
git clone https://github.com/deepak-kr662/Medilog-.git
```

Go to the project folder

```bash
cd Medilog
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Sample Dataset

The project uses a simulated dataset of approximately 500 connected medical device logs.

The dataset includes:

- Device ID
- Timestamp
- Hospital Name
- Firmware Version
- Battery Level
- Temperature
- Signal Strength
- Bluetooth Status
- Sterilization Status
- Error Code
- Device Status

No real patient information or confidential data is used.

---

## Future Improvements

Some ideas for extending the project:

- Email alert notifications
- Device maintenance history
- PDF report generation
- Authentication
- Live device monitoring
- REST API integration

---

## Author

**Deepak Kumar**

GitHub: https://github.com/deepak-kr662
