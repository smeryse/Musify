import logging

from aiogram import Bot, Dispatcher

from config import TELEGRAM_TOKEN_2

# Уcтанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# создаем бота и диспетчера
bot = Bot(TELEGRAM_TOKEN_2)
dp = Dispatcher(bot)
