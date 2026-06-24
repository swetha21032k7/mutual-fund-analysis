import pandas as pd

file_path = "data/raw/01_fund_master.csv"
fund_master = pd.read_csv(file_path)

print("\n📌 COLUMNS IN DATASET:")
print(fund_master.columns)

print("\n📊 FUND HOUSE LIST:")
print(fund_master["fund_house"].unique())

print("\n📊 CATEGORY LIST:")
print(fund_master["category"].unique())

print("\n📊 SUB CATEGORY LIST:")
print(fund_master["sub_category"].unique())