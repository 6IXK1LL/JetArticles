from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from parser import Parser
from make import make

from config import *



bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    pass


@dp.message_handler(commands=['habr_parse'], content_types=['text'])
async def habr_parse(message: types.Message):
    URL = message.get_args()

    article: str = make(URL)

    await bot.send_message(CHANNEL, article, parse_mode='Markdown')


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)