import asyncio
import logging
from aiogram import Bot, Dispatcher

from handlers import user_messages, user_commands, questionare
from callbacks import pagination

from config_reader import config
from midlewares.check_sub import CheckFollowing
from midlewares.antiflood import AntiFloodMiddleware



async def main():
    bot = Bot(config.bot_token.get_secret_value(), parse_mode='HTML')
    dp = Dispatcher()
    
    # dp.message.middleware(CheckFollowing())
    # dp.message.middleware(AntiFloodMiddleware())
    
    dp.include_routers(
        user_commands.rt,
        pagination.rt,
        questionare.rt,
        user_messages.rt
    )
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)    
    asyncio.run(main())
