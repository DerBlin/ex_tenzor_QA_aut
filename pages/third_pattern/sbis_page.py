from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
link_page = 'https://sbis.ru'


class SbisPage:

    def go_to_the_download(*args):
        driver.get(link_page)
        time.sleep(1)
        x = driver.find_element(*args)
        link_to_download = x.get_attribute('href')
        driver.get(link_to_download)
        time.sleep(2)



