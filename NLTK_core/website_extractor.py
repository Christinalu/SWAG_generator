# Need to install BeautifulSoup 4, lxml


import bs4 as bs
import urllib.request
import re

website = urllib.request.urlopen ('https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic').read()

soup = bs.BeautifulSoup(website, 'lxml')
extracted_article = ""
for item in soup.find_all ('p'):
    extracted_article = extracted_article + item.text

extracted_article = re.sub(r'\s+',' ',extracted_article)

extracted_article = re.sub(r'\[[0-9]*\]',' ',extracted_article)
