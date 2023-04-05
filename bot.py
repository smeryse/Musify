import logging

from aiogram import Bot, Dispatcher
from aiogram import executor

from config import TELEGRAM_TOKEN
from handlers import *  # импортируем все обработчики из handlers.py

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# Уcтанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# создаем бота и диспетчера
bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher(bot)

# TODO сделать обработку сообщений от лишних символов
# TODO закрывать предыдущий трек при поиске нового
# TODO сделать ограничение по длительности треков (+-30 минут)
# TODO сделать поиск только по трекам (чтобы не выдавало видео)
# TODO основное окно с инлайн клавиатурой (мои треки, мои плейлисты и тд)
