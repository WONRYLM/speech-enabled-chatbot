import requests
from bs4 import BeautifulSoup
import csv
# Target URL (use a real URL like "https://quotes.toscrape.com")
url = "https://quotes.toscrape.com"
# Send HTTP GET request
response = requests.get(url)
# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all quote elements
    quotes = soup.find_all("span", class_="text")
    author = soup.find_all("small", class_="author")
    print("Quotes:")
    # Create a list and append the quotes and authors
    author_list = []
    quotes_list = []

      # Loop over both quotes and authors together (assuming equal length)
    for i in range(len(quotes)):
        quote_text = quotes[i].text.strip()
        author_name = author[i].text.strip()
        print(f"{i+1}. {quote_text} — {author_name}")
        
        # Add to the lists
        quotes_list.append(quote_text)
        author_list.append(author_name)

    # Saves the data to a CSV file
    with open('quotes.csv', 'w', newline='') as quotes_csv:
        fieldnames = ["Author", "Quote"]
        writer = csv.DictWriter(quotes_csv, fieldnames=fieldnames)
        writer.writeheader()

        # Write the quotes and authors together
        for author, quote in zip(author_list, quotes_list):
            writer.writerow({"Author": author, "Quote": quote})

    print("Data has been saved to quotes.csv.")
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")

#     # for i, author, quote in (authors, quotes ):
#     #     print(f"{author} {quote.text}")
#     for i, quote in enumerate(quotes, 1):
#         print(f"{i}. {quote.text}")
#         quotes_list.append(quote.text)
#     for i, author in enumerate(author, 1):
#         print(f"{i}. {author.text}")
#         author_list.append(author.text)
#     # with open ('quotes.csv', 'w', newline='') as quotes_csv:
#     #     fieldnames = (["Authors","Quotes"])
#     #     writer = csv.writer(quotes_csv)
#     #     writer.writerow(fieldnames)   
#     print(author_list)
#     print(quotes_list) 
# else:
#     print(f"Failed to retrieve page. Status code: {response.status_code}")

    #save to csv file with headings Author and Quote
