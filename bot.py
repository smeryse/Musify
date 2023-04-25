import asyncio
import logging

from aiogram import Dispatcher, Bot

from config import TELEGRAM_TOKEN
from create_bot import dp, bot
from handlers.handlers import router

# Задаём уровень логирования
logging.basicConfig(level=logging.INFO)


def on_startup():
    print('Бот запущен')


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()

    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TELEGRAM_TOKEN, parse_mode="HTML")
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
