import requests
import pandas as pd

def fetch_nav(scheme_code, scheme_name):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌ Failed: {scheme_name}")
        return None

    data = response.json()

    nav_data = data.get("data", [])

    df = pd.DataFrame(nav_data)

    df["scheme_code"] = scheme_code
    df["scheme_name"] = scheme_name

    file_path = f"data/raw/live_nav_{scheme_code}.csv"
    df.to_csv(file_path, index=False)

    print(f"✅ Saved: {file_path}")

    return df


# REQUIRED SCHEMES (Bluestock Task)
schemes = {
    "HDFC Top 100": 125497,
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}

for name, code in schemes.items():
    fetch_nav(code, name)

print("\n🎯 All NAV data fetched successfully!")