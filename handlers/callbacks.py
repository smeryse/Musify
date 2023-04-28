from aiogram import Router, F
from aiogram.types import CallbackQuery

from tools.regexp import YOUTUBE_ID_REGEXP
from tools.youtube_functions import download_audio_youtube

callbacks = Router()


@callbacks.callback_query(F.data.regexp(YOUTUBE_ID_REGEXP))
async def audio_download(callback: CallbackQuery):
    video_id = str(callback.data)

    # Отправить информацию о выбранном треке.
    await callback.answer('Скачиваем...')

    # Скачать трек (Добавить выбор качества скачивания)
    audio_path = download_audio_youtube(video_id)

    # Убедиться в том, что трек загрузился на сервера телеграм.
    await callback.message.answer_audio(audio=audio_path)
    # Удалить трек.
    # Оповещать пользователя с помощью result: bool = await bot.answer_callback_query(...)
