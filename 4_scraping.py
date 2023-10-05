import requests
from bs4 import BeautifulSoup
from collections import defaultdict

# Base URL of the website
base_url = "https://quotes.toscrape.com/page/"

# Function to get the count of quotes for each tag from multiple pages
def get_quotes_count_per_tag(num_pages):
    # Initialize a defaultdict to store tag counts
    tag_counts = defaultdict(int)
    
    for page_number in range(1, num_pages + 1):
        # Construct the URL for the current page
        url = base_url + str(page_number)
        
        # Send a GET request to the URL
        response = requests.get(url, verify = False)
        
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find all the quote elements
        quote_elements = soup.find_all("div", class_="quote")
        
        # Iterate through the quote elements
        for quote_element in quote_elements:
            # Find the tags within the quote element
            tag_elements = quote_element.find_all("a", class_="tag")
            
            # Extract and increment the count for each tag
            for tag_element in tag_elements:
                tag = tag_element.get_text(strip=True)
                tag_counts[tag] += 1
    
    return tag_counts

# Input: Number of pages to scrape
num_pages = int(input("Enter the number of pages to scrape: "))

# Get the counts for all tags from the specified number of pages
tag_counts = get_quotes_count_per_tag(num_pages)

# Print the result
for tag, count in tag_counts.items():
    print(f"Tag: '{tag}' - Count: {count}")
