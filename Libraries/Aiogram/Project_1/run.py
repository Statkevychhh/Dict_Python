import os
import sys
import asyncio
import logging
import aiogram
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.handlers import router
from app.database.models import async_main


def load_token():
    load_dotenv()
    return os.getenv('TOKEN')

async def main():
    await async_main()
    
    token = load_token()
    bot = Bot(token=token, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(router)
    
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit') 