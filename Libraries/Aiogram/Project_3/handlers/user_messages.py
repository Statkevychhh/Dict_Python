from aiogram import Router, F
from aiogram.types import Message
from aiogram.enums.dice_emoji import DiceEmoji

from keyboards.builders import calc_kb
from keyboards.fabrics import paginator
from keyboards.inline import sources_kb
from keyboards.reply import main_kb, spec_kb

from data.subloader import get_json


rt = Router()

@rt.message(F.text == 'НАЗАД')
async def start(message: Message):
    await message.answer('Aiogram 3.x', reply_markup=main_kb)

@rt.message(F.text == 'play')
async def play_game(message: Message):
    x = await message.answer_dice(DiceEmoji.DICE)
    print(x.dice.value)
    
@rt.message(F.text.lower().in_(['хай', 'хелоу', 'привіт', 'здоров', 'прив']))
async def start(message: Message):
    await message.reply('Привііітт!')

@rt.message()
async def echo(message: Message):
    msg = message.text
    smiles = await get_json('smiles.json')
    
    if msg == 'Посилання':
        await message.answer('Ось ваші ссилки:', reply_markup=sources_kb)
    elif msg == 'Спец. кнопки':
        await message.answer('Спец. кнопки:', reply_markup=spec_kb)
    elif msg == 'Калькулятор':
        await message.answer('Калькулятор:', reply_markup=calc_kb())
    elif msg == 'Смайлики':
        await message.answer(f'{smiles[0][0]} <b>{smiles[0][1]}</b>', reply_markup=paginator())
