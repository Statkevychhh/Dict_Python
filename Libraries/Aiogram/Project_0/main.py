import random
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandObject
from aiogram.enums.dice_emoji import DiceEmoji


bot = Bot('6766705740:AAF4_Me_Zv6arFfsUBgJZ0on71TQNTZeMUY', parse_mode='HTML')
dp = Dispatcher()


@dp.message(F.text == '/start')
async def cmd_start(message: types.Message):
    await message.answer(f'<b>{message.from_user.first_name}</b>, вітаю вас в магазині кросовок!')

@dp.message(Command(commands=['rn', 'random-number']))
async def random_num(message: types.Message, command: CommandObject):
     a, b = [int(n) for n in command.args.split('-')]
     rnum = random.randint(a, b)
     
     await message.reply(f'Random number: {rnum}')

@dp.message(F.text == 'play')
async def play_game(message: types.Message):
    x = await message.answer_dice(DiceEmoji.DICE)
    print(x.dice.value)

@dp.message()
async def play_game(message: types.Message):
    await message.answer(f'I don\'t understand you!')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())