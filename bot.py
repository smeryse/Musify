import asyncio
import logging

from aiogram import Dispatcher, Bot

from config import TELEGRAM_TOKEN
from create_bot import dp, bot
from handlers.callbacks import callbacks
from handlers.handlers import main_menu

# Задаём уровень логирования
logging.basicConfig(level=logging.INFO)


def on_startup():
    print('Бот запущен')


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


async def main() -> None:
    from create_bot import bot, dp

    # ... and all other routers should be attached to Dispatcher
    dp.include_router(main_menu)
    dp.include_router(callbacks)

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
