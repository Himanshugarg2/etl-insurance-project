import pandas as pd
import kagglehub
import os
import logging

logging.basicConfig(level=logging.INFO)

def extract_data_from_kaggle(dataset_name="mirichoi0218/insurance"):
    """
    Downloads a dataset from Kaggle using kagglehub and loads the first CSV file into a DataFrame.
    """
    logging.info(f"Downloading dataset: {dataset_name}")
    path = kagglehub.dataset_download(dataset_name)
    
    if not path or not os.path.exists(path):
        raise FileNotFoundError("Dataset download failed or path is invalid.")
    
    logging.info(f"Dataset downloaded at: {path}")

    csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
    if csv_files:
        csv_path = os.path.join(path, csv_files[0])
        logging.info(f"Loading data from: {csv_path}")
        
        df = pd.read_csv(csv_path)
        logging.info(f"Data loaded successfully with shape: {df.shape}")

        local_save_path = "insurance.csv"
        df.to_csv(local_save_path, index=False)
        logging.info(f"Saved dataset locally as: {local_save_path}")

        return df
    else:
        raise FileNotFoundError("No CSV files found in the downloaded dataset.")

def extract_data(file_path):
    """
    Loads a dataset from a local CSV file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    logging.info(f"Loading data from local file: {file_path}")
    return pd.read_csv(file_path)

if __name__ == "__main__":
    try:
        data = extract_data_from_kaggle()
        print(data.head())
        print(f"Dataset shape: {data.shape}")
        print(f"Columns: {list(data.columns)}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
