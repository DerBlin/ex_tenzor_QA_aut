from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
link_page = 'https://tensor.ru/about'
size_list = []


class TenzorAboutPage:

    def get_size_picture(*args):
        driver.get(link_page)
        time.sleep(2)
        picture = driver.find_element(*args)
        width = picture.get_attribute("width")
        height = picture.get_attribute("height")
        size_list.append([width, height])

    def comparison_size(*args):
        if size_list == sorted(size_list):
            return "Все фото одинакового размера"
        else:
            return "Не все фото одинакового размера!"

    def clear_size_list(*args):
        size_list.clear()
        return print("Словарь очищен!")





