import pandas as pd
import sqlite3
import logging
import os

logging.basicConfig(level=logging.INFO)

DB_NAME = "insurance.db"

def load_to_sqlite(df: pd.DataFrame, table_name="insurance_data"):
    """
    Loads transformed data into an SQLite database.
    """
    try:
        logging.info(f"Connecting to SQLite database: {DB_NAME}")
        conn = sqlite3.connect(DB_NAME)

        logging.info(f"Loading data into table: {table_name}")
        df.to_sql(table_name, conn, if_exists='replace', index=False)

        conn.commit()
        logging.info("Data successfully loaded into database!")

        conn.close()

    except Exception as e:
        logging.error(f"Failed to load data: {e}")

if __name__ == "__main__":
    from transform import transform_insurance_data

    df_raw = pd.read_csv("insurance.csv")
    df_clean = transform_insurance_data(df_raw)
    
    load_to_sqlite(df_clean)
