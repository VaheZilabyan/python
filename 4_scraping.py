import requests
from bs4 import BeautifulSoup
from collections import defaultdict

base_url = "https://quotes.toscrape.com/page/"

def get_quotes_count_per_tag(num_pages):
    tag_counts = defaultdict(int)
    
    for page_number in range(1, num_pages + 1):
        url = base_url + str(page_number)
        response = requests.get(url, verify = False)
        soup = BeautifulSoup(response.text, "html.parser")
        quote_elements = soup.find_all("div", class_="quote")
        for quote_element in quote_elements:
            tag_elements = quote_element.find_all("a", class_="tag")
            for tag_element in tag_elements:
                tag = tag_element.get_text(strip=True)
                tag_counts[tag] += 1
    
    return tag_counts

num_pages = int(input("Enter the number of pages to scrape: "))
tag_counts = get_quotes_count_per_tag(num_pages)

for tag, count in tag_counts.items():
    print(f"Tag: '{tag}' - Count: {count}")
