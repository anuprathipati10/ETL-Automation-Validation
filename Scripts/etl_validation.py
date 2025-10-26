import pandas as pd
import pyodbc
from datetime import datetime
import os

# 1️⃣ File paths
base_path = "C:/Users/jaypr/Documents/ETL_Project"
source_file = os.path.join(base_path, "data", "source_data.csv")
report_folder = os.path.join(base_path, "reports")

# Create 'reports' folder if not exists
os.makedirs(report_folder, exist_ok=True)

# 2️⃣ Read Source CSV
source_df = pd.read_csv(source_file)
print("✅ Source CSV loaded successfully")
print(source_df)

# 3️⃣ Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=PRATHIPATI;"               # change if your server name differs
    "DATABASE=ETL_Test_DB;"
    "Trusted_Connection=yes;"
)

# 4️⃣ Read Target Table
target_df = pd.read_sql("SELECT * FROM target_table_2", conn)
print("\n✅ Target table loaded successfully")
print(target_df)

# 5️⃣ Expected Transformations
source_df['expected_name'] = source_df['name'].str.upper()
source_df['expected_salary'] = source_df['salary'] * 1.10  # +10%

# 6️⃣ Join Source and Target
comparison_df = source_df.merge(target_df, on='id', suffixes=('_src', '_tgt'))

# 7️⃣ Transformation Validations
comparison_df['name_match'] = comparison_df['expected_name'] == comparison_df['name_tgt']
comparison_df['salary_match'] = round(comparison_df['expected_salary'], 2) == round(comparison_df['salary_tgt'], 2)
comparison_df['overall_result'] = comparison_df.apply(
    lambda x: "PASS" if x['name_match'] and x['salary_match'] else "FAIL", axis=1
)

# 8️⃣ Generate Report
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_file = os.path.join(report_folder, f"validation_report_{timestamp}.csv")

comparison_df.to_csv(report_file, index=False)

print("\n📊 Validation report generated successfully:")
print(report_file)

# 9️⃣ Print Summary
total = len(comparison_df)
passed = (comparison_df['overall_result'] == 'PASS').sum()
failed = total - passed

print(f"\nSummary:")
print(f"Total Records: {total}")
print(f"✅ Passed: {passed}")
print(f"❌ Failed: {failed}")

if failed == 0:
    print("\n🎯 All transformations validated successfully!")
else:
    print("\n⚠️ Some mismatches found — check the report for details.")

# 🔟 Close connection
conn.close()
