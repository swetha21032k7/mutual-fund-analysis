import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("=" * 60)
print("COLUMN NAMES")
print("=" * 60)
print(df.columns)

print("\n" + "=" * 60)
print("FIRST 5 ROWS")
print("=" * 60)
print(df.head())

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)
print(df.dtypes)

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)
print(df.isnull().sum())

print("\n" + "=" * 60)
print("TRANSACTION TYPES")
print("=" * 60)
print(df["transaction_type"].unique())

print("\n" + "=" * 60)
print("KYC STATUS")
print("=" * 60)
print(df["kyc_status"].unique())

print("\n" + "=" * 60)
print("SHAPE")
print("=" * 60)
print(df.shape)