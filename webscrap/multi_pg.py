import requests
from bs4 import BeautifulSoup

for i in range(2, 11):
    url = "https://www.flipkart.com/search?q=samsung+5g+mobile+under+50000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_5_18_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_5_18_na_na_ps&as-pos=5&as-type=RECENT&suggestionId=samsung+5g+mobile+under+50000&requestId=093ec403-985a-4e52-9c5b-8df8f4f62779&as-searchtext=mobile+under+50000&page=" + str(i)
    
    r = requests.get(url)
    print(f"Status Code for Page {i}: {r.status_code}")

    soup = BeautifulSoup(r.text, "lxml")
    
    np_tag = soup.find("a", class_="_9QVEpD")
    
    if np_tag:
        np = np_tag.get("href")
        cnp = "https://www.flipkart.com" + np
        print(f"Next Page URL: {cnp}")
    else:
        print(f"No 'Next Page' link found on Page {i}")
