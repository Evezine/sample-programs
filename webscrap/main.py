import requests #requests library used to get a HTTP request and response from web pages later we can scrap the data from websites.

url="https://courses.wscubetech.com/"
r= requests.get(url)
#print(r.status_code) # to know about the status of web page
print(r.text)