import asyncio

from aiogram import Router
from aiogram import types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from pytube import Search
from aiogram import F
from inline_keyboard import inline_builder_from_youtube

# All handlers should be attached to the Router (or Dispatcher)
router = Router()


# команда /start
@router.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    # отправляем приветственное сообщение
    msg = await message.answer("Привет! Я бот для поиска и загрузки музыки. Для поиска музыки введите название песни.")
    await message.delete()
    await msg.delete()


# Обработчик текстовых сообщений
@router.inline_query(Command(commands=["sound"]))
async def track_name(message: Message):
    await message.answer(text='Напиши название?')


@router.message()
async def search(message: Message):
    # Получить текст от пользователя.
    search_query = message.text

    # Найти трек на ютуб (отдельная функция).
    results = Search(search_query + ' music video')

    # Отправить пользователю 5 ин лайн кнопок с треками (внизу стрелочки для перелистывания)
    buttons = [video for video in results.results[:5]]
    await message.answer(text='Выбери трек', reply_markup=inline_builder_from_youtube(buttons))
    # Можно получать лист с возможными форматами аудио и видео, и предоставлять пользователю выбор.


@router.callback_query(F.data == 'download')
async def video_download(callback: CallbackQuery):
    print(callback.message.reply_markup.inline_keyboard[0][0].text)
    # TODO Надо как-то отслеживать и сохранять данные о поиске. (чтобы лишний раз не искать по video_id)
    await callback.answer('Скачиваем трек')
    # Получить метаданные трека (Название, Автор, год выпуска, альбом, жанры, обложка)
    # Отправить информацию о выбранном треке.
    # Скачать трек (Добавить выбор качества скачивания)
    # Сохранить трек на устройстве (отдельная папка для временных файлов)
    # Отправить трек пользователю.
    # Убедиться в том, что трек загрузился на сервера телеграм.
    # Удалить трек
    # Оповещать пользователя с помощью result: bool = await bot.answer_callback_query(...)
    pass


if __name__ == '__main__':
    msg = Message
    msg.text = 'Smooth Criminal'
    asyncio.run(search(msg))
