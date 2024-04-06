from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


sources_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='Youtube', url='https://www.youtube.com/channel/UCWyAYVyqe_0_n3l7cPp-0vg'), 
        InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/statkevychhh/'),
        InlineKeyboardButton(text='Telegram', url='https://t.me/+xWPfgdCOFCAxZTNi'),
        InlineKeyboardButton(text='Telegram', url='tg://resolve?domain=pythonnnchik')
        ],

    ],
)


sub_channel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Підписатись', url='https://t.me/pythonnnchik')
        ]
    ]
)