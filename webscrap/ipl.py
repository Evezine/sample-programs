import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://www.iplt20.com/auction/2022"

r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find("table",class_="ih-td-tab auction-tbl")
# print(table)

header=table.find_all("th")
# print(header)

titles=[]

for i in header:
    title=i.text
    titles.append(title)

# print(titles)

df =pd.DataFrame(columns=titles)
# print(df)

rows=table.find_all("tr")
# print(rows)

for i in rows[1:]:
    first_td =i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()# to remove /n we use strip (space)

    data=i.find_all("td")[1:]
    row= [tr.text for tr in data]
    row.insert(0,first_td)
    l=len(df)
    df.loc[l]=row#locating the l
print(df)    

df.to_csv("ipl_auction_stats_2022.csv")