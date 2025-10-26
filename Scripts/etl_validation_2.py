import pandas as pd
import pyodbc

# 1️⃣ Read Source CSV
source_file = "C:/Users/jaypr/Documents/ETL_Project/data/source_data.csv"
source_df = pd.read_csv(source_file)
print("✅ Source CSV loaded successfully")
print(source_df)

# 2️⃣ Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=PRATHIPATI;"              
    "DATABASE=ETL_Test_DB;"
    "Trusted_Connection=yes;"
)

# 3️⃣ Read Target Table
target_df = pd.read_sql("SELECT * FROM target_table_2", conn)
print("\n✅ Target table loaded successfully")
print(target_df)

# 4️⃣ Apply expected transformations on Source
source_df['expected_name'] = source_df['name'].str.upper()
source_df['expected_salary'] = source_df['salary'] * 1.10  # +10%

# 5️⃣ Join Source & Target on ID for comparison
comparison_df = source_df.merge(target_df, on='id', suffixes=('_src', '_tgt'))

# 6️⃣ Validation checks
comparison_df['name_match'] = comparison_df['expected_name'] == comparison_df['name_tgt']
comparison_df['salary_match'] = round(comparison_df['expected_salary'], 2) == round(comparison_df['salary_tgt'], 2)

# 7️⃣ Print results
print("\n🔍 Transformation Validation Results:")
print(comparison_df[['id', 'name_src', 'name_tgt', 'name_match', 'salary_src', 'salary_tgt', 'salary_match']])

# 8️⃣ Summary
if comparison_df['name_match'].all() and comparison_df['salary_match'].all():
    print("\n✅ All transformations validated successfully!")
else:
    print("\n❌ Some transformation mismatches found!")

# 9️⃣ Close connection
conn.close()
