import pandas as pd


def analyze_devices(df):

    df = df.copy()

    df["Requires_Attention"] = (
        (df["Battery_Level"] < 20) |
        (df["Temperature"] > 40) |
        (df["Signal_Strength"] < 40) |
        (df["Bluetooth_Status"] == "Disconnected") |
        (df["Sterilization_Status"] == "Failed")
    )

    df["Requires_Attention"] = df["Requires_Attention"].map({
        True: "Yes",
        False: "No"
    })

    return df