import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/computers"

r=requests.get(url)
# print(r)

soup =BeautifulSoup(r.text,"lxml")
#print(soup.div.ul)# to find the individual tags in the web page

tag=soup.header
print(tag.attrs) # to show the attributes in the any tags
atb=tag.attrs
print(atb["role"])# to show the inside the class attributes


tag=soup.div.p.string #  to print inside the tag only   Navigable strings can be obtained by .
print(tag)

