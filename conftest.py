import allure
import pytest
from selenium import webdriver


@allure.step('Открываем и закрываем браузер')
@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
