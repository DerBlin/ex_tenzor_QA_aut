from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import urllib.request
import os
import re

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
link_page = 'https://sbis.ru/download?tab=plugin&innerTab=default'


class SbisDownload:

    def download_plugin(*args):
        driver.get(link_page)
        destination = 'plugin.exe'
        x = driver.find_element(By.CSS_SELECTOR,
                                'a[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')
        link_down = x.get_attribute('href')
        urllib.request.urlretrieve(link_down, destination)
        time.sleep(5)

    def check_complete_download(*args):
        if os.path.isfile('plugin.exe'):
            return "Файл существует"
        else:
            return "Файл не существует"

    def find_size_plugin(*args):
        file_name = 'plugin.exe'
        file_size_bytes = os.path.getsize(file_name)
        file_size_megabytes = float(file_size_bytes / 1048576)
        return round(file_size_megabytes, 2)

    def get_web_size_plugin(*args):
        driver.get(link_page)
        x = driver.find_element(By.CSS_SELECTOR,
                                'a[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')
        text = x.text
        pattern = '(\d+|\d)(.)(\d+)'
        web_size = float(re.search(pattern=pattern, string=text).group())
        return round(web_size, 2)


