
import requests
from bs4 import BeautifulSoup
res = requests.get("http://www.example.com")
soup = BeautifulSoup(res.text,"html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.head)
# print(soup.body)

# print(soup.find("h1"))
# print(soup.find_all("p"))

h1 = soup.find("h1")
h1.name
h1.text