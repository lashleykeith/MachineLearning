import requests
from bs4 import BeautifulSoup

r = requests.get("http://pythonhow.com/example.html")
c = r.content

soup = BeautifulSoup(c,"html.parser")

all = soup.find_all("div",{"class":"cities"})
all[0].find_all("h2")[0].text

for item in all:
    print (item.find_all("p")[0].text)