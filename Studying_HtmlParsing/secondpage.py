import requests
from bs4 import BeautifulSoup

res = requests.get("http://books.toscrape.com/catalogue/category/books/travel_2/index.html")

soup = BeautifulSoup(res.text,"html.parser")

# book = soup.find("h3")
# print(book.a.text)
# h3_results = soup.find_all("h3")
# for book in h3_results:
#     print(book.a["title"])

# soup.find("div")

# soup.find("div",id="results")

find_result = soup.find("div","page-header")

print(find_result.h1.text.strip())