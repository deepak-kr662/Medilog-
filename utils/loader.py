import pandas as pd


def load_data():
    df = pd.read_csv("device_logs.csv")

    # Replace missing error codes with "None"
    df["Error_Code"] = df["Error_Code"].fillna("None").astype(str)

    return df