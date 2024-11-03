import time
import csv
from  selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.divan.ru/kaluga/category/podvesnye-svetilniki"

driver.get(url)
time.sleep(3)
lamps = driver.find_elements(By.CLASS_NAME, 'WdR1o')
#print(lamps)

#Создаем список
parsed_data = []

#Перебираем лампы
for lamp in lamps:
    try:
        #Находим название светильника
        name = lamp.find_element(By.CSS_SELECTOR, 'div.lsooF span::text').get()
        #Находим цену светильника
        price = lamp.find_element(By.CSS_SELECTOR, 'div.pY3d2 span::text').get()
        #Находим ссылку с помощью атрибута 'href'
        link = lamp.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
    except:
        print("произошла ошибка при парсинге")
        continue

# Вносим найденную информацию в список
parsed_data.append([name, price, link])

# Закрываем подключение браузера
driver.quit()

# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("lamps.csv", 'w',newline='', encoding='utf-8') as file:
# Используем модуль csv и настраиваем запись данных в виде таблицы
# Создаём объект
writer = csv.writer(file)
# Создаём первый ряд
writer.writerow(['Название светильника', 'цена', 'ссылка на светильник'])

# Прописываем использование списка как источника для рядов таблицы
writer.writerows(parsed_data)