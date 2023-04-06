import logging

from aiogram.utils import executor

from create_bot import dp

# Задаём уровень логирования
logging.basicConfig(level=logging.INFO)


def on_startup():
    print('Бот запущен')

# Регистрируем хендлеры из hendlers.py
from handlers import handlers

handlers.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup())
