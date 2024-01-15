from pages.first_pattern.tenzor_about_page import TenzorAboutPage, size_list
from selenium.webdriver.common.by import By


def test_size_photo():
    TenzorAboutPage.clear_size_list()
    TenzorAboutPage.get_size_picture(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img')
    TenzorAboutPage.get_size_picture(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img')
    TenzorAboutPage.get_size_picture(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img')
    TenzorAboutPage.get_size_picture(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img')
    assert "Все фото одинакового размера" == TenzorAboutPage.comparison_size(size_list)

