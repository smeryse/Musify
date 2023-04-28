from aiogram import Bot
from aiogram import Dispatcher

from config import TELEGRAM_TOKEN

# создаем бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN, parse_mode="HTML")
dp = Dispatcher()
