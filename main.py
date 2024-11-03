import time
import csv
from  selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.divan.ru/kaluga/category/podvesnye-svetilniki"

driver.get(url)
time.sleep(3)
lamps = driver.find_elements(By.CLASS_NAME, 'WdR1o')