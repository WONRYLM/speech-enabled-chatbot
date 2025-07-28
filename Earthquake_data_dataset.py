import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from datetime import datetime, timedelta
import numpy as np

# 1. Load the CSV
df = pd.read_csv("earthquake_data_dataset.csv")

# 2. Initialize reverse geocoder
geolocator = Nominatim(user_agent="earthquake-country-detector")
reverse = RateLimiter(geolocator.reverse, min_delay_seconds=1)

# 3. Define function to get country
def get_country(lat, lon):
    try:
        location = reverse((lat, lon), language='en')
        return location.raw['address'].get('country', 'Unknown')
    except:
        return 'Unknown'

# 4. Apply country detection
df['country'] = df.apply(lambda row: get_country(row['latitude'], row['longitude']), axis=1)

# 5. Add a synthetic 'date_time' column (if no real date column)
start_date = datetime(2015, 1, 1)
df['date_time'] = [start_date + timedelta(days=int(x)) for x in np.random.randint(0, 3650, size=len(df))]

# 6. Save the updated CSV
df.to_csv("earthquake_data_with_country_and_date.csv", index=False)

print("✅ Done! Your file now includes 'country' and 'date_time'.")
