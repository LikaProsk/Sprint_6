from selenium.webdriver.common.by import By

block_faq_text = (By.XPATH, '//div[contains(text(), "Вопросы о важном")]')  # Блок "Вопросы о важном"
question_cost_and_payment = (By.ID, 'accordion__heading-0')  # Вопрос "Сколько это стоит? И как оплатить?"
answer_cost_and_payment = (By.ID, 'accordion__panel-0')  # Ответ на вопрос "Сколько это стоит? И как оплатить?"
button_cooke = (By.ID, 'rcc-confirm-button')  # Кнопка согласия на сбор данных cooke
question_about_few_scooters = (By.ID, 'accordion__heading-1')  # Вопрос "Хочу сразу несколько самокатов! Так можно?"
answer_about_few_scooters = (
By.ID, 'accordion__panel-1')  # Ответ на вопрос "Хочу сразу несколько самокатов! Так можно?"
question_rent_time = (By.ID, 'accordion__heading-2')  # Вопрос "Как рассчитывается время аренды?"
answer_rent_time = (By.ID, 'accordion__panel-2')  # Ответ на вопрос "Как рассчитывается время аренды?"
question_scooter_for_today = (By.ID, 'accordion__heading-3')  # Вопрос "Можно ли заказать самокат прямо на сегодня?"
answer_scooter_for_today = (
By.ID, 'accordion__panel-3')  # Ответ на вопрос "Можно ли заказать самокат прямо на сегодня?"
question_prolong_order_or_return_earlier = (
By.ID, 'accordion__heading-4')  # Вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
answer_prolong_order_or_return_earlier = (
By.ID, 'accordion__panel-4')  # Ответ на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
question_about_charger = (By.ID, 'accordion__heading-5')  # Вопрос "Вы привозите зарядку вместе с самокатом?"
answer_about_charger = (By.ID, 'accordion__panel-5')  # Ответ на вопрос "Вы привозите зарядку вместе с самокатом?"
question_cancel = (By.ID, 'accordion__heading-6')  # Вопрос "Можно ли отменить заказ?"
answer_cancel = (By.ID, 'accordion__panel-6')  # Ответ на вопрос "Можно ли отменить заказ?"
question_far_away_delivery = (By.ID, 'accordion__heading-7')  # Вопрос "Я жизу за МКАДом, привезёте?"
answer_far_away_delivery = (By.ID, 'accordion__panel-7')  # Ответ на вопрос "Я жизу за МКАДом, привезёте?"
header_order_button = (By.XPATH,
                       "//div[contains(@class, 'Header_Nav')]//button[contains(text(), 'Заказать')]")  # Кнопка "Заказать" наверху страницы (в хедере)
body_order_button = (By.XPATH,
                     "//div[contains(@class, 'Home_RoadMap')]//button[contains(text(), 'Заказать')]")  # Кнопка "Заказать" внизу страницы
scooter_logo = (By.XPATH, "//a[@href='/']")  # Логотип "Самокат"
yandex_logo = (By.XPATH, "//a[@href='//yandex.ru']")  # Логотип "Яндекс"
