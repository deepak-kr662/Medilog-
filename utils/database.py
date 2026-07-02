import sqlite3


def save_to_database(df):
    connection = sqlite3.connect("database/device_logs.db")

    df.to_sql(
        "device_logs",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()
    