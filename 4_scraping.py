from bs4 import BeautifulSoup
from collections import defaultdict
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url='https://quotes.toscrape.com/page/'

def get_quotes_count_per_tag(num_pages):
    tag_count = defaultdict(int)
    for page in range(1,num_pages):
        response = requests.get(url + str(page) + '/', verify = False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            tags = soup.find_all(class_='tag')
            for tag in tags:
                tag_name = tag.get_text()
                tag_count[tag_name] += 1
        else:
            print("Error: Exited with status code: " + response.status_code)

    sorted_tag_count = dict(sorted(tag_count.items(), key = lambda item: item[1], reverse = True))
    for tag, count in sorted_tag_count.items():
        print(f"{tag}: {count}")

num_pages = int(input("Enter the number of pages to scrape: "))
get_quotes_count_per_tag(num_pages)