from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Dict, Any, Awaitable


class TestMidleware(BaseMiddleware):
    def __init__(self):
        ...
    
    async def __call__(self,
                      handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                      event: TelegramObject,
                      data: Dict[str, Any]) -> Any:
        print('Дія до обробника')
        result = await handler(event, data)
        print('Дія до обробника')
        return result