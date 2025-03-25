'''
**********************************************************************************************************
Web Scrapping
**********************************************************************************************************
The below script demonstrates to Webscrapping Multiple Pages.
GOAL: Get the list of quotes and unique authors from the Website.
https://quotes.toscrape.com/
**********************************************************************************************************
'''

import requests
import bs4

page_still_valid = True
authors = set()
quotes = set()
page = 1
base_url = "https://quotes.toscrape.com/page/"

while page_still_valid:
    page_url = base_url + str(page)
    res = requests.get(page_url)

    if "No quotes found!" in res.text:
        break
    
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    for name in soup.select(".author"):
        authors.add(name.text)

    for quo in soup.select(".text"):
        quotes.add(quo.text)

    page = page + 1

print("\n****** The list of unique Authors from the Website are :: ******\n", authors)
print("\n****** The list of quotes from the Website are :: ******\n", quotes)