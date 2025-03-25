'''
**********************************************************************************************************
Web Scrapping
**********************************************************************************************************
soup.select('div') - All elements with 'div' tag
soup.select('#some_id') - Elements containing id = 'some_id'
soup.select('.some_class') - Elements containing class = 'some_class'
soup.select('div span') - Any elements named span within a div element
soup.select('div > span') - Any element named span directly within a div element, with nothing in between
**********************************************************************************************************
'''
import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(res.text, 'lxml')

# print(soup)

print("Elements of the Class are :::")
classname = soup.select('.vector-toc-text')
print(classname)
# first_item = soup.select('.vector-toc-text')[1]
# print(first_item.getText)

print("\nElements of the Class are :::")
for item in soup.select('.vector-toc-text'):
    print(item.text)

# python .\python_bootcamp\L119_WebScraping_GrabbingElementsOfClass.py