from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from config import TELEGRAM_TOKEN

# создаем бота и диспетчера
bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher(bot)
