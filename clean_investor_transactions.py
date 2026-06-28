import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# ---------------------------------
# 1. Convert transaction date
# ---------------------------------
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# ---------------------------------
# 2. Standardize transaction types
# ---------------------------------
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Standardize possible variations
transaction_map = {
    "Sip": "SIP",
    "Lump Sum": "Lumpsum",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

df["transaction_type"] = df["transaction_type"].replace(transaction_map)

# ---------------------------------
# 3. Keep only positive amounts
# ---------------------------------
df = df[df["amount_inr"] > 0]

# ---------------------------------
# 4. Standardize KYC status
# ---------------------------------
df["kyc_status"] = (
    df["kyc_status"]
    .str.strip()
    .str.title()
)

valid_kyc = ["Verified", "Pending"]

invalid = df[~df["kyc_status"].isin(valid_kyc)]

if len(invalid) > 0:
    print("\nInvalid KYC values found:")
    print(invalid["kyc_status"].unique())

# ---------------------------------
# 5. Remove duplicates
# ---------------------------------
df = df.drop_duplicates()

print("Cleaned Shape:", df.shape)

# ---------------------------------
# Save cleaned dataset
# ---------------------------------
output_path = "data/processed/08_investor_transactions_cleaned.csv"

df.to_csv(output_path, index=False)

print(f"\n✅ Cleaned dataset saved to:\n{output_path}")