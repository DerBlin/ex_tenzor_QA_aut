from selenium.webdriver.common.by import By
from pages.first_pattern.tenzor_main_page import TenzorMainPage


def test_people_field():
    assert True is TenzorMainPage.search_element(By.XPATH, '//*[@id="container"]')