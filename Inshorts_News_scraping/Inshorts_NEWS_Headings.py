# Author: Vasanth Desai
# Date: 10/06/2020
# Title: Scraping news headings from Inshorts

from bs4 import BeautifulSoup
import requests
from datetime import datetime
now = datetime.now()

print("Today",now.strftime("%B %d, %Y %H:%M:%S"),"\n")
source=requests.get('https://inshorts.com/en/read').text
soup=BeautifulSoup(source,'lxml')
for news in soup.find_all('div', class_='news-card-title news-right-box'):
    headings=news.span.text
    print('#  ', headings)
