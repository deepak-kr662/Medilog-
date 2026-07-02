import random
from datetime import datetime, timedelta
import pandas as pd

hospitals = [
    "City Hospital",
    "Apollo Hospital",
    "Sunrise Medical",
    "Care Plus",
    "Metro Hospital"
]

firmware_versions = ["1.0.1", "1.1.0", "1.2.0", "2.0.0"]

error_codes = ["None", "E101", "E202", "E303", "E404"]

bluetooth_status = ["Connected", "Disconnected"]

sterilization_status = ["Passed", "Failed"]

status = ["Healthy", "Warning", "Critical"]

rows = []

start_date = datetime.now()

for i in range(1, 501):
    rows.append({
        "Device_ID": f"MD-{1000+i}",
        "Timestamp": start_date - timedelta(minutes=random.randint(1, 100000)),
        "Hospital_Name": random.choice(hospitals),
        "Firmware_Version": random.choice(firmware_versions),
        "Battery_Level": random.randint(5, 100),
        "Temperature": round(random.uniform(30, 45), 1),
        "Signal_Strength": random.randint(20, 100),
        "Bluetooth_Status": random.choice(bluetooth_status),
        "Sterilization_Status": random.choice(sterilization_status),
        "Error_Code": random.choice(error_codes),
        "Status": random.choice(status)
    })

df = pd.DataFrame(rows)

df.to_csv("device_logs.csv", index=False)

print("device_logs.csv created successfully!")