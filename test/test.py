import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

from config import TELEGRAM_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Progress(StatesGroup):
    progress = State()


@dp.message_handler(Command('start'))
async def start_handler(message: types.Message):
    msg = await bot.send_message(chat_id=message.chat.id, text='Процесс загрузки начат')
    for percent in range(10, 101, 10):
        await msg.edit_text(str(percent))
        await asyncio.sleep(2)
    await msg.edit_text('Процесс загрузки завершен')


if __name__ == '__main__':
    asyncio.run(dp.start_polling())
