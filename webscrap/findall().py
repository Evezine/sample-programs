import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r=requests.get(url)
# print(r)

soup =BeautifulSoup(r.text,"lxml")

prices =soup.find_all("h4",class_="price float-end card-title pull-right")
print(len(prices))
for i in prices:
 print(i.text)
print(prices[3])# particular block retrieving