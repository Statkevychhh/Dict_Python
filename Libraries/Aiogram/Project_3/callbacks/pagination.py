from contextlib import suppress

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from data.subloader import get_json
from keyboards.reply import main_kb
from keyboards.fabrics import Pagination, paginator


rt = Router()



@rt.callback_query(Pagination.filter(F.action.in_(['prev', 'next'])))
async def pagination_handler(call: CallbackQuery, callback_data: Pagination):
    smiles = await get_json('smiles.json')
    
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0
    
    if callback_data.action == 'next':
        page = page_num + 1 if page_num < (len(smiles) - 1) else page_num
    
    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f'{smiles[page][0]} <b>{smiles[page][1]}</b>', 
            reply_markup=paginator(page)
        )
        await call.answer()