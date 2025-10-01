#  ETL Insurance Project

This project demonstrates a complete **ETL (Extract → Transform → Load)** pipeline for **health insurance claims data**.  
The pipeline fetches the dataset from **Kaggle**, cleans and transforms it using **Pandas**, and loads it into a **SQLite database** for analysis.  
Automation is provided via **Prefect** (and Airflow-ready code for future scaling).

---

##  Features
-  **Extract:** Downloads the [Insurance Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance) using `kagglehub`.
-  **Transform:** Cleans data, handles missing values, engineers new features such as:
  - `bmi_category` → *Underweight / Normal / Overweight / Obese*
  - `is_senior` → Identifies senior citizens (age ≥ 60)
-  **Load:** Saves the transformed data into a **SQLite database** (`insurance.db`) for downstream analytics.
- **Automated Orchestration:** Supports running via **Prefect flows** or **Apache Airflow DAG**.
-  **SQL Queries:** Sample queries to analyze trends such as charges by BMI category and smoker status.

---

##  Project Structure
```
etl_insurance_project/
│── etl_flow.py                # Prefect ETL flow
│── insurance.csv              # Raw insurance data (downloaded)
│── insurance.db               # SQLite database
│── README.md                  # Project documentation
│── scripts/
│   ├── extract.py             # Extract logic (Kaggle download)
│   ├── transform.py           # Data cleaning & feature engineering
│   ├── load.py                # Load to SQLite
│   ├── test_queries.py        # Example SQL queries
│   └── __pycache__/           # Python cache files
```

---

## Setup & Installation
1. **Clone the repository** and navigate to the project folder.
2. **Create a virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
4. **Add your Kaggle API key** as `kaggle.json` in the project root (see [Kaggle API docs](https://github.com/Kaggle/kaggle-api)).

---

## Usage
### Run the ETL pipeline with Prefect:
```powershell
python etl_flow.py
```

### Run individual scripts:
```powershell
python scripts/extract.py
python scripts/transform.py
python scripts/load.py
```

### Run SQL queries:
```powershell
python scripts/test_queries.py
```

---

##  Example Analyses
- **Total records**
- **Average charges by BMI category**
- **Senior citizens who are smokers**

---

##  Requirements
- Python 3.8+
- pandas
- kagglehub
- prefect
- sqlalchemy
- sqlite3 (Python built-in)

---

##  References
- [Kaggle Insurance Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- [Prefect Documentation](https://docs.prefect.io/)
- [KaggleHub Documentation](https://github.com/kagglehub/kagglehub)

---

