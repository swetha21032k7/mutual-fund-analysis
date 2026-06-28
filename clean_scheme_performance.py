import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# -----------------------------------
# 1. Ensure return columns are numeric
# -----------------------------------
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# -----------------------------------
# 2. Find rows with invalid returns
# -----------------------------------
anomalies = df[df[return_columns].isnull().any(axis=1)]

print("\nNumber of anomalous rows:", len(anomalies))

# -----------------------------------
# 3. Validate expense ratio
# Expected range: 0.1% to 2.5%
# -----------------------------------
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("Invalid Expense Ratio Rows:", len(invalid_expense))

# -----------------------------------
# 4. Remove duplicate rows
# -----------------------------------
df = df.drop_duplicates()

print("Cleaned Shape:", df.shape)

# -----------------------------------
# Save cleaned dataset
# -----------------------------------
output_path = "data/processed/07_scheme_performance_cleaned.csv"

df.to_csv(output_path, index=False)

print(f"\n✅ Cleaned dataset saved to:\n{output_path}")