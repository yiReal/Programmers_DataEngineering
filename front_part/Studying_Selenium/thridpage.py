
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://hashcode.co.kr/")
button = driver.find_element(By.CLASS_NAME, "UtilMenustyle__Link-sc-2sjysx-4 ewJwEL")
ActionChains(driver).click(button).perform()
time.sleep(100)