import sqlite3
import pandas as pd

# Path to your database
DB_PATH = "insurance.db"

# Connect to the database
conn = sqlite3.connect(DB_PATH)

# 1. Total records
query1 = "SELECT COUNT(*) AS total_records FROM insurance_data;"
df1 = pd.read_sql(query1, conn)
print("\n Total Records:")
print(df1)

# 2. Average charges by BMI category
query2 = """
SELECT bmi_category, ROUND(AVG(charges), 2) AS avg_charges
FROM insurance_data
GROUP BY bmi_category;
"""
df2 = pd.read_sql(query2, conn)
print("\n Average Charges by BMI Category:")
print(df2)

# 3. Senior citizens who are smokers
query3 = """
SELECT COUNT(*) AS senior_smokers
FROM insurance_data
WHERE is_senior = 1 AND smoker = 1;
"""
df3 = pd.read_sql(query3, conn)
print("\n Senior Citizens Who Are Smokers:")
print(df3)

# Close the connection
conn.close()
print("\n All queries executed successfully!")
