from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)

link_params_sbis = (By.CSS_SELECTOR, 'a[href="/contacts"]') #СБИС --> контакты
link_params_tenzor = (By.CSS_SELECTOR, 'a[href="https://tensor.ru/"]') #СБИС --> контакты --> tenzor



def click_to_button(link_string, *args):
    driver.get(link_string)
    time.sleep(3)
    link_contacts = driver.find_element(*args)
    # driver.implicitly_wait(10)
    link_contacts.click()


click_to_button('https://sbis.ru/', By.CSS_SELECTOR, 'a[href="/contacts"]')
click_to_button('https://sbis.ru/contacts/', By.CSS_SELECTOR, 'a[href="https://tensor.ru/"]')


def search_element(link_string, *args):
    driver.get(link_string)
    el = driver.find_element(*args)
    if bool(el) == True:
        return print('YES')
    else:
        return print('NO')


search_element('https://tensor.ru/', By.XPATH, '//*[@id="container"]')
search_element('https://tensor.ru/', By.CSS_SELECTOR, 'a[href="/about"]')
click_to_button('https://tensor.ru/', By.CSS_SELECTOR, 'a[href="/about"]')

driver.get("https://tensor.ru/")
if bool(driver.find_element(By.XPATH, '//*[@id="container"]')) == True:
    print('YES')
else:
    print('NO')

if bool(driver.find_element(By.CSS_SELECTOR, 'a[href="/about"]'))==True:
    print('YES')
else:
    print('NO')
time.sleep(5)


def get_size_picture(link_string, *args):
    driver.get(link_string)
    picture = driver.find_element(*args)
    width = picture.get_attribute("width")
    height = picture.get_attribute("height")
    return width, height


if get_size_picture('https://tensor.ru/about', By.XPATH,
                    '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img') ==\
    get_size_picture('https://tensor.ru/about', By.XPATH,
                     '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img') ==\
    get_size_picture('https://tensor.ru/about', By.XPATH,
                     '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img') ==\
    get_size_picture('https://tensor.ru/about', By.XPATH,
                     '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img'):
    print('Yesssss')
else:
    print('SizeError')
time.sleep(2)