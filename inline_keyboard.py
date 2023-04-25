from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pytube import YouTube


def inline_builder_from_youtube(buttons: list[YouTube]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for button in buttons:
        builder.button(text=button.title,
                       callback_data='download')
    builder.adjust(1)
    return builder.as_markup()
    # Сделать callback функции для отлова этих кнопок
    # TODO Сделать подкласс для класса поиска
    #  https://docs.aiogram.dev/en/dev-3.x/dispatcher/filters/callback_data.html
