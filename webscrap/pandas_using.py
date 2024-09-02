import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r=requests.get(url)

soup=BeautifulSoup(r.text,"lxml")

names=soup.find_all("a",class_="title")
print(names)

product_name=[]
for i in names:
    name=i.text
    product_name.append(name)
print(product_name)  


prices=soup.find_all("h4",class_="price float-end card-title pull-right")
price_list=[]
for i in prices:
    price =i.text
    price_list.append(price)

print(price_list)

desc=soup.find_all("p",class_="description card-text")

description_list=[]
for i in desc:
    d=i.text
    description_list.append(d)
print(description_list)    

reviews=soup.find_all("p",class_="review-count float-end")

rev_list=[]
for i in reviews:
    rev=i.text
    rev_list.append(rev)
print(rev_list)    

df=pd.DataFrame({"Product Name":product_name,"Prices":price_list,"Description":description_list,"Reviews":rev_list})
print(df)# arranging in the structured format we using dataframe

df.to_csv("Products_details.csv")# to get csv file format
df.to_excel("Products_details.xlsx")# to get the file in excel format