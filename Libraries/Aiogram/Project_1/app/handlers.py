from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb
from app.database.requests import get_product



router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привіт, {message.from_user.first_name}!', reply_markup=kb.main)

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Виберіть варіант із каталога', reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category_selected(callback: CallbackQuery):
    category_id = callback.data.split('_')[1]
    await callback.message.answer(f'Товари по вибраній категорії: ', reply_markup=await kb.products(category_id))
    await callback.answer('')

@router.callback_query(F.data.startswith('product_'))
async def product_selected(callback: CallbackQuery):
    product_id = callback.data.split('_')[1]
    product = await get_product(product_id=product_id)
    await callback.message.answer(f'Ваш товар: <b>{product.name}</b>\n\n{product.description}\n\nЦіна: {product.price}$')
    await callback.answer(f'Ви вибрали: {product.name}')
