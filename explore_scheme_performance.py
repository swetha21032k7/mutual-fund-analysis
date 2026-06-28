import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

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
print("SHAPE")
print("=" * 60)
print(df.shape)