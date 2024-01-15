from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
link_page = 'https://tensor.ru/'


class TenzorMainPage:

    def search_element(*args):
        driver.get(link_page)
        el = driver.find_element(*args)
        return bool(el)
        # if bool(el) is True:
        #     return 'YES'
        # else:
        #     return 'NO'

    def click_to_button(*args):
        driver.get(link_page)
        time.sleep(4)
        link_contacts = driver.find_element(*args)
        link_contacts.click()
        time.sleep(4)
        res = driver.current_url
        return res



