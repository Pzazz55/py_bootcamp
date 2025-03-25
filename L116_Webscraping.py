'''
Web Scraping is a general term for techniques involving automating the gathering of data
from website - such as downloading images or information
HTML (Hyper Text Markup Language) is a special code that the browser is able to understand in
order to display something nice for the user to read.
HTML - Used to create the basic structure and content of a Webpage.
CSS - Used for the design and style of a Webpage, where elements are placed and how it looks.
JavaScript - Used to define the interactive elements of a Webpage.
CSS stands for Cascading Style Sheets.
To web scrape using Python, we can use the BeautifulSoup and requests libraries.
pip install requests
pip install lxml
pip install bs4
'''

import requests
import bs4

result = requests.get("https://example.com/")
print(result.text)