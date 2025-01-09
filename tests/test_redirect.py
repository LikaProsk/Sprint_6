import allure

from page_object.home_page import HomePage


class TestRedirect:

    @allure.title('Проверка редиректов с главной страницы')
    @allure.description('Нажимаем на логотипы "Самокат" и "Яндекс" проверяем редиректы на корректные страницы')
    def test_redirect(self, driver):
        home_page_object = HomePage(driver)
        home_page_object.open_home_page()
        home_page_object.click_button_cooke()
        home_page_object.click_scooter_logo()
        home_page_object.check_redirect_scooter_logo()
        home_page_object.click_yandex_logo()
        home_page_object.check_redirect_yandex_logo()
