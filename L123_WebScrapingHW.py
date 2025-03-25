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

base_url = "https://quotes.toscrape.com/page/{}/"

page_num = []
top_tags = []
authors_list = []
quotes_list = []

#1. Snippet to find the last page in the Website
for n in range(1, 30):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    last_page = soup.select('.next')
    for last in last_page:
        page_num.append(last.get_text())

last_page = len(page_num) + 1
print("****** Last Page is :: ******", last_page)

#2. Snippet to find the top 10 tags from the 1st page of the Website
scrape_url = "https://quotes.toscrape.com/page/1/"
res = requests.get(scrape_url)
soup = bs4.BeautifulSoup(res.text, 'lxml')
top_10_tags = soup.select(".tag-item")

for tag in top_10_tags:
    top_tags.append(tag.text)

print("\n****** The top 10 tags in the Website are :: ******\n", top_tags)

#2. Snippet to find the Authors & Quotes from the 1st page of the Website
scrape_url = "https://quotes.toscrape.com/page/1/"
res = requests.get(scrape_url)
soup = bs4.BeautifulSoup(res.text, 'lxml')

authors = soup.select(".author")
for auth in authors:
    authors_list.append(auth.get_text())

authors_unqiue = set(authors_list) # typecasting the list to set, to get the unique Author Names
print("\n****** The list of unique Authors from the First page are :: ******\n", authors_unqiue) #display all the unique authors from the 1st page.

quotes = soup.select(".text")
for quo in quotes:
    quotes_list.append(quo.get_text())

print("\n****** The list of quotes from the First Page are :: ******\n", quotes_list) #display all the quotes from the 1st page.


#Snippet to find all the Authors & quotes in the Website
for n in range(1, last_page):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    authors = soup.select(".author")   
    for auth in authors:
        authors_list.append(auth.get_text())

    quotes = soup.select(".text")
    for quo in quotes:
        quotes_list.append(quo.get_text())

# print(authors_list)
authors_unqiue = set(authors_list) # Typecasting the list to set, to get the unique Authore Names
print("\n****** The list of unique Authors from the Website are :: ******\n", authors_unqiue)
print("\n****** The list of quotes from the Website are :: ******\n", quotes_list)