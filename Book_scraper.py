import requests
from bs4 import BeautifulSoup
import time
import csv

BASE_URL = "http://books.toscrape.com/"
current_url = BASE_URL


# Keep scraping pages while there is a URL to visit
Titles_list = []
Prices_list = []
Availability_list = []

while current_url:
    # Send a request to the current page and get the HTML content
    response = requests.get(current_url)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    # Find all book containers on the page
    books = soup.find_all("article", class_="product_pod")

    # Loops through each book to get the info needed
    for book in books:
        # Gets the title
        title = book.h3.a["title"]
        # Checks for the price of the book
        price = book.find("p", class_="price_color").text
        # Checks for the availability
        availability = book.find("p", class_="instock availability").text.strip() # Remove extra spaces
        Titles_list.append(title)
        Prices_list.append(price)
        Availability_list.append(availability)
        print(f'Book: "{title}", Price: {price}, Availability: {availability}')

        # Save into csv .Title, Price, Availability
        with open ('books.csv',mode = 'w',newline = '' ) as book_data:
          writer = csv.writer(book_data)
          writer.writerow(['Title','Price','Availability'])
          for row in zip(Titles_list,Prices_list,Availability_list):
            writer.writerow(row)

            # Switch the price into an integer



    # Looks for the next button to find the link to the next page
    next_btn = soup.find("li", class_="next")

    if next_btn:
        next_page_url = next_btn.a["href"]
        # Update the current pages' url to the next pages' URL
        current_url = BASE_URL + next_page_url
    else:
        # Stop the loop
        current_url = None
time.sleep(1) # Prevents overloading the website requests