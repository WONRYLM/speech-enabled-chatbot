import requests
import csv
import time
from datetime import datetime

API_KEY = "b43b05507b0cb186c11cae167ddca6af"  # Replace this with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Open CSV for writing

with open("weather_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["City", "Temperature (°C)", "Weather", "Humidity (%)", "Wind Speed (m/s)", "Timestamp"])  # Write header

while True:
    user_input = input("Please enter names of cities : ").split()
    
    if len(user_input) == 1 and user_input[0].lower() == "exit":
        print(" Exiting ")
        break

    cities = list(set([city.strip() for city in user_input if city.strip()]))

    with open("weather_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
    
        for city in cities:
            params = {"q": city, "appid": API_KEY, "units": "metric"}
            response = requests.get(BASE_URL, params=params)

            if response.status_code == 200:
                data = response.json()
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                temp = data["main"]["temp"]
                weather = data["weather"][0]["description"]
                humidity = data["main"]["humidity"]
                wind_speed = data["wind"]["speed"]

                writer.writerow([city, temp, weather, humidity, wind_speed])
                print(f"✅ Saved data for {city} on {date}")
            else:
                print(f"❌ Failed to get data for {city}: {response.status_code}")
                print("Message :", response.json())
            
            time.sleep(1)  # to avoid API rate limit

