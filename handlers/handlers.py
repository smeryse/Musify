import asyncio

from aiogram import F
from aiogram import Router
from aiogram import types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from pytube import Search

from inline_keyboard import inline_builder_from_youtube

# All handlers should be attached to the Router (or Dispatcher)
main_menu = Router()


# команда /start
@main_menu.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    # отправляем приветственное сообщение
    msg = await message.answer("Привет! Я бот для поиска и загрузки музыки. Для поиска музыки введите название песни.")
    await message.delete()
    await msg.delete()


# Обработчик текстовых сообщений
@main_menu.inline_query(Command(commands=["sound"]))
async def track_name(message: Message):
    await message.answer(text='Напиши название?')


@main_menu.message()
async def search(message: Message):
    # Получить текст от пользователя.
    search_query = message.text

    # Найти трек на ютуб (отдельная функция).
    results = Search(search_query + ' music video')

    # Отправить пользователю 5 ин лайн кнопок с треками (внизу стрелочки для перелистывания)
    buttons = [video for video in results.results[:5]]
    await message.answer(text='Выбери трек', reply_markup=inline_builder_from_youtube(buttons))
    # Можно получать лист с возможными форматами аудио и видео, и предоставлять пользователю выбор.







if __name__ == '__main__':
    msg = Message
    msg.text = 'Smooth Criminal'
    asyncio.run(search(msg))
