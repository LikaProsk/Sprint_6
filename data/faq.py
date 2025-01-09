from locators.home_page import question_cost_and_payment, answer_cost_and_payment, question_about_few_scooters, \
    answer_about_few_scooters, question_rent_time, answer_rent_time, question_scooter_for_today, \
    answer_scooter_for_today, question_prolong_order_or_return_earlier, answer_prolong_order_or_return_earlier, \
    question_about_charger, answer_about_charger, question_cancel, answer_cancel, answer_far_away_delivery, \
    question_far_away_delivery

text_question_cost_and_payment = "Сколько это стоит? И как оплатить?"
text_answer_cost_and_payment = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
text_question_about_few_scooters = "Хочу сразу несколько самокатов! Так можно?"
text_answer_about_few_scooters = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
text_question_rent_time = "Как рассчитывается время аренды?"
text_answer_rent_time = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
text_question_scooter_for_today = "Можно ли заказать самокат прямо на сегодня?"
text_answer_scooter_for_today = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
text_question_prolong_order_or_return_earlier = "Можно ли продлить заказ или вернуть самокат раньше?"
text_answer_prolong_order_or_return_earlier = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
text_question_about_charger = "Вы привозите зарядку вместе с самокатом?"
text_answer_about_charger = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
text_question_cancel = "Можно ли отменить заказ?"
text_answer_cancel = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
text_question_far_away_delivery = "Я жизу за МКАДом, привезёте?"
text_answer_far_away_delivery = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

faq_test_case = {
    'question_cost_and_payment':
        {'question': text_question_cost_and_payment,
         'question_locator': question_cost_and_payment,
         'answer': text_answer_cost_and_payment,
         'answer_locator': answer_cost_and_payment},
    'question_about_few_scooters':
        {'question': text_question_about_few_scooters,
         'question_locator': question_about_few_scooters,
         'answer': text_answer_about_few_scooters,
         'answer_locator': answer_about_few_scooters},
    'question_rent_time':
        {'question': text_question_rent_time,
         'question_locator': question_rent_time,
         'answer': text_answer_rent_time,
         'answer_locator': answer_rent_time},
    'question_scooter_for_today':
        {'question': text_question_scooter_for_today,
         'question_locator': question_scooter_for_today,
         'answer': text_answer_scooter_for_today,
         'answer_locator': answer_scooter_for_today},
    'question_prolong_order_or_return_earlier':
        {'question': text_question_prolong_order_or_return_earlier,
         'question_locator': question_prolong_order_or_return_earlier,
         'answer': text_answer_prolong_order_or_return_earlier,
         'answer_locator': answer_prolong_order_or_return_earlier},
    'question_about_charger':
        {'question': text_question_about_charger,
         'question_locator': question_about_charger,
         'answer': text_answer_about_charger,
         'answer_locator': answer_about_charger},
    'question_cancel':
        {'question': text_question_cancel,
         'question_locator': question_cancel,
         'answer': text_answer_cancel,
         'answer_locator': answer_cancel},
    'question_far_away_delivery':
        {'question': text_question_far_away_delivery,
         'question_locator': question_far_away_delivery,
         'answer': text_answer_far_away_delivery,
         'answer_locator': answer_far_away_delivery}

}
