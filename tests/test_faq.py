import allure
import pytest

from data.faq import faq_test_case
from page_object.home_page import HomePage


class TestFAQ:

    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на каждый вопрос и проверяем соответствующий текст')
    @pytest.mark.parametrize('question_and_answer', faq_test_case.values(),
                             ids=faq_test_case.keys())
    def test_question(self, driver, question_and_answer: dict):
        home_page_object = HomePage(driver)
        home_page_object.open_home_page()
        home_page_object.click_button_cooke()
        home_page_object.check_visibility_block_faq_text()
        home_page_object.check_text_question(question_and_answer.get('question_locator'),
                                             question_and_answer.get('question'))
        home_page_object.click_question(question_and_answer.get('question_locator'))
        home_page_object.check_text_answer(question_and_answer.get('answer_locator'), question_and_answer.get('answer'))
