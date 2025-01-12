from locators.home_page import header_order_button, body_order_button

order_test_case = {
    'header_order_button':
        {'order_button': header_order_button,
         'name_field': 'Лиля',
         'last_name_field': 'Иванова',
         'address_field': 'Маросейка, 34',
         'phone_number_field': '89665441412',
         'when_deliver_scooter_field': '15.01.2025',
         'courier_comment_field': 'оставить у двери'
         },
    'body_order_button':
        {'order_button': body_order_button,
         'name_field': 'Илья',
         'last_name_field': 'Цветков',
         'address_field': 'Тверская, 101',
         'phone_number_field': '89629449444',
         'when_deliver_scooter_field': '19.01.2025',
         'courier_comment_field': 'домофон 20В'
         }

}
