# 🧩 ETL Automation Validation Project

This project demonstrates **ETL testing automation** using **Python, Pandas, and SQL Server**.

## 🚀 Project Overview

The ETL process performs the following:
- Extracts source data from a CSV file.
- Loads target data from SQL Server.
- Validates transformation rules:
  - Converts names to uppercase.
  - Increases salary by 10%.
- Generates a CSV **validation report** automatically.

## 🗂 Folder Structure

ETL-Automation-Validation/
├── data/ → Source files (CSV)
├── reports/ → Auto-generated validation reports
├── scripts/ → Python validation scripts
├── requirements.txt → Dependencies
└── README.md → Project documentation


## 🧠 Technologies Used

- **Python 3.10**
- **Pandas**
- **PyODBC**
- **SQL Server**
- **Windows CMD / VS Code**

## 🧪 How to Run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt

2.Run the script

python scripts/etl_validation.py

3.Check the report generated inside the reports/ folder.

📊 Example Output
id	name_src	name_tgt	salary_src	salary_tgt	overall_result
1	John	JOHN	50000	55000	PASS
2	Mary	MARY	60000	66000	PASS
🏁 Next Steps

Add pytest for automated test execution.

Integrate with Jenkins for CI/CD validation.

Extend to Snowflake, MySQL, or SnapLogic pipelines.

🧑‍💻 Created by Jayanth — ETL Tester | Python Automation Enthusiast


---

## 🧩 Step 5. Add & Commit Your Files

In CMD:

```bash
git add .
git commit -m "Initial ETL automation project setup"
