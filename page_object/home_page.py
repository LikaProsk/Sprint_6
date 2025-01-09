from typing import Tuple

import allure
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base_class import BaseClass

from locators.home_page import block_faq_text, button_cooke, scooter_logo, yandex_logo
from urls.site_urls import home_page_url, yandex_dzen_url


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
    @allure.step('Открытие главной страницы')
    def open_home_page(self):
        self._open_page(self.driver, home_page_url)

    @allure.step('Нажатие на кнопку согласия с cooke')
    def click_button_cooke(self):
        self._click_element(self.driver, button_cooke)

    @allure.step('Проверка наличия блока "Вопросы о важном"')
    def check_visibility_block_faq_text(self):
        self._is_element_displayed(self.driver, block_faq_text)

    @allure.step('Проверка текста вопроса')
    def check_text_question(self, question_locator: Tuple[str, str], text_question: str):
        question = self._get_element_text(self.driver, question_locator)
        assert question == text_question

    @allure.step('Нажатие на вопрос')
    def click_question(self, question_locator: Tuple[str, str]):
        self._move_element_and_click(self.driver, question_locator)

    @allure.step('Проверка текста ответа')
    def check_text_answer(self, answer_locator: Tuple[str, str], text_answer: str):
        answer = self._get_element_text_and_wait(self.driver, answer_locator)
        assert answer == text_answer

    @allure.step('Нажатие на логотип "Самокат"')
    def click_scooter_logo(self):
        self._click_element(self.driver, scooter_logo)

    @allure.step('Проверка редиректа на главную страницу')
    def check_redirect_scooter_logo(self):
        assert self.driver.current_url == home_page_url

    @allure.step('Нажатие на логотип "Яндекс"')
    def click_yandex_logo(self):
        self._click_element(self.driver, yandex_logo)

    @allure.step('Проверка редиректа на страницу "Дзен"')
    def check_redirect_yandex_logo(self):
        self.switch_to_window(self.driver,1)
        wait = WebDriverWait(self.driver, 50)
        assert wait.until(EC.url_contains(yandex_dzen_url))

    @allure.step('Нажатие на 2 разные кнопки заказа на главной странице')
    def click_button_order_by_locator(self, button_order_locator: Tuple[str, str]):
        self._move_element_and_click(self.driver, button_order_locator)


