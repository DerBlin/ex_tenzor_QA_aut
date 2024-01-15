from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
link_page = 'https://sbis.ru/contacts'


class SbisContactsPage:

    def check_region(*args):
        driver.get(link_page)
        el = driver.find_element(*args).text
        if el == 'Ярославская обл.':
            return 'True'
        else:
            return 'False'

    def check_partners_list(*args):
        driver.get(link_page)
        time.sleep(1)
        x = driver.find_elements(*args)
        first_partners_list = []
        for el in x:
            first_partners_list.append(el.text)
        if len(first_partners_list[1:]) > 0:
            return 'Список найден'
        else:
            return 'NO'

    def change_region(*args):
        driver.get(link_page)
        time.sleep(1)
        button_first_region = driver.find_element(*args)
        button_first_region.click()
        time.sleep(1)
        new_region = driver.find_element(By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span')
        new_region.click()
        time.sleep(1)
        return driver.find_element(*args).text

    def change_and_check_person(*args):
        params_list = []
        partners_count = 0
        driver.get(link_page)
        time.sleep(1)
        button_first_region = driver.find_element(*args)
        button_first_region.click()
        time.sleep(1)
        new_region = driver.find_element(By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span')
        new_region.click()
        time.sleep(1)
        x = driver.find_elements(By.XPATH,
                                 '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div')
        new_title = driver.title
        params_list.append(new_title)
        new_url = driver.current_url
        params_list.append(new_url)
        first_partners_list = []
        for el in x:
            first_partners_list.append(el.text)
        if len(first_partners_list[1:]) > 0:
            partners_count += len(first_partners_list[1:])
            params_list.append(partners_count)
            return params_list
        else:
            params_list.append(None)
            return params_list




