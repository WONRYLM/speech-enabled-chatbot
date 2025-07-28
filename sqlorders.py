import re
from datetime import datetime

# Replace with the path to your file
with open("orders.sql", "r") as file:
    data = file.read()

# Regex to find all dates in dd/mm/yy format
pattern = r"'(\d{2})/(\d{2})/(\d{2})'"

def convert(match):
    day, month, year = match.groups()
    year = '20' + year if int(year) < 50 else '19' + year
    return f"'{year}/{month}/{day}'"

converted_data = re.sub(pattern, convert, data)

# Save or print the updated SQL
with open("orders_converted.sql", "w") as file:
    file.write(converted_data)
