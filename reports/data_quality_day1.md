# Mutual Fund Analysis Project

## Day 1 Report – Project Setup & Data Ingestion (ETL)

### Intern Details

**Name:** Swetha S
**Project:** Mutual Fund Analysis Dashboard
**Task:** Day 1 – Project Setup and Data Ingestion (ETL)

---

## 1. Objective

The objective of Day 1 was to establish the project structure, ingest the provided mutual fund datasets, integrate live NAV data through API calls, perform initial data exploration, and validate AMFI scheme codes for data consistency.

---

## 2. Project Setup

A structured project directory was created to support the complete analytics workflow.

### Folder Structure

* data/raw
* data/processed
* notebooks
* sql
* dashboard
* reports

Git was initialized and the project repository was connected to GitHub for version control.

---

## 3. Environment Setup

A requirements.txt file was created containing the necessary Python libraries:

* pandas
* numpy
* matplotlib
* seaborn
* plotly
* sqlalchemy
* requests
* scipy
* jupyter

These libraries provide support for data ingestion, analysis, visualization, API integration, and dashboard development.

---

## 4. Dataset Ingestion

A Python script (`data_ingestion.py`) was developed to load and profile all provided CSV datasets.

### Activities Performed

* Loaded all CSV files from the data/raw directory.
* Examined dataset dimensions using `.shape`.
* Inspected column data types using `.dtypes`.
* Reviewed sample records using `.head()`.
* Checked missing values using `.isnull().sum()`.

### Outcome

* All provided datasets were loaded successfully.
* Dataset structures were inspected and documented.
* Initial data quality checks were completed.

---

## 5. Live NAV Data Integration

A separate script (`live_nav_fetch.py`) was developed to fetch real-time mutual fund NAV data using the MFAPI service.

### API Endpoint

https://api.mfapi.in/mf/{scheme_code}

### Schemes Fetched

| Scheme Name      | AMFI Code |
| ---------------- | --------- |
| HDFC Top 100     | 125497    |
| SBI Bluechip     | 119551    |
| ICICI Bluechip   | 120503    |
| Nippon Large Cap | 118632    |
| Axis Bluechip    | 119092    |
| Kotak Bluechip   | 120841    |

### Activities Performed

* Sent API requests using the requests library.
* Parsed JSON responses.
* Converted NAV history into Pandas DataFrames.
* Saved fetched data as CSV files in the data/raw directory.

### Outcome

* Live NAV data for six mutual fund schemes was successfully collected and stored.
* API integration workflow was validated.

---

## 6. Fund Master Exploration

The fund master dataset (`01_fund_master.csv`) was analyzed to understand its structure and metadata.

### Key Columns Identified

* amfi_code
* fund_house
* scheme_name
* category
* sub_category
* plan
* launch_date
* benchmark
* expense_ratio_pct
* exit_load_pct
* min_sip_amount
* min_lumpsum_amount
* fund_manager
* risk_category
* sebi_category_code

### Insights

#### Fund Houses

The dataset contains mutual funds from major fund houses including:

* SBI Mutual Fund
* HDFC Mutual Fund
* ICICI Prudential MF
* Nippon India MF
* Kotak Mahindra MF
* Axis Mutual Fund
* Aditya Birla Sun Life MF
* UTI Mutual Fund
* Mirae Asset MF
* DSP Mutual Fund

#### Categories

* Equity
* Debt

#### Sub-Categories

* Large Cap
* Mid Cap
* Small Cap
* Flexi Cap
* Value
* Index
* Index/ETF
* Liquid
* Gilt
* Short Duration
* Large & Mid Cap
* ELSS

---

## 7. AMFI Code Validation

A validation script (`amfi_validation.py`) was developed to compare AMFI scheme codes available in the fund master dataset against the fetched NAV datasets.

### Validation Results

* Total AMFI Codes in Fund Master: 40
* Total NAV Schemes Fetched: 6
* Matching Percentage: 15%

### Observation

The mismatch is expected because live NAV data was fetched only for a selected set of schemes rather than the complete fund master dataset.

### Conclusion

The validation confirms that the fetched NAV datasets correspond correctly to the selected AMFI scheme codes and that the ingestion pipeline functions as expected.

---

## 8. Data Quality Summary

### Findings

* All datasets were loaded successfully.
* No critical ingestion failures occurred.
* Dataset schemas were identified and documented.
* Live NAV API integration was successful.
* AMFI code validation logic was implemented successfully.

### Areas for Future Improvement

* Standardize date formats across datasets.
* Handle missing values where applicable.
* Expand NAV ingestion to all available schemes.
* Build a consolidated processed dataset for analytics.

---

## 9. Deliverables Completed

### Source Code

* data_ingestion.py
* live_nav_fetch.py
* fund_exploration.py
* amfi_validation.py

### Documentation

* Day 1 Report
* Data Quality Summary

### Data Assets

* 10 Provided CSV Datasets
* 6 Live NAV Datasets

### Repository

* Git repository initialized
* Changes committed and pushed to GitHub

---

## 10. Conclusion

Day 1 objectives were successfully completed. The project environment was configured, datasets were ingested and explored, live NAV data was integrated through APIs, and AMFI validation was performed. The project is now ready for the next phase involving data cleaning, transformation, and dashboard preparation.
