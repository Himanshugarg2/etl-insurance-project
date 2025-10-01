import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def transform_insurance_data(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Starting data transformation...")

    # 1. Drop duplicates
    df = df.drop_duplicates()

    # 2. Handle missing values
    df['bmi'] = df['bmi'].fillna(df['bmi'].median())
    df['charges'] = df['charges'].fillna(0)

    # 3. Convert data types
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['children'] = df['children'].astype(int)
    df['charges'] = pd.to_numeric(df['charges'], errors='coerce')

    # 4. Remove invalid age values
    df = df[(df['age'] > 0) & (df['age'] <= 100)]

    # 5. Standardize text columns
    df['sex'] = df['sex'].str.title()
    df['smoker'] = df['smoker'].str.lower().map({'yes': 1, 'no': 0})
    df['region'] = df['region'].str.title()

    # 6. Feature engineering
    def bmi_category(bmi):
        if bmi < 18.5:
            return 'Underweight'
        elif bmi < 25:
            return 'Normal'
        elif bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'
    
    df['bmi_category'] = df['bmi'].apply(bmi_category)
    df['is_senior'] = df['age'].apply(lambda x: 1 if x >= 60 else 0)

    logging.info(f"Transformation complete. Shape: {df.shape}")
    return df

if __name__ == "__main__":
    # Testing with extracted data
    raw_df = pd.read_csv("insurance.csv")
    clean_df = transform_insurance_data(raw_df)
    print(clean_df.head())
