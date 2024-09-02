import requests
from bs4 import BeautifulSoup
import re #regular expression find the pattern in a string


url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r=requests.get(url)

soup =BeautifulSoup(r.text,"lxml")
data=soup.find_all(string=re.compile("Galaxy")) # it retrieves the similar word in the web pages
print(data)