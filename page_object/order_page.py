import random

import allure

from page_object.base_class import BaseClass

from locators.order_page import order_page_header, name_field, last_name_field, address_field, metro_station_field, \
    list_metro_station, phone_number_field, continue_button, about_rent_text, when_deliver_scooter_field, \
    rent_time_field, list_rent_time, courier_comment_field, order_button, confirm_order_button, success_order_text
from urls.site_urls import order_page_url


class OrderPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открытие страницы оформления заказа')
    def open_order_page(self):
        self._open_page(order_page_url)

    @allure.step('Проверка наличия хедера оформления заказа')
    def check_visibility_order_page_header(self):
        self._is_element_displayed(order_page_header)

    @allure.step('Заполнения поля "Имя"')
    def send_keys_name_field(self, value: str):
        self._send_keys(name_field, value)

    @allure.step('Заполнения поля "Фамилия"')
    def send_keys_last_name_field(self, value: str):
        self._send_keys(last_name_field, value)

    @allure.step('Заполнения поля "Адрес"')
    def send_keys_address_field(self, value: str):
        self._send_keys(address_field, value)

    @allure.step('Нажатие на поле "Станция метро" для раскрытия выпадающего списка')
    def click_metro_station_field(self):
        self._click_element(metro_station_field)

    @allure.step('Выбор станции метро из выпадающего списка')
    def random_select_metro_station(self):
        list_metro_station_elements = self.get_elements(list_metro_station)
        metro_station = list_metro_station_elements[random.randint(0, len(list_metro_station_elements))]
        metro_station.click()

    @allure.step('Заполнение поля "Номер телефона"')
    def send_keys_phone_number_field(self, value: str):
        self._send_keys(phone_number_field, value)

    @allure.step('Нажатие кнопки "Далее"')
    def click_continue_button(self):
        self._click_element(continue_button)

    @allure.step('Проверка наличия хедера "Про аренду"')
    def check_visibility_about_rent_text(self):
        self._is_element_displayed(about_rent_text)

    @allure.step('Заполнение поля "Когда привезти самокат"')
    def send_keys_when_deliver_scooter_field(self, value: str):
        self._send_keys(when_deliver_scooter_field, value)

    @allure.step('Нажатие на поле "Срок аренды" для раскрытия выпадающего списка')
    def click_rent_time_field(self):
        self._click_element(rent_time_field)

    @allure.step('Выбор срока аренды из выпадающего списка')
    def random_select_rent_time(self):
        list_rent_time_elements = self.get_elements(list_rent_time)
        rent_time = list_rent_time_elements[random.randint(0, len(list_rent_time_elements) - 1)]
        rent_time.click()

    @allure.step('Выбор цвета самоката в чекбоксе')
    def select_random_scooter_color(self, color_locators_list: list):
        random_color_locator = color_locators_list[random.randint(0, len(color_locators_list) - 1)]
        self._click_element(random_color_locator)

    @allure.step('Заполнение поля "Комментарий курьеру"')
    def send_keys_courier_comment_field(self, value: str):
        self._send_keys(courier_comment_field, value)

    @allure.step('Нажатие кнопки "Заказать"')
    def click_order_button(self):
        self._click_element(order_button)

    @allure.step('Нажатие кнопки подтверждения заказа')
    def click_confirm_order_button(self):
        self._click_element(confirm_order_button)

    @allure.step('Проверка наличия всплывающего окна об успешном оформлении заказа')
    def check_success_order_text(self):
        success_message = self._get_element_text_and_wait(success_order_text)
        assert 'Заказ оформлен' in success_message
