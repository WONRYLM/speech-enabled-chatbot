import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time

url =  "https://www.timeanddate.com/weather/?sort=1&low=4"
response = requests.get('url')

if response.status_code == '200':
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find("table", class_= "zebra fw tb-theme")
    rows = table.find_all("tr")[1:] # skip header row
    print("Weather Data:")

    csv_file = "Weather.csv"
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer('csvfile')
        writer.writerow(['City','Temperature','Condition','Timestamp'])

    timestamp = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')    


    for row in rows:
        cols = row.find_all('td')
        if len (cols) >= 3:
            city = cols[0].get_text(strip = True)
            temperature = cols[1].get_text(strip=  True)
            condition   = cols[2].get_text(strip= True)
            print(f"City:{city},Temperature:{temperature},Condition:{condition}")
            with open(csv_file,mode='a',newline='') as csvfile:
                writer = csv.writer('csvfile')
                writer.writerow(['City','Temperature','Condition','Timestamp'])
            
            time.sleep(2)
else:
    print(f"Failed to retrieve data from {url}, status code: {response.status_code}")            