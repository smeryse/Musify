import re

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pytube import YouTube


def inline_builder_from_youtube(buttons: list[YouTube]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for button in buttons:
        builder.button(text=button.title,
                       callback_data=f'{button.video_id}')
    builder.adjust(1)
    print(re.match(r'^[A-Za-z0-9_-]{11}$', button.video_id))
    return builder.as_markup()
    # Сделать callback функции для отлова этих кнопок
    # TODO Сделать подкласс для класса поиска
    #  https://docs.aiogram.dev/en/dev-3.x/dispatcher/filters/callback_data.html
