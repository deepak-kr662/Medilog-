import pandas as pd


def analyze_devices(df):
    df = df.copy()

    attention = []
    health_scores = []
    issues = []

    for _, row in df.iterrows():

        score = 100
        device_issues = []

        # Battery Check
        if row["Battery_Level"] < 20:
            score -= 20
            device_issues.append("Low Battery")

        # Temperature Check
        if row["Temperature"] > 40:
            score -= 20
            device_issues.append("High Temperature")

        # Signal Check
        if row["Signal_Strength"] < 40:
            score -= 20
            device_issues.append("Weak Signal")

        # Bluetooth Check
        if row["Bluetooth_Status"] == "Disconnected":
            score -= 20
            device_issues.append("Bluetooth Disconnected")

        # Sterilization Check
        if row["Sterilization_Status"] == "Failed":
            score -= 20
            device_issues.append("Sterilization Failed")

        # Prevent Negative Score
        score = max(score, 0)

        health_scores.append(score)

        if len(device_issues) > 0:
            attention.append("Yes")
            issues.append(", ".join(device_issues))
        else:
            attention.append("No")
            issues.append("None")

    df["Health_Score"] = health_scores
    df["Requires_Attention"] = attention
    df["Issues"] = issues

    return df