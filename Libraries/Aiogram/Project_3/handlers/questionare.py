from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.states import Form
from keyboards.builders import profile
from keyboards.reply import rmk



rt = Router()

@rt.message(Command('profile'))
async def fill_profile(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer(
        'Давайте начнемо, введи своє ім\'я: ',
        reply_markup=profile(message.from_user.first_name)
    )

@rt.message(Form.name)
async def form_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.age)
    await message.answer(
        'Чудово! Тепер введіть свій вік: ',
        reply_markup=rmk
    )

@rt.message(Form.age)
async def form_age(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(Form.sex)
        await message.answer(
            'Тепер давай визначимо твій гендер: ',
            reply_markup=profile(['Хлопець', 'Дівчина'])
        )
    else:
        await message.answer('Введіть число ще раз!')

@rt.message(Form.sex, F.text.casefold().in_(['хлопець', 'дівчина']))
async def form_sex(message: Message, state: FSMContext):
    await state.update_data(sex=message.text)
    await state.set_state(Form.about)
    await message.answer('Розкажи про себе!',reply_markup=rmk)

@rt.message(Form.sex)
async def incorrect_form_sex(message: Message, state: FSMContext):
    await message.answer('Нажми на кнопку!')

@rt.message(Form.about)
async def form_about(message: Message, state: FSMContext):
    if len(message.text) < 5:
        await message.answer('Введи щось поцікавіше про себе (мінімум 5 символів).')
    else:
        await state.update_data(about=message.text)
        await state.set_state(Form.photo)
        await message.answer('Тепер відправ своє фото: ')

@rt.message(Form.photo, F.photo)
async def form_photo(message: Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    data = await state.get_data()
    await state.clear()
    
    formatted_text = []
    [
        formatted_text.append(f'{key}: {value}')
        for key, value in data.items()
    ]
    
    await message.answer_photo(
        photo_file_id,
        '\n'.join(formatted_text)
    )

@rt.message(Form.photo, ~F.photo)
async def incorrect_form_photo(message: Message, state: FSMContext):
    await message.answer('Відправ фото!')
