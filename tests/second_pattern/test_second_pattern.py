from selenium.webdriver.common.by import By
from pages.second_pattern.sbis_contacts import SbisContactsPage


def test_check_region():
    assert 'True' == SbisContactsPage.check_region(By.XPATH,
                                                   '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]'
                                                   '/span/span')


def test_person_list():
    assert 'Список найден' == SbisContactsPage.check_partners_list(By.XPATH,
                                                                   '//*[@id="contacts_list"]/div/div[2]/div[2]/'
                                                                   'div/div[2]/div[1]/div[3]/div')


def test_change_region():
    assert 'Камчатский край' == SbisContactsPage.change_region(By.XPATH,
                                                               '//*[@id="container"]/div[1]/div/div[3]/div[2]'
                                                               '/div[1]/div/div[2]/span/span')


def test_change_partners():
    assert 1 == SbisContactsPage.change_and_check_person(By.XPATH,
                                                         '//*[@id="container"]/div[1]/div/div[3]/div[2]/'
                                                         'div[1]/div/div[2]/span/span')[2]


def test_change_url():
    assert 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients' == SbisContactsPage.change_and_check_person(
        By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')[1]


def test_change_title():
    assert 'СБИС Контакты — Камчатский край' == SbisContactsPage.change_and_check_person(
        By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')[0]