# Author: Vasanth Desai
# Date: 10/06/2020
# Title: Scraping Brief news from Inshorts

from bs4 import BeautifulSoup
import requests
from datetime import datetime
now = datetime.now()

print("Today",now.strftime("%B %d, %Y %H:%M:%S"),"\n")
source=requests.get('https://inshorts.com/en/read').text
soup=BeautifulSoup(source,'lxml')
for news in soup.find_all('div',itemprop="articleBody"):
    brief=news.text
    print('#  ', brief,"\n")
