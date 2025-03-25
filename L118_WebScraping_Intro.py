'''
**********************************************************************************************************
Introduction to Web Scrapping
Reference - Udemy (PIERIAN DATA) by Jose
**********************************************************************************************************
bs4 - BeautifulSpup Liberary
bs4 liberary is used to figuring out what string syntax to pass into the soup.select() method.
**********************************************************************************************************
Prerequisites:
pip install beautifulsoup4
pip install lxml
**********************************************************************************************************
'''
import requests
import bs4

results = requests.get("http://www.example.com")
type(results)

print("##### Before the Beautiful Soup (bs4) ######")
requests.models.Response
print(results.text) #returns the HTML of the above URL

#bs4 liberary will help us navigate through the HTML page and grab the required information from here.
print("##### After the Beautiful Soup (bs4) ######")
soup = bs4.BeautifulSoup(results.text, "lxml")
print(soup)

print("##### Grabbing the individual HTML tag elements ######")
#Returns all the avaliable <title> elements that are avaliable on the HTML page. 
#If more than one element then retuns in a list.

print('Elements :::\n', soup.select('title')) 
print('Value of the Elements :::\n', soup.select('title')[0].getText())

print('Elements :::\n', soup.select('p'))
site_para = soup.select('p')
print('Type of the Element is :::\n', type(site_para[0]))
print('First Element of the Paragraph is :::\n', site_para[0])
print('Text of the First Element of the Paragraph is :::\n', site_para[0].getText())

# python .\python_bootcamp\L118_WebScraping_Intro.py