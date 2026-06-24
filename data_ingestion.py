import pandas as pd
import os

raw_data_path = "data/raw"

csv_files = sorted([f for f in os.listdir(raw_data_path) if f.endswith(".csv")])

for file in csv_files:
    print("\n" + "=" * 70)
    print(f"DATASET: {file}")
    print("=" * 70)

    df = pd.read_csv(os.path.join(raw_data_path, file))

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())