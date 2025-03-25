'''
**********************************************************************************************************
Web Scrapping
**********************************************************************************************************
The below script demonstrates to Webscrapping Multiple Pages.
https://toscrape.com/
GOAL: Get title of every book with a 2 star rating.
https://books.toscrape.com/
**********************************************************************************************************
'''

import requests
import bs4

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

"""
page_num = 20
# print(base_url.format('20'))
# print(base_url.format(page_num))

res = requests.get(base_url.format(page_num))

soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup)
# print("List of Products :::\n", soup.select(".product_pod"))
# print("\nLength :::", len(soup.select(".product_pod")))

books = soup.select(".product_pod")
example = books[0]

# APPROACH 1 (DIRTY WAY) - Convert into String and to check if 'star-rating Two' string exists in it. 
print(str(example))
if 'star-rating Three' in str(example):
    print('Yes')
else:
    print('No')

# APPROACH 2 - Use the bs4 (beautiful soup) and grab the class name and check if it is empty or not.
example.select(".star-rating.Three") #the gap between star-rating Three should be filled with a dot(.)
print(example.select(".star-rating.Three"))
if [] == example.select(".star-rating.Three"):
    print('Yes')
else:
    print('No')

# To grab the book title, based on the tag <a>.
print(example.select('a'))
print(example.select('a')[1]['title'])
"""

#Now, combining the above ideas to check for 2 Stars Book (string call in, example.select(rating))
#example.select('a')[1]['title'] to grab the book title

two_start_titles = []

for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    books = soup.select(".product_pod")

    for bk in books:
        if len(bk.select(".star-rating.Two")) != 0:
            book_title = bk.select('a')[1]['title']
            two_start_titles.append(book_title)

print(two_start_titles)