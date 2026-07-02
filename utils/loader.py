import pandas as pd

def load_data():
    df = pd.read_csv("device_logs.csv")
    return df
