import time
import csv
from  selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

class LampparsSpider(scrapy.Spider):
    name = "lamppars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/kaluga/category/svet"]

    def parse(self, response):
        lamps = response.css('div._Ud0k')
        for lamp in lamps:
            # Возвращаем информацию по каждой карточке
            yield {
                'name': lamp.css('div.lsooF span::text').get(),
                'price': lamp.css('div.pY3d2 span::text').get(),  # получаем цену
                'url': lamp.css('a').attrib['href']  # получаем ссылку
            }
