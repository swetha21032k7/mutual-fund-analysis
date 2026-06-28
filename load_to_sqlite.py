import pandas as pd
from sqlalchemy import create_engine

# -----------------------------------
# Create SQLite database
# -----------------------------------
engine = create_engine("sqlite:///bluestock_mf.db")

# -----------------------------------
# Load cleaned datasets
# -----------------------------------

# Fund Master
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

# NAV History
nav = pd.read_csv("data/processed/02_nav_history_cleaned.csv")
nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

# Investor Transactions
transactions = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")
transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

# Scheme Performance
performance = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")
performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

# -----------------------------------
# Verify row counts
# -----------------------------------

print("\n✅ Data Loaded Successfully!\n")

tables = {
    "dim_fund": fund_master,
    "fact_nav": nav,
    "fact_transactions": transactions,
    "fact_performance": performance,
}

for table_name, df in tables.items():
    print(f"{table_name}: {len(df)} rows")