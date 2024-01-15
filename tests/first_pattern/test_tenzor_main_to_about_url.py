from selenium.webdriver.common.by import By
from pages.first_pattern.tenzor_main_page import TenzorMainPage


def test_tenzor_main_to_about_url():
    assert 'https://tensor.ru/about' == TenzorMainPage.click_to_button(By.CSS_SELECTOR, 'a[href="/about"]')