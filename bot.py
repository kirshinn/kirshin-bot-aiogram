import logging
from decouple import config
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

api_token = config('API_TOKEN')

bot = Bot(token=api_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    # await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
    # await message.answer(message.text)
    # await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
