import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# -----------------------------
# 1. Convert date to datetime
# -----------------------------
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# -----------------------------
# 2. Sort by AMFI code and date
# -----------------------------
df = df.sort_values(by=["amfi_code", "date"])

# -----------------------------
# 3. Forward fill missing NAV
# (within each mutual fund)
# -----------------------------
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# -----------------------------
# 4. Remove duplicate rows
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# 5. Keep only valid NAV values
# -----------------------------
df = df[df["nav"] > 0]

print("Cleaned Shape:", df.shape)

# -----------------------------
# Save cleaned dataset
# -----------------------------
output_path = "data/processed/02_nav_history_cleaned.csv"
df.to_csv(output_path, index=False)

print(f"\n✅ Cleaned dataset saved to:\n{output_path}")