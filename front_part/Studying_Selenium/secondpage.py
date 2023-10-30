

# 스크래핑에 필요한 라이브러리를 불러와봅시다.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://indistreet.com/live?sortOption=startDate%3AASC")
# driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div[4]/div[1]/div[1]/div/a/div[2]/p[1]')
from selenium.webdriver.support import expected_conditions as EC
# with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
#     driver.get("https://indistreet.com/live?sortOption=startDate%3AASC")
#     element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div[4]/div[1]/div[1]/div/a/div[2]/p[1]')))
#     print(element)

with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.get("https://indistreet.com/live?sortOption=startDate%3AASC")
    driver.implicitly_wait(10)
    for i in range(1,11):
        element = driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div[4]/div[1]/div[{}]/div/a/div[2]/p[1]'.format(i))
        print(element.text)
