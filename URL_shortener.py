#Author : Vasanth Kumar Desai

#Requirements
#pip install pyshorteners

#---------------------------------------------------------------------#


import pyshorteners
#creating an instance of pyshortener class
s=pyshorteners.Shortener()

#will use tiny url shorten from s class
url=s.tinyurl.short('http://vasanthdesai.me/?i=1')
print(url)
