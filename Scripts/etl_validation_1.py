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
target_df = pd.read_sql("SELECT * FROM target_table", conn)
print("\n✅ Target table loaded successfully")
print(target_df)

# 4️⃣ Basic Row Count Validation
if len(source_df) == len(target_df):
    print("\n✅ Row count matched!")
else:
    print(f"\n❌ Row count mismatch: Source={len(source_df)}, Target={len(target_df)}")

# 5️⃣ Data Comparison Validation
merged = source_df.merge(target_df, on="id", how="outer", suffixes=('_src', '_tgt'), indicator=True)
mismatched = merged[merged['_merge'] != 'both']

if mismatched.empty:
    print("\n✅ All records matched perfectly between Source and Target!")
else:
    print("\n❌ Data mismatches found:")
    print(mismatched)

# 6️⃣ Close the connection
conn.close()
