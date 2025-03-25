'''
**********************************************************************************************************
Web Scrapping
**********************************************************************************************************
The below script demonstrates to Web scrap an Image.
**********************************************************************************************************
'''

import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(result.text, 'lxml')
# print(soup)
# print(soup.select('img'))
# print(soup.select('img')[0])
# print(soup.select('.mw-file-element')[0])

image_link = soup.select('.mw-file-element')[1]
print(image_link['src']) 
#returns - //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg

image = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
print(image.content) #shows the binary content of the image file

f = open('D://Aryabhat//ScriptPython//reports//my_computer_image.jpg', 'wb') #wb shows write binary
f.write(image.content)
f.close()