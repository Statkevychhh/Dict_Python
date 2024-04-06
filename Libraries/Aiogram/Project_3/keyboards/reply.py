from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType, 
    ReplyKeyboardRemove
)


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Смайлики'), 
        KeyboardButton(text='Посилання')
        ],
        [
        KeyboardButton(text='Калькулятор'), 
        KeyboardButton(text='Спец. кнопки')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Виберіть дію в меню',
    selective=True
)


spec_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Відправити гео', request_location=True), 
        KeyboardButton(text='Відправити контакт', request_contact=True),
        KeyboardButton(text='Відправити голосування', request_poll=KeyboardButtonPollType())  # type=['quiz', 'regular']
        ],
        [
        KeyboardButton(text='НАЗАД')
        ]
    ],
    resize_keyboard=True
)


rmk = ReplyKeyboardRemove()