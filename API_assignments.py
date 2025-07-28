import requests
import json

names = ["emma", "john", "amina", "lucy", "ken"]
results = []

for name in names:
    response = requests.get(f"https://api.agify.io/?name={name}")
    if response.status_code == 200:
        data = response.json()
        results.append(data)
    else:
        print(f"Failed to fetch data for {name}")

with open("ages.json", "w") as file:
    json.dump(results, file, indent=4)

total_age = 0
count_valid_ages = 0

for person in results:
    if person["age"] is not None:
        total_age += person["age"]
        count_valid_ages += 1

if count_valid_ages > 0:
    average_age = total_age / count_valid_ages
    print(f"\n✅ Average predicted age: {average_age:.2f} years")
else:
    print("❌ No valid ages found to calculate average.")
