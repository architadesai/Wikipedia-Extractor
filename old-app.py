import re
import urllib.request
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Machine_learning#Theory'

html = urllib.request.urlopen(url)
soup = BeautifulSoup(html)

# data = soup.findAll(text=True)
# data = soup.find("span", {"id": "Theory"})

# data = soup.find("span", {"class": "mw-headline"})

print(soup.find("span",attrs={"class":"mw-headline","id":"Theory"}).text)

# def visible(element):
#     if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
#         return False
#     elif re.match('<!--.*-->', str(element.encode('utf-8'))):
#         return False
#     return True

# result = filter(visible, data)

# print(list(result))
