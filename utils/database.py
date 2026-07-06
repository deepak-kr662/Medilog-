import sqlite3


DATABASE_PATH = "database/device_logs.db"


def save_to_database(df):
    """
    Save the DataFrame to the SQLite database.
    The table is replaced each time new data is loaded.
    """

    connection = sqlite3.connect(DATABASE_PATH)

    df.to_sql(
        name="device_logs",
        con=connection,
        if_exists="replace",
        index=False
    )

    connection.commit()
    connection.close()


def load_from_database():
    """
    Load all device logs from the SQLite database.
    """

    connection = sqlite3.connect(DATABASE_PATH)

    df = connection.execute(
        "SELECT * FROM device_logs"
    ).fetchall()

    columns = [
        description[0]
        for description in connection.execute(
            "SELECT * FROM device_logs"
        ).description
    ]

    connection.close()

    import pandas as pd
    return pd.DataFrame(df, columns=columns)