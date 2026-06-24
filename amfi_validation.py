import pandas as pd
import os

# Load fund master
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

# Collect NAV scheme codes from all NAV files
nav_folder = "data/raw"
nav_codes = set()

for file in os.listdir(nav_folder):
    if file.startswith("live_nav"):
        df = pd.read_csv(os.path.join(nav_folder, file))
        if "scheme_code" in df.columns:
            nav_codes.update(df["scheme_code"].unique())

# AMFI codes from fund master
master_codes = set(fund_master["amfi_code"].unique())

# Find missing codes
missing_codes = master_codes - nav_codes

print("\n📊 TOTAL MASTER CODES:", len(master_codes))
print("📊 TOTAL NAV CODES:", len(nav_codes))

print("\n❌ MISSING CODES:")
print(missing_codes)

print("\n✅ MATCHING PERCENTAGE:")
print(round((len(master_codes - missing_codes) / len(master_codes)) * 100, 2), "% matched")