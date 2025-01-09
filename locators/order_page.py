from selenium.webdriver.common.by import By

order_page_header = (
By.XPATH, '//div[contains(text(), "Для кого самокат")]')  # Хедер страницы оформления заказа "Для кого самокат"
name_field = (By.XPATH, '//input[@placeholder="* Имя"]')  # Поле "Имя"
last_name_field = (By.XPATH, '//input[@placeholder="* Фамилия"]')  # Поле "Фамилия"
address_field = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')  # Поле "Адрес"
metro_station_field = (By.XPATH, '//input[@placeholder="* Станция метро"]')  # Поле "Станция метро"
phone_number_field = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')  # Поле "Номер телефона"
list_metro_station = (By.XPATH,
                      '//div[@class="select-search__select"]//div[contains(@class, "Order_Text")]')  # Выпадающий список станций метро
continue_button = (By.XPATH, '//button[contains(text(), "Далее")]')  # Кнопка "Далее"
about_rent_text = (By.XPATH, '//div[contains(text(), "Про аренду")]')  # Хедер страницы оформления заказа "Про аренду"
when_deliver_scooter_field = (
By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')  # Поле "Когда привезти самокат"
rent_time_field = (By.XPATH, '//span[@class="Dropdown-arrow"]')  # Поле "Срок аренды"
list_rent_time = (By.XPATH, '//div[@class="Dropdown-menu"]')  # Выпадающий список со сроком аренды
scooter_color_field = (By.XPATH, '//div[contains(@class, "Order_Title")]')  # Поле с цетами самоката
courier_comment_field = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')  # Поле  "Комментарий для курьера"
scooter_color_black = (By.XPATH, '//label[@for="black"]')  # Чекбокс с черным цветом самоката
scooter_color_grey = (By.XPATH, '//label[@for="grey"]')  # Чекбокс с серым цветом самоката
order_button = (By.XPATH,
                '//div[contains(@class, "Order_Buttons")]//button[contains(text(), "Заказать")]')  # Кнопка "Заказать" для дальнейшего оформления заказа
confirm_order_button = (By.XPATH, '//button[contains(text(), "Да")]')  # Кнопка подтверждения заказа
success_order_text = (
By.XPATH, '//div[contains(text(), "Заказ оформлен")]')  # Всплывающее окно успешного оформления заказа
