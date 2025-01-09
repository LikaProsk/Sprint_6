import allure
import pytest

from data.order import order_test_case
from locators.order_page import scooter_color_black, scooter_color_grey
from page_object.home_page import HomePage
from page_object.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description(
        'Используя две разные кнопки на главной странице и два набора разных данных оформляем заказы и проверяем успешность')
    @pytest.mark.parametrize('test_case', order_test_case.values(),
                             ids=order_test_case.keys())
    def test_order(self, driver, test_case: dict):
        order_page_object = OrderPage(driver)
        home_page_object = HomePage(driver)
        home_page_object.open_home_page()
        home_page_object.click_button_order_by_locator(test_case.get('order_button'))
        home_page_object.click_button_cooke()
        order_page_object.check_visibility_order_page_header()
        order_page_object.send_keys_name_field(test_case.get('name_field'))
        order_page_object.send_keys_last_name_field(test_case.get('last_name_field'))
        order_page_object.send_keys_address_field(test_case.get('address_field'))
        order_page_object.click_metro_station_field()
        order_page_object.random_select_metro_station()
        order_page_object.send_keys_phone_number_field(test_case.get('phone_number_field'))
        order_page_object.click_continue_button()
        order_page_object.check_visibility_about_rent_text()
        order_page_object.send_keys_when_deliver_scooter_field(test_case.get('when_deliver_scooter_field'))
        order_page_object.click_rent_time_field()
        order_page_object.random_select_rent_time()
        order_page_object.select_random_scooter_color([scooter_color_black, scooter_color_grey])
        order_page_object.send_keys_courier_comment_field(test_case.get('courier_comment_field'))
        order_page_object.click_order_button()
        order_page_object.click_confirm_order_button()
        order_page_object.check_success_order_text()
