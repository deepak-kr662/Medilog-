import matplotlib.pyplot as plt


def battery_chart(df):
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.hist(df["Battery_Level"], bins=10)
    ax.set_title("Battery Level Distribution")
    ax.set_xlabel("Battery Level")
    ax.set_ylabel("Devices")
    return fig


def status_chart(df):
    fig, ax = plt.subplots(figsize=(5, 3))
    df["Status"].value_counts().plot(kind="bar", ax=ax)
    ax.set_title("Device Status")
    return fig


def hospital_chart(df):
    fig, ax = plt.subplots(figsize=(5, 3))
    df["Hospital_Name"].value_counts().plot(kind="bar", ax=ax)
    ax.set_title("Hospital-wise Device Count")
    return fig


def error_chart(df):
    fig, ax = plt.subplots(figsize=(5, 3))

    error_data = df[df["Error_Code"] != "None"]

    error_data["Error_Code"].value_counts().head(5).plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Top 5 Error Codes")

    return fig