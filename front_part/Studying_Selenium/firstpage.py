from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("http://www.example.com")

# with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
#     driver.get("http://www.example.com")
#     print(driver.page_source)

from selenium.webdriver.common.by import By
with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.get("http://www.example.com")
    for element in driver.find_elements(By.TAG_NAME,"p"):
        print(element.text)
