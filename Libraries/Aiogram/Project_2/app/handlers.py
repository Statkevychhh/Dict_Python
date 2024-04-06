from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from app.keyboards import main_kb as kb_1
from app.keyboards import settings_kb as kb_2
from app.keyboards import reply_cars as kb_3
from app.keyboards import inline_cars as kb_4

from app.midlewares import TestMidleware



router = Router()

# router.message.middleware(TestMidleware)

class Reg(StatesGroup):
    name = State()
    number = State()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привіт, {message.from_user.first_name}! Твій ID: {message.from_user.id}', reply_markup=kb_1)

@router.message(F.text.in_(['Контакти', 'Корзина']))
async def cmd_start(message: Message):
    await message.reply(f'Привіт, {message.from_user.first_name}!', reply_markup=kb_2)

@router.message(F.text == 'Каталог')
async def cmd_start(message: Message):
    await message.reply(f'Привіт, {message.from_user.first_name}!', reply_markup=await kb_3())

@router.message(F.text.in_(['Tesla', 'BMW', 'Mercedes']))
async def cmd_start(message: Message):
    await message.reply(f'Привіт, {message.from_user.first_name}!', reply_markup=await kb_4())

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('''Список команд: 
    /start  -  Початок роботи бота
    /help  -  Вивід списку команд бота''')


@router.message(F.text == 'Як справи?')
async def how_are_you(message: Message):
    await message.answer('OK!')
    await message.answer('А в тебе як?')

@router.message(F.photo)
async def get_photo(message: Message):
    photo_id = message.photo[-1].file_id
    await message.answer(f'ID фото: {photo_id}')
    await message.answer_photo(photo=photo_id)



@router.callback_query(F.data == 'yt')
async def yout_print(callback: CallbackQuery):
    await callback.answer('Ви вибрали каталог!')
    await callback.message.edit_text('Hello!', reply_markup=await kb_4())



# FSM Context - Машина стану.
@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введіть ваше ім\'я!')

@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введіть свій номер телефону!')

@router.message(Reg.number)
async def reg_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()  
    await message.answer(f'Дякую, реєстрація завершена.\nІм\'я: {data["name"]}\nНомер: {data["number"]}')
    await state.clear()