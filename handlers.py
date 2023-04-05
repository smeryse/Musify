import os
from io import BytesIO

from aiogram import types
from aiogram.types import InputFile
from aiogram.utils.exceptions import TelegramAPIError
from pytube import YouTube

from bot import bot, dp
from database_func import is_audio_exists_in_db, add_data_to_db
from youtube_func import find_on_youtube, create_url, download_audio_from_youtube


# команда /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    # отправляем приветственное сообщение
    await message.answer("Привет! Я бот для поиска и загрузки музыки. Для поиска музыки введите название песни.")


# Обработчик текстовых сообщений
@dp.message_handler(content_types=['text'])
async def text_handler(message: types.Message):
    # Получаем название песни от пользователя
    query = message.text.strip()
    print(query)

    # Ищем видео с музыкой на YouTube
    video_id = find_on_youtube(query)
    video_url = create_url(video_id)

    # Получаем название и исполнителя трека
    yt = YouTube(video_url)
    title = yt.title
    artist = yt.author

    # Проверяем наличие записи в базе данных
    audio_id = is_audio_exists_in_db(video_id)

    if audio_id:
        # Если запись есть, отправляем аудио с этим audio_id из этого чата
        try:
            await bot.send_audio(message.chat.id, audio=audio_id, performer=artist, title=title)
        except TelegramAPIError as e:
            print(f"Ошибка при отправке аудио: {e}")
    else:
        # Если записи нет, скачиваем аудио с YouTube
        audio = download_audio_from_youtube(video_url)

        # Отправляем пользователю трек и получаем его file_id
        with open(audio, 'rb') as f:
            audio_bytes = BytesIO(f.read())
            try:
                sent_audio = await bot.send_audio(message.chat.id, audio=InputFile(audio_bytes), performer=artist,
                                                  title=title)
                audio_id = sent_audio.audio.file_id
            except TelegramAPIError as e:
                print(f"Ошибка при отправке аудио: {e}")
                return

        # Удаляем файл
        os.remove(audio)

        # Возвращаем название и исполнителя трека в качестве сообщения об успешной отправке
        await message.answer(f'Трек "{title}" от {artist} успешно отправлен.')

        # Добавляем информацию о треке в базу данных
        add_data_to_db(message.chat.id, video_id, audio_id)
