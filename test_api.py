import requests

url = "https://api.mfapi.in/mf/125497"
data = requests.get(url).json()

print(data["meta"])
