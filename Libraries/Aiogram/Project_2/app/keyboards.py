from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакти')]
], resize_keyboard=True, input_field_placeholder='Виберіть пункт з меню.')

settings_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Youtube', callback_data='yt')]
])

cars = ['Tesla', 'BMW', 'Mercedes']
async def reply_cars():
    keyboard = ReplyKeyboardBuilder()
    for car in cars:
        keyboard.add(KeyboardButton(text=car))
    return keyboard.adjust(2).as_markup()

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, callback_data='car'))
    return keyboard.adjust(2).as_markup()