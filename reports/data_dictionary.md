# Data Dictionary – Mutual Fund Analysis

## Project
Bluestock Internship – Day 2

---

## Dataset: 01_fund_master.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Mutual fund company |
| scheme_name | Text | Name of the mutual fund scheme |
| category | Text | Fund category (Equity, Debt, etc.) |
| sub_category | Text | Fund sub-category |
| plan | Text | Direct or Regular plan |
| launch_date | Date | Scheme launch date |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Float | Annual expense ratio (%) |
| exit_load_pct | Float | Exit load percentage |
| min_sip_amount | Integer | Minimum SIP amount |
| min_lumpsum_amount | Integer | Minimum lump sum investment |
| fund_manager | Text | Fund manager name |
| risk_category | Text | Risk level |
| sebi_category_code | Text | SEBI category code |

Source: Provided CSV Dataset

---

## Dataset: 02_nav_history.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | AMFI scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

Source: Provided CSV Dataset + MFAPI reference

---

## Dataset: 07_scheme_performance.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | AMFI scheme code |
| scheme_name | Text | Scheme name |
| fund_house | Text | Fund house |
| category | Text | Category |
| plan | Text | Direct/Regular |
| return_1yr_pct | Float | 1-Year Return (%) |
| return_3yr_pct | Float | 3-Year Return (%) |
| return_5yr_pct | Float | 5-Year Return (%) |
| benchmark_3yr_pct | Float | Benchmark return |
| alpha | Float | Alpha value |
| beta | Float | Beta value |
| sharpe_ratio | Float | Sharpe Ratio |
| sortino_ratio | Float | Sortino Ratio |
| std_dev_ann_pct | Float | Annual Standard Deviation |
| max_drawdown_pct | Float | Maximum Drawdown |
| aum_crore | Integer | Assets Under Management (₹ Crore) |
| expense_ratio_pct | Float | Expense Ratio (%) |
| morningstar_rating | Integer | Morningstar Rating |
| risk_grade | Text | Risk Grade |

Source: Provided CSV Dataset

---

## Dataset: 08_investor_transactions.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| investor_id | Text | Unique Investor ID |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | AMFI scheme code |
| transaction_type | Text | SIP / Lumpsum / Redemption |
| amount_inr | Integer | Transaction amount |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | T30 / B30 classification |
| age_group | Text | Investor age group |
| gender | Text | Investor gender |
| annual_income_lakh | Float | Annual income (₹ Lakhs) |
| payment_mode | Text | Payment method |
| kyc_status | Text | KYC verification status |

Source: Provided CSV Dataset

---

## Database

Database: SQLite

File:
bluestock_mf.db

Tables:

- dim_fund
- fact_nav
- fact_transactions
- fact_performance

---

Prepared By:

Swetha S
Bluestock Internship