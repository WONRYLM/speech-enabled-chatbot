import requests
import json
import csv
# response = requests.get("https://api.github.com/users/octocat")
# print (response.status_code) # 200 - ok 400 - bad request 404 - not found 401
# print(response.text)
# print(response.json())
# s = response.json()
# print(s['id'])
# print(s['avatar_url'])

response = requests.get("https://official-joke-api.appspot.com/random_joke")
print (response.status_code)
print(response.text)
print(response.json())
# Task : Save to a json file then csv file
# with open ('api.json','w') as data:
#     json.dump(response.json(),data)
data = {}
data  = response.json()
fieldnames = ["type","setup","punchline","id"]
with open ('api_data.csv','w',newline = "") as data_in_csv:
    writer = csv.DictWriter(data_in_csv,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(data)
        

