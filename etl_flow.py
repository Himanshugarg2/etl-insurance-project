import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))
from prefect import flow, task
from extract import extract_data_from_kaggle
from transform import transform_insurance_data
from load import load_to_sqlite
import pandas as pd

@task
def extract_task():
    extract_data_from_kaggle()  # This downloads and saves 'insurance.csv'

@task
def transform_task():
    df = pd.read_csv("insurance.csv")
    return transform_insurance_data(df)

@task
def load_task(df):
    load_to_sqlite(df)

@flow(name="Insurance_ETL_Flow")
def etl_flow():
    extract_task()
    df_clean = transform_task()
    load_task(df_clean)

if __name__ == "__main__":
    etl_flow()