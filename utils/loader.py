import pandas as pd
from utils.analyzer import analyze_devices


def load_data(uploaded_file=None):
    """
    Load device log data from an uploaded CSV file.
    If no file is uploaded, load the default CSV.
    """

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_csv("device_logs.csv")

    # Replace missing Error Codes
    df["Error_Code"] = df["Error_Code"].fillna("None").astype(str)

    # Analyze devices
    df = analyze_devices(df)

    return df