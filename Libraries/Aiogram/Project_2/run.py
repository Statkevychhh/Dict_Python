import os
from dotenv import load_dotenv

import asyncio
import logging

import aiogram
from aiogram import Bot, Dispatcher

from app.handlers import router


load_dotenv()
key = os.getenv('TOKEN')

bot = Bot(token=key)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')