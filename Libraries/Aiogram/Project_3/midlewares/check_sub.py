from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from keyboards.inline import sub_channel


class CheckFollowing(BaseMiddleware):
    async def __call__(self, 
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
    #   bot = data.get('bot')
        chat_member = await event.bot.get_chat_member(chat_id='@pythonnnchik', user_id=event.from_user.id)
        
        if chat_member.status == 'left':
            await event.answer('Підпишись на канал!', reply_markup=sub_channel)
        else:
            result = await handler(event, data)
            return result