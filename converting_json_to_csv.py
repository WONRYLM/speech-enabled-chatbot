import json
import csv

with open('products.json', 'r') as json_file:
    products = json.load(json_file)

with open('products.csv', 'w', newline='') as csv_file:
    fieldnames = ['id', 'name', 'price']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)
# While using DictWriter , you need to pass a list of dictionaries to the writerows() method. 