import requests
from bs4 import BeautifulSoup

r=requests.get("http://www.century21.com/real-estate/detroit-mi/LCMIDETROIT/")
c = r.content

soup = BeautifulSoup(c, "html.parser")
print(soup.prettify())