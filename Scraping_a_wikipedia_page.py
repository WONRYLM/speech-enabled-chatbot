import requests
from bs4 import BeautifulSoup
import csv

# Function to download and parse the Wikipedia page HTML
def get_content(url):
    response = requests.get(url)# Send a GET request to the given URL
    if response.status_code == 200:# Check if the request was successful 
        return BeautifulSoup(response.text, 'html.parser')# Parse the HTML content using BeautifulSoup and return the parsed object
    else:
        # If the request fails
        print(f"Error fetching page: {response.status_code}")
        # Return None indicates failure
        return None

# Function to extract the title of the Wikipedia article
def get_title(soup):
    # Only proceed if soup - parsed HTML- is not None
    if soup:
        return soup.find('h1').text # Find the first <h1> tag containing the title for the article obtain its content
    else: #  Returns 'No Title Found' If soup is None
        return "No Title Found"

# Function to extract the article's main text organized by section headings
def get_article_and_headings(soup):
    # Find the main content container by looking for a <div> with class 'mw-parser-output'
    content = soup.find('div', {'class': 'mw-parser-output'})
    if content is None:# Returns an empty dictionary content is not found 
        print("Content not found.")
        return {}

    # Dictionary to hold sections and their paragraphs
    sections = {}
    # Start with a section named 'Introduction' for paragraphs before first heading
    current_section = "Introduction"
    sections[current_section] = []

    # Loop through all <h2>/section headings and paragraphs inside the content container
    for element in content.find_all(['h2', 'p']):
        # If the element is a section heading (<h2>)
        if element.name == 'h2':
            # Clean the heading text by removing '[edit]' and stripping unwanted whitespaces
            current_section = element.get_text().replace('[edit]', '').strip()
            # Create a new empty list in the dictionary
            sections[current_section] = []
        # If the element is a paragraph 
        elif element.name == 'p':
            # Get the text of the paragraph and strip whitespace
            text = element.get_text().strip()
            # If the paragraph is not empty, append it to the current section's list
            if text:
                sections[current_section].append(text)

    # Return the dictionary containing sections and their paragraphs
    return sections

# Function to extract all internal article links from the page
def get_links(soup):
    # If soup is None, return an empty list 
    if not soup:
        return []

    # Find all anchor tags that with a href attribute
    links = soup.find_all('a', href=True)
    # Set to avoid duplicate links
    internal_links = set()

    # Loop through each link found
    for link in links:
        href = link['href']
        # Check if the href starts with '/wiki/' (indicates a Wikipedia article link)
        # and does NOT contain ':' (which excludes special pages like File:, Category:, etc.)
        if href.startswith('/wiki/') and ':' not in href:
            # Prepend the full Wikipedia URL and add to the set  # Add items to the beginning of the set
            internal_links.add("https://en.wikipedia.org" + href)

    # Convert the set back to a list before returning
    return list(internal_links)

# Main function which controls the scraping process
def scrape_wikipedia(url):
    # Get the parsed HTML of the Wikipedia page
    soup = get_content(url)
    # Return None to indicate failure if fetching/parsing has failed
    if not soup:
        return None

    # Extract the article title from the page
    title = get_title(soup)
    # Extract the text content grouped by section headings
    text_by_section = get_article_and_headings(soup)
    # Extract all internal Wikipedia links
    links = get_links(soup)

    # Return all extracted data in a dictionary
    return {'title': title,'text': text_by_section,'internal_links': links
    }

# Function to save the scraped data into a CSV file for later use
def save_to_csv(data, filename="wikipedia_scrape.csv"):
    # Open a file in write mode, with utf-8 encoding and with no extra newlines
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        # Write the article title as a header row and its value in the next row
        writer.writerow(["Title"])
        writer.writerow([data['title']])

        # Blank row for spacing
        writer.writerow([])
        # Write headers for the sectioned article text
        writer.writerow(["Section", "Paragraph"])
        # Loop through each section and its paragraphs
        for section, paragraphs in data['text'].items():
            for pg in paragraphs:
                # Write the section name and paragraph text as rows
                writer.writerow([section, pg])

        # Blank row for spacing
        writer.writerow([])
        # Write a header row for the internal Wikipedia links
        writer.writerow(["Internal Wikipedia Links"])
        # Write each link on its own row
        for link in data['internal_links']:
            writer.writerow([link])

    # Inform the user that the data was saved successfully
    print(f"Data saved to '{filename}'")

if __name__ == "__main__":
    # URL of the Wikipedia page to scrape
    #
    url = "https://en.wikipedia.org/wiki/Machine_learning"

    # Run the scraping process
    result = scrape_wikipedia(url)

    # Save data to CSV if scraping was successful,
    if result:
        save_to_csv(result)
    else:
        # Notify the user if scraping failed
        print("Failed to scrape the Wikipedia page.")

