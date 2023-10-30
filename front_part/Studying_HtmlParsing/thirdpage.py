import requests
from bs4 import BeautifulSoup
user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
# res = requests.get("https://hashcode.co.kr/",user_agent)

# soup = BeautifulSoup(res.text,"html.parser")

# print(soup.find("li","question-list-item").find("div","question").find("div","top").h4.text)

# questions = soup.find_all("li","question-list-item")
# for question in questions:
#     print(question.find("div","question").find("div","top").h4.text)


import time
for i in range(1,6):
    res = requests.get("https://hashcode.co.kr/?page={}".format(i),user_agent)
    soup = BeautifulSoup(res.text,"html.parser")
    questions = soup.find_all("li","question-list-item")
    for question in questions:
        print(question.find("div","question").find("div","top").h4.text)
    time.sleep(0.5)