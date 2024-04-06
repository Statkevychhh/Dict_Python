import random

from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, CommandObject
from keyboards.reply import main_kb

from filters.is_admin import IsAdmin
from filters.is_digit_or_float import CheckForDigit


rt = Router()

@rt.message(CommandStart())
async def start(message: Message):
    await message.answer('Hello, Aiogram 3.x', reply_markup=main_kb)

@rt.message(Command('admin'), IsAdmin(895617317))
async def start(message: Message):
    await message.answer(f'Ти адмін!!', reply_markup=main_kb)


@rt.message(Command('pay'), CheckForDigit())
async def pay_the_order(message: Message, command: CommandObject) -> None:
    await message.answer(f'Ви успішно оплатили товар!')


@rt.message(Command(commands=['rn', 'random-number']))
async def random_num(message: Message, command: CommandObject):
    a, b = [int(n) for n in command.args.split('-')]
    rnum = random.randint(a, b)
     
    await message.reply(f'Random number: {rnum}')

@rt.message(Command('test'))
async def test(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, 'test')
